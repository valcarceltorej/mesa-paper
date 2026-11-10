"""Mesa PAPER con datos reales (sin dinero real).
Fuentes: PumpPortal (tokens nuevos), DexScreener (precio/volumen), RugCheck.
Cada token se evalua a los 15 min, 1 h y 3 h, y se sigue su resultado.
Uso: python real.py [minutos]   (15 o menos = diagnostico rapido)
"""
import asyncio
import json
import os
import queue
import statistics
import sys
import threading
import time
from collections import Counter, defaultdict

import requests

import mesa as M

WS = "wss://pumpportal.fun/api/data"
DEX = "https://api.dexscreener.com/latest/dex/tokens/"
RUG = "https://api.rugcheck.xyz/v1/tokens/%s/report"
TICK_S = 10
RUG_POR_TICK = 2
LP_MIN = 90.0
VOL_SAT = 250_000
EDADES = [900, 3600, 10800]
HITOS = [3600, 10800]
EDADES_DIAG = [90, 240]
HITOS_DIAG = [120, 300]
ST = Counter()
MUESTRA = {}

M.R["slippage"] = 0.03
M.R["enfriamiento"] = 90


class FilterReal(M.Filter):
    """Si faltan datos de seguridad, no se opera (falla cerrado)."""

    def revisar(self, p):
        m = []
        if p.vol_1h < M.R["vol_min"]:
            m.append("volumen 1h < 50k$")
        elif None in (p.mint_revocado, p.lp_bloqueado, p.top10, p.dev_en_rugs):
            m.append("sin datos de seguridad (no se opera)")
        else:
            m += super().revisar(p).motivos
            if getattr(p, "freeze_activo", False):
                m.append("freeze authority activo")
            if getattr(p, "insiders", False):
                m.append("red de insiders detectada")
            if getattr(p, "riesgo_critico", False):
                m.append("riesgo critico segun RugCheck")
        return M.Veredicto(p, not m, m)


class AnalystReal(M.Analyst):
    def puntuar(self, v):
        if not v.ok:
            raise ValueError("Analyst: solo puntua supervivientes del Filter")
        p = v.par
        liq = min(p.vol_1h / VOL_SAT, 1.0)
        dist = max(0.0, 1 - p.top10 / M.R["top10_max"])
        mom = min(max((p.mom + 0.1) / 0.3, 0.0), 1.0)
        score = 0.4 * liq + 0.3 * dist + 0.3 * mom
        txt = "liq %.2f, reparto %.2f, momentum %.2f" % (liq, dist, mom)
        return M.Senal(v, round(score, 3), txt)


def escuchar(cola, estado):
    import websockets

    async def run():
        while True:
            try:
                async with websockets.connect(WS) as ws:
                    await ws.send(json.dumps({"method": "subscribeNewToken"}))
                    async for msg in ws:
                        ev = json.loads(msg)
                        if ev.get("mint") and ev.get("txType") == "create":
                            cola.put(ev)
            except Exception as e:
                estado["ws_error"] = str(e)[:80]
                ST["ws_reconexiones"] += 1
                await asyncio.sleep(5)

    asyncio.run(run())


def get(url):
    try:
        r = requests.get(url, timeout=15)
        if r.status_code != 200:
            ST["http_%d" % r.status_code] += 1
            return None
        return r.json()
    except Exception:
        ST["error_red"] += 1
        return None


def precios_dex(mints):
    out = {}
    for i in range(0, len(mints), 30):
        d = get(DEX + ",".join(mints[i:i + 30]))
        for p in (d or {}).get("pairs") or []:
            if p.get("chainId") != "solana":
                continue
            m = (p.get("baseToken") or {}).get("address")
            liq = (p.get("liquidity") or {}).get("usd") or 0
            if m and (m not in out or liq > out[m]["liq"]):
                out[m] = {
                    "precio": float(p.get("priceUsd") or 0),
                    "vol": float((p.get("volume") or {}).get("h1") or 0),
                    "liq": float(liq),
                    "mom": float(
                        (p.get("priceChange") or {}).get("m5") or 0) / 100}
    return out


def seguridad(mint):
    rep = get(RUG % mint)
    if rep is None:
        return None
    tok = rep.get("token") or {}
    riesgos = rep.get("risks") or []
    if "claves" not in MUESTRA:
        MUESTRA["claves"] = sorted(rep.keys())
        MUESTRA["holder0"] = (rep.get("topHolders") or [None])[0]
    for r in riesgos:
        MUESTRA.setdefault("riesgos", {})[r.get("name")] = r.get("level")

    def revocada(k):
        v = rep[k] if k in rep else tok.get(k, "?")
        return None if v == "?" else (v is None)

    markets = rep.get("markets") or []
    locks = [(x.get("lp") or {}).get("lpLockedPct") or 0 for x in markets]
    lock = max(locks, default=None)
    ths = rep.get("topHolders") or []
    nombres = [(r.get("name") or "").lower() for r in riesgos]
    dev = bool(rep.get("rugged")) or any(
        "creator" in n and "rug" in n for n in nombres)
    return {
        "mint_revocado": revocada("mintAuthority"),
        "lp_bloqueado": None if lock is None else lock >= LP_MIN,
        "top10": (sum(float(h.get("pct") or 0) for h in ths[:10]) / 100
                  if ths else None),
        "dev_en_rugs": dev,
        "freeze_activo": revocada("freezeAuthority") is False,
        "insiders": bool(rep.get("graphInsidersDetected"))
        or bool(rep.get("insiderNetworks")),
        "riesgo_critico": any(
            (r.get("level") or "").lower() == "danger" for r in riesgos)}


def correr_real(minutos):
    diag = minutos <= 15
    edades = EDADES_DIAG if diag else EDADES
    hitos = HITOS_DIAG if diag else HITOS
    os.makedirs("datos_mesa", exist_ok=True)
    dia = time.strftime("%Y%m%d_%H%M")
    c, risk = M.Cartera(), M.Risk()
    log = M.Logger("datos_mesa/registro_%s.jsonl" % dia)
    ex, filt, ana = M.Executor(c), FilterReal(), AnalystReal()
    cola, estado = queue.Queue(), {}
    threading.Thread(target=escuchar, args=(cola, estado), daemon=True).start()
    espera, segur, track, px, hist = [], [], [], {}, []
    fin, t, ult_panel = time.time() + minutos * 60, 0, 0

    def evaluar(par, etapa):
        log.log(t, "Scout", "nuevo par", mint=par.mint, origen=par.origen,
                etapa=etapa)
        v = filt.revisar(par)
        if not v.ok:
            log.log(t, "Filter", "descarte", mint=par.mint,
                    motivos=v.motivos, etapa=etapa)
            return "descartado: " + v.motivos[0]
        log.log(t, "Filter", "pasa", mint=par.mint, etapa=etapa)
        s = ana.puntuar(v)
        if s.score < M.R["score_min"]:
            log.log(t, "Analyst", "descarte", mint=par.mint, score=s.score,
                    motivos=["score %.2f < 0.60" % s.score], etapa=etapa)
            return "descartado: score bajo"
        log.log(t, "Analyst", "aprobado", mint=par.mint, score=s.score,
                motivo=s.motivo, etapa=etapa)
        antes = len(c.pos)
        ex.abrir(s, px, t, log)
        return "operado" if len(c.pos) > antes else "rechazado por Executor"

    while time.time() < fin:
        ini = time.time()
        while not cola.empty():
            ev = cola.get()
            espera.append({"t0": time.time(), "mint": ev["mint"], "etapa": 0,
                           "next": time.time() + edades[0]})
            ST["tokens_vistos"] += 1
        if c.pos:
            for m, d in precios_dex(list(c.pos)).items():
                if d["precio"] > 0:
                    px[m] = d["precio"]
        for m, motivo in risk.vigilar(c, px, log, t):
            ex.cerrar(m, motivo, px, t, log)
        ahora = time.time()
        listos = [w for w in espera if ahora >= w["next"]][:60]
        for w in listos:
            espera.remove(w)
        datos = precios_dex([w["mint"] for w in listos]) if listos else {}
        for w in listos:
            e, d = w["etapa"], datos.get(w["mint"])
            if d is None or d["precio"] <= 0:
                if ahora - (w["t0"] + edades[e]) < 1800:
                    w["next"] = ahora + 120
                    espera.append(w)
                    continue
                ST["sin_par"] += 1
                log.log(t, "Scout", "descarte", mint=w["mint"], etapa=e,
                        motivos=["sin par en DexScreener"])
            else:
                ST["evaluaciones"] += 1
                px[w["mint"]] = d["precio"]
                par = M.Par(w["mint"], "pumpfun", d["precio"], d["vol"],
                            None, None, None, None, d["mom"])
                if d["vol"] >= M.R["vol_min"]:
                    segur.append({"par": par, "intentos": 0, "etapa": e})
                else:
                    evaluar(par, e)
            w["etapa"] = e + 1
            if w["etapa"] < len(edades):
                w["next"] = w["t0"] + edades[w["etapa"]]
                espera.append(w)
        for item in segur[:RUG_POR_TICK]:
            segur.remove(item)
            par = item["par"]
            s = seguridad(par.mint)
            ST["rugcheck_llamadas"] += 1
            if s is None and item["intentos"] < 3:
                item["intentos"] += 1
                segur.append(item)
                continue
            if s is not None:
                for k, val in s.items():
                    setattr(par, k, val)
            nuevo = precios_dex([par.mint]).get(par.mint)
            if nuevo and nuevo["precio"] > 0:
                par.precio, par.vol_1h, par.mom = (
                    nuevo["precio"], nuevo["vol"], nuevo["mom"])
                px[par.mint] = nuevo["precio"]
            dec = evaluar(par, item["etapa"])
            track.append({"mint": par.mint, "t0": time.time(),
                          "p0": par.precio, "dec": dec, "hitos": list(hitos)})
            time.sleep(2.5)
        ahora = time.time()
        debidos = [w for w in track
                   if w["hitos"] and ahora - w["t0"] >= w["hitos"][0]]
        if debidos:
            d2 = precios_dex(sorted({w["mint"] for w in debidos}))
            for w in debidos:
                h, x = w["hitos"].pop(0), d2.get(w["mint"])
                ok = x and x["precio"] > 0 and w["p0"] > 0
                log.log(t, "Logger", "resultado", mint=w["mint"],
                        horizonte_s=h, decision=w["dec"],
                        ret=round(x["precio"] / w["p0"] - 1, 4) if ok else None)
            track[:] = [w for w in track if w["hitos"]]
        hist.append(c.equity(px))
        t += 1
        if time.time() - ult_panel > 60:
            ult_panel = time.time()
            print(M.panel(t, c, log, hist, px))
            print(" tokens vistos %d, evaluaciones %d, en espera %d" % (
                ST["tokens_vistos"], ST["evaluaciones"], len(espera)),
                flush=True)
            log.f.flush()
        time.sleep(max(0, TICK_S - (time.time() - ini)))
    cierre(c, log, hist, dia, estado)


def seguimiento(log):
    g, sin = defaultdict(list), 0
    for e in log.eventos:
        if e["tipo"] != "resultado":
            continue
        if e["ret"] is None:
            sin += 1
        else:
            g[(e["decision"], e["horizonte_s"])].append(e["ret"])
    L = ["", "SEGUIMIENTO (que paso con los tokens que llegaron al analisis)"]
    for (dec, h), r in sorted(g.items(), key=lambda kv: -len(kv[1]))[:14]:
        L.append("  n=%3d  media %+5.0f%%  mediana %+5.0f%%  %s  (a %d min)" % (
            len(r), 100 * sum(r) / len(r), 100 * statistics.median(r),
            dec, h // 60))
    L.append("  sin datos de precio posterior: %d" % sin)
    return L


def cierre(c, log, hist, dia, estado):
    hist = hist or [M.R["saldo_inicial"]]
    with open("datos_mesa/equity_%s.csv" % dia, "w") as f:
        f.write("tick,equity\n" + "\n".join(
            "%d,%.2f" % (i, x) for i, x in enumerate(hist)))
    diag = ["", "DIAGNOSTICO", json.dumps(dict(ST)),
            "websocket: " + str(estado.get("ws_error", "sin errores")),
            "rugcheck claves: " + json.dumps(MUESTRA.get("claves")),
            "rugcheck riesgos vistos: " + json.dumps(MUESTRA.get("riesgos")),
            "rugcheck holder0: " + json.dumps(MUESTRA.get("holder0"))]
    out = "\n".join([M.resumen(c, log, hist)] + seguimiento(log) + diag)
    open("datos_mesa/resumen_%s.md" % dia, "w", encoding="utf-8").write(out)
    log.f.flush()
    print(out, flush=True)


if __name__ == "__main__":
    correr_real(float(sys.argv[1]) if len(sys.argv) > 1 else 10)
