"""Mesa PAPER con datos reales (sin dinero real).
Fuentes: PumpPortal (tokens nuevos), DexScreener (precio/volumen), RugCheck.
Uso: python real.py [minutos] [edad_min_segundos]
Con 15 minutos o menos funciona como diagnostico rapido.
"""
import asyncio
import json
import os
import queue
import sys
import threading
import time
from collections import Counter

import requests

import mesa as M

WS = "wss://pumpportal.fun/api/data"
DEX = "https://api.dexscreener.com/latest/dex/tokens/"
RUG = "https://api.rugcheck.xyz/v1/tokens/%s/report"
TICK_S = 10
RUG_POR_TICK = 2
LP_MIN = 90.0
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
        return M.Veredicto(p, not m, m)


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
                    "mom": float((p.get("priceChange") or {}).get("m5") or 0) / 100}
    return out


def seguridad(mint):
    rep = get(RUG % mint)
    if rep is None:
        return None
    tok = rep.get("token") or {}
    if "claves" not in MUESTRA:
        MUESTRA["claves"] = sorted(rep.keys())
        MUESTRA["riesgos"] = [r.get("name") for r in rep.get("risks") or []]
        MUESTRA["holder0"] = (rep.get("topHolders") or [None])[0]

    def autoridad(k):
        v = rep[k] if k in rep else tok.get(k, "?")
        return None if v == "?" else (v is None)

    markets = rep.get("markets") or []
    lock = max(((x.get("lp") or {}).get("lpLockedPct") or 0 for x in markets),
               default=None)
    ths = rep.get("topHolders") or []
    nombres = [(r.get("name") or "").lower() for r in rep.get("risks") or []]
    dev = bool(rep.get("rugged")) or any(
        "creator" in n and "rug" in n for n in nombres)
    return {
        "mint_revocado": autoridad("mintAuthority"),
        "lp_bloqueado": None if lock is None else lock >= LP_MIN,
        "top10": (sum(float(h.get("pct") or 0) for h in ths[:10]) / 100
                  if ths else None),
        "dev_en_rugs": dev}


def correr_real(minutos, edad_s):
    os.makedirs("datos_mesa", exist_ok=True)
    dia = time.strftime("%Y%m%d_%H%M")
    c, risk = M.Cartera(), M.Risk()
    log = M.Logger("datos_mesa/registro_%s.jsonl" % dia)
    ex, filt, ana = M.Executor(c), FilterReal(), M.Analyst()
    cola, estado = queue.Queue(), {}
    threading.Thread(target=escuchar, args=(cola, estado), daemon=True).start()
    espera, segur, px, hist = [], [], {}, []
    fin, t, ult_panel = time.time() + minutos * 60, 0, 0

    def evaluar(par):
        log.log(t, "Scout", "nuevo par", mint=par.mint, origen=par.origen)
        v = filt.revisar(par)
        if not v.ok:
            log.log(t, "Filter", "descarte", mint=par.mint, motivos=v.motivos)
            return
        log.log(t, "Filter", "pasa", mint=par.mint)
        s = ana.puntuar(v)
        if s.score < M.R["score_min"]:
            log.log(t, "Analyst", "descarte", mint=par.mint, score=s.score,
                    motivos=["score %.2f < 0.60" % s.score])
            return
        log.log(t, "Analyst", "aprobado", mint=par.mint, score=s.score,
                motivo=s.motivo)
        ex.abrir(s, px, t, log)

    while time.time() < fin:
        ini = time.time()
        while not cola.empty():
            ev = cola.get()
            espera.append({"t0": time.time(), "mint": ev["mint"], "next": 0})
            ST["tokens_vistos"] += 1
        if c.pos:
            for m, d in precios_dex(list(c.pos)).items():
                if d["precio"] > 0:
                    px[m] = d["precio"]
        for m, motivo in risk.vigilar(c, px, log, t):
            ex.cerrar(m, motivo, px, t, log)
        ahora = time.time()
        listos = [w for w in espera
                  if ahora - w["t0"] >= edad_s and ahora >= w["next"]][:60]
        for w in listos:
            espera.remove(w)
        datos = precios_dex([w["mint"] for w in listos]) if listos else {}
        for w in listos:
            d = datos.get(w["mint"])
            if d is None or d["precio"] <= 0:
                if ahora - w["t0"] < 2700:
                    w["next"] = ahora + 120
                    espera.append(w)
                else:
                    ST["sin_par"] += 1
                    log.log(t, "Scout", "descarte", mint=w["mint"],
                            motivos=["sin par en DexScreener"])
                continue
            ST["con_datos"] += 1
            px[w["mint"]] = d["precio"]
            par = M.Par(w["mint"], "pumpfun", d["precio"], d["vol"],
                        None, None, None, None, d["mom"])
            if d["vol"] >= M.R["vol_min"]:
                segur.append({"par": par, "intentos": 0})
            else:
                evaluar(par)
        for item in segur[:RUG_POR_TICK]:
            segur.remove(item)
            s = seguridad(item["par"].mint)
            ST["rugcheck_llamadas"] += 1
            if s is None and item["intentos"] < 3:
                item["intentos"] += 1
                segur.append(item)
                continue
            if s is not None:
                for k, v in s.items():
                    setattr(item["par"], k, v)
            evaluar(item["par"])
            time.sleep(2.5)
        hist.append(c.equity(px))
        t += 1
        if time.time() - ult_panel > 60:
            ult_panel = time.time()
            print(M.panel(t, c, log, hist, px))
            print(" tokens vistos %d, con datos %d, en espera %d" % (
                ST["tokens_vistos"], ST["con_datos"], len(espera)), flush=True)
            log.f.flush()
        time.sleep(max(0, TICK_S - (time.time() - ini)))
    cierre(c, log, hist, dia, estado)


def cierre(c, log, hist, dia, estado):
    hist = hist or [M.R["saldo_inicial"]]
    with open("datos_mesa/equity_%s.csv" % dia, "w") as f:
        f.write("tick,equity\n" + "\n".join(
            "%d,%.2f" % (i, x) for i, x in enumerate(hist)))
    txt = M.resumen(c, log, hist)
    diag = ["", "DIAGNOSTICO", json.dumps(dict(ST)),
            "websocket: " + str(estado.get("ws_error", "sin errores")),
            "rugcheck claves: " + json.dumps(MUESTRA.get("claves")),
            "rugcheck riesgos: " + json.dumps(MUESTRA.get("riesgos")),
            "rugcheck holder0: " + json.dumps(MUESTRA.get("holder0"))]
    out = txt + "\n" + "\n".join(diag)
    open("datos_mesa/resumen_%s.md" % dia, "w", encoding="utf-8").write(out)
    log.f.flush()
    print(out, flush=True)


if __name__ == "__main__":
    mins = float(sys.argv[1]) if len(sys.argv) > 1 else 10
    edad = float(sys.argv[2]) if len(sys.argv) > 2 else (90 if mins <= 15 else 900)
    correr_real(mins, edad)
