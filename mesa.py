"""Mesa de memecoins de Solana - SOLO PAPER (simulacion, sin dinero real).
Agentes: Scout -> Filter -> Analyst -> Executor <- Risk, y Logger registra todo.
Uso: python mesa.py [ticks] [semilla]
"""
import json
import random
import sys
from collections import Counter
from dataclasses import dataclass

R = {
    "saldo_inicial": 1000.0,
    "max_posicion": 0.08,    # maximo 8 % del saldo actual por operacion
    "stop": -0.06,           # stop fijo
    "trailing_on": 0.12,     # el trailing solo se activa desde +12 %
    "trailing_dist": 0.06,   # distancia del trailing (supuesto, ajustable)
    "score_min": 0.60,
    "vol_min": 50_000,
    "top10_max": 0.20,
    "enfriamiento": 20,      # ticks sin abrir tras un stop (sin venganza)
    "max_abiertas": 5,       # anadido: limita la exposicion total
    "freno_dd": -0.10,       # anadido: sin nuevas entradas si cae 10 % desde maximo
    "comision": 0.01,
    "slippage": 0.015,
}


@dataclass
class Par:
    mint: str
    origen: str
    precio: float
    vol_1h: float
    top10: float
    mint_revocado: bool
    lp_bloqueado: bool
    dev_en_rugs: bool
    mom: float


@dataclass
class Veredicto:
    par: Par
    ok: bool
    motivos: list


@dataclass
class Senal:
    veredicto: Veredicto
    score: float
    motivo: str


@dataclass
class Posicion:
    mint: str
    entrada: float
    unidades: float
    coste: float
    maximo: float
    trailing: bool = False


class Logger:
    def __init__(self, ruta="registro.jsonl"):
        self.f = open(ruta, "w", encoding="utf-8")
        self.eventos = []
        self.descartes = Counter()
        self.actividad = {}
        self.cuenta = Counter()

    def log(self, t, agente, tipo, **datos):
        ev = {"tick": t, "agente": agente, "tipo": tipo, **datos}
        self.eventos.append(ev)
        self.f.write(json.dumps(ev, ensure_ascii=False) + "\n")
        self.actividad[agente] = tipo + " " + str(datos.get("mint", ""))
        self.cuenta[agente] += 1
        if tipo in ("descarte", "rechazo"):
            for m in datos["motivos"]:
                self.descartes[m] += 1


class ScoutSim:
    """Genera pares y precios inventados. Sustituir por PumpFun/Raydium reales."""

    def __init__(self, rng):
        self.rng, self.n, self.px, self.tipo = rng, 0, {}, {}

    def avanzar(self):
        r = self.rng
        for m, p in list(self.px.items()):
            t = self.tipo[m]
            if t == "rug":
                f = r.uniform(0.05, 0.3) if r.random() < 0.04 else 1 + r.gauss(0.01, 0.04)
            elif t == "muerto":
                f = 1 + r.gauss(-0.012, 0.03)
            elif t == "luna":
                f = 1 + r.gauss(0.03, 0.06)
            else:
                f = 1 + r.gauss(0.0, 0.04)
            self.px[m] = max(p * f, 1e-6)

    def nuevos(self, t):
        r = self.rng
        if r.random() > 0.6:
            return []
        self.n += 1
        m = "SIM%04d" % self.n
        tipo = r.choices(["rug", "muerto", "normal", "luna"], [0.35, 0.35, 0.25, 0.05])[0]
        rug = tipo == "rug"
        self.px[m], self.tipo[m] = 1.0, tipo
        return [Par(
            m, r.choice(["pumpfun", "raydium"]), 1.0,
            vol_1h=r.lognormvariate(10.8, 0.9),
            top10=r.uniform(0.15, 0.6) if rug else r.uniform(0.08, 0.35),
            mint_revocado=r.random() < (0.5 if rug else 0.85),
            lp_bloqueado=r.random() < (0.35 if rug else 0.75),
            dev_en_rugs=r.random() < (0.3 if rug else 0.05),
            mom=r.gauss(0.05 if tipo == "luna" else 0.0, 0.05))]


class Filter:
    def revisar(self, p):
        m = []
        if not p.mint_revocado:
            m.append("mint no revocado")
        if not p.lp_bloqueado:
            m.append("LP no bloqueado")
        if p.top10 > R["top10_max"]:
            m.append("top 10 holders > 20%")
        if p.vol_1h < R["vol_min"]:
            m.append("volumen 1h < 50k$")
        if p.dev_en_rugs:
            m.append("dev vinculado a rugs")
        return Veredicto(p, not m, m)


class Analyst:
    def puntuar(self, v):
        if not v.ok:
            raise ValueError("Analyst: solo puntua supervivientes del Filter")
        p = v.par
        liq = min(p.vol_1h / 500_000, 1.0)
        dist = max(0.0, 1 - p.top10 / R["top10_max"])
        mom = min(max((p.mom + 0.1) / 0.3, 0.0), 1.0)
        score = 0.4 * liq + 0.3 * dist + 0.3 * mom
        return Senal(v, round(score, 3),
                     "liq %.2f, reparto %.2f, momentum %.2f" % (liq, dist, mom))


class Cartera:
    def __init__(self):
        self.cash = R["saldo_inicial"]
        self.pos, self.operados, self.cierres = {}, set(), []
        self.enfria_hasta, self.pico, self.parado = 0, R["saldo_inicial"], False

    def equity(self, px):
        return self.cash + sum(p.unidades * px[m] for m, p in self.pos.items())


class Executor:
    """Unico que compra y vende. Solo acepta senales aprobadas."""

    def __init__(self, c):
        self.c = c

    def abrir(self, s, px, t, log):
        if not (s.veredicto.ok and s.score >= R["score_min"]):
            raise PermissionError("Executor: senal sin filtros o con score bajo")
        c, m = self.c, s.veredicto.par.mint
        eq = c.equity(px)
        c.pico = max(c.pico, eq)
        if eq <= c.pico * (1 + R["freno_dd"]):
            c.parado = True
        tam = min(R["max_posicion"] * eq, c.cash)
        razon = None
        if c.parado:
            razon = "freno de capital activo"
        elif t < c.enfria_hasta:
            razon = "enfriamiento tras stop (sin venganza)"
        elif m in c.operados:
            razon = "ya operado (no promediar a la baja)"
        elif len(c.pos) >= R["max_abiertas"]:
            razon = "maximo de posiciones abiertas"
        elif tam < 1.0:
            razon = "saldo insuficiente"
        if razon:
            log.log(t, "Executor", "rechazo", mint=m, motivos=[razon])
            return
        fill = px[m] * (1 + R["slippage"])
        c.cash -= tam
        c.pos[m] = Posicion(m, fill, tam * (1 - R["comision"]) / fill, tam, fill)
        c.operados.add(m)
        log.log(t, "Executor", "compra", mint=m, tam=round(tam, 2),
                eq=round(eq, 2), score=s.score, motivo=s.motivo)

    def cerrar(self, m, motivo, px, t, log):
        c = self.c
        p = c.pos.pop(m)
        sal = p.unidades * px[m] * (1 - R["slippage"]) * (1 - R["comision"])
        c.cash += sal
        c.cierres.append(sal / p.coste - 1)
        if motivo.startswith("stop"):
            c.enfria_hasta = t + R["enfriamiento"]
        log.log(t, "Executor", "venta", mint=m, motivo=motivo,
                ret_precio=round(px[m] / p.entrada - 1, 4),
                pnl=round(sal - p.coste, 2))


class Risk:
    """Solo emite ordenes de cierre. Nunca abre ni promedia."""

    def vigilar(self, c, px, log, t):
        ordenes = []
        for m, p in list(c.pos.items()):
            p.maximo = max(p.maximo, px[m])
            if not p.trailing and p.maximo / p.entrada - 1 >= R["trailing_on"]:
                p.trailing = True
                log.log(t, "Risk", "trailing activado", mint=m)
            if px[m] / p.entrada - 1 <= R["stop"]:
                ordenes.append((m, "stop -6%"))
            elif p.trailing and px[m] <= p.maximo * (1 - R["trailing_dist"]):
                ordenes.append((m, "trailing"))
        for m, mo in ordenes:
            log.log(t, "Risk", "orden de cierre", mint=m, motivo=mo)
        return ordenes


def spark(xs, n=44):
    if len(xs) > n:
        xs = [xs[int(i * len(xs) / n)] for i in range(n)]
    lo, hi = min(xs), max(xs)
    return "".join("▁▂▃▄▅▆▇█"[int((x - lo) / (hi - lo + 1e-9) * 7)] for x in xs)


def panel(t, c, log, hist, px):
    eq = c.equity(px)
    L = ["=" * 60,
         " DATOYBARRO MESA (PAPER)  tick %d  %s" % (t, "FRENO" if c.parado else "activa"),
         "=" * 60,
         " Caja %9.2f   Equity %9.2f   (%+.1f%%)" % (c.cash, eq, 100 * (eq / R["saldo_inicial"] - 1)),
         " Posiciones abiertas: %d   Cerradas: %d" % (len(c.pos), len(c.cierres)),
         " Equity  " + spark(hist),
         "-" * 60]
    for a in ("Scout", "Filter", "Analyst", "Executor", "Risk"):
        L.append(" %-9s %4d  %s" % (a, log.cuenta[a], log.actividad.get(a, "-")))
    L.append("-" * 60)
    return "\n".join(L)


def resumen(c, log, hist):
    g = [x for x in c.cierres if x > 0]
    p = [x for x in c.cierres if x <= 0]
    pico, dd = hist[0], 0.0
    for x in hist:
        pico = max(pico, x)
        dd = min(dd, x / pico - 1)
    vistos = log.cuenta["Scout"]
    pasan = sum(1 for e in log.eventos if e["agente"] == "Filter" and e["tipo"] == "pasa")
    L = ["RESUMEN",
         "Equity final: %.2f (%+.1f%%)" % (hist[-1], 100 * (hist[-1] / R["saldo_inicial"] - 1)),
         "Max drawdown: %.1f%%" % (100 * dd),
         "Pares vistos: %d, pasan filtros: %d" % (vistos, pasan),
         "Operaciones cerradas: %d, ganadoras: %d" % (len(c.cierres), len(g)),
         "Ganancia media: %+.1f%%, perdida media: %+.1f%%" % (
             100 * sum(g) / max(len(g), 1), 100 * sum(p) / max(len(p), 1)),
         "Motivos de descarte:"]
    for m, n in log.descartes.most_common():
        L.append("  %5d  %s" % (n, m))
    return "\n".join(L)


def correr(ticks=300, semilla=7, vivo=False, ruta="registro.jsonl"):
    rng = random.Random(semilla)
    scout, filt, ana = ScoutSim(rng), Filter(), Analyst()
    c, log, risk = Cartera(), Logger(ruta), Risk()
    ex, hist = Executor(c), []
    for t in range(ticks):
        scout.avanzar()
        px = scout.px
        for m, motivo in risk.vigilar(c, px, log, t):
            ex.cerrar(m, motivo, px, t, log)
        for par in scout.nuevos(t):
            log.log(t, "Scout", "nuevo par", mint=par.mint, origen=par.origen)
            v = filt.revisar(par)
            if not v.ok:
                log.log(t, "Filter", "descarte", mint=par.mint, motivos=v.motivos)
                continue
            log.log(t, "Filter", "pasa", mint=par.mint)
            s = ana.puntuar(v)
            if s.score < R["score_min"]:
                log.log(t, "Analyst", "descarte", mint=par.mint, score=s.score,
                        motivos=["score %.2f < 0.60" % s.score])
                continue
            log.log(t, "Analyst", "aprobado", mint=par.mint, score=s.score, motivo=s.motivo)
            ex.abrir(s, px, t, log)
        hist.append(c.equity(px))
        if vivo or t % 100 == 99:
            print(panel(t, c, log, hist, px))
    with open("equity.csv", "w") as f:
        f.write("tick,equity\n" + "\n".join("%d,%.2f" % (i, x) for i, x in enumerate(hist)))
    txt = resumen(c, log, hist)
    open("resumen.txt", "w", encoding="utf-8").write(txt)
    print(txt)
    return c, log, hist


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    s = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    correr(n, s)
