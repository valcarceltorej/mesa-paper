EJECUCION 20261123_2249

RESUMEN
Equity final: 1006.07 (+0.6%)
Max drawdown: -1.5%
Pares vistos: 4822, pasan filtros: 14
Operaciones cerradas: 1, ganadoras: 1
Ganancia media: +7.6%, perdida media: +0.0%
Motivos de descarte:
   4261  volumen 1h < 50k$
    476  sin par en DexScreener
     48  top 10 holders > 20%
     45  red de insiders detectada
     45  riesgo critico segun RugCheck
     32  mint no revocado
      9  freeze authority activo
      8  sin datos de seguridad (no se opera)
      5  dev vinculado a rugs
      2  LP no bloqueado
      2  score 0.47 < 0.60
      1  score 0.45 < 0.60
      1  score 0.20 < 0.60
      1  score 0.34 < 0.60
      1  score 0.16 < 0.60
      1  score 0.19 < 0.60
      1  score 0.46 < 0.60
      1  score 0.27 < 0.60
      1  score 0.44 < 0.60
      1  score 0.40 < 0.60
      1  score 0.38 < 0.60
      1  score 0.28 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               2063
  evaluaciones con precio:     4346
  con volumen >= 50k$:         85
  pasan filtros de seguridad:  14
  aprobados por el Analyst:    1
  compras simuladas:           1

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 27  media    +0%  mediana    +0%  descartado: mint no revocado  (a 60 min)
  n= 17  media    -1%  mediana    -1%  descartado: mint no revocado  (a 180 min)
  n= 16  media   +26%  mediana   -46%  descartado: top 10 holders > 20%  (a 60 min)
  n=  8  media   -38%  mediana   -37%  descartado: score bajo  (a 60 min)
  n=  7  media   +11%  mediana    -4%  descartado: red de insiders detectada  (a 60 min)
  n=  6  media   -43%  mediana   -44%  descartado: score bajo  (a 180 min)
  n=  5  media    -1%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  3  media   -31%  mediana   -46%  descartado: dev vinculado a rugs  (a 60 min)
  n=  3  media   -20%  mediana   -17%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  3  media   -46%  mediana   -46%  descartado: top 10 holders > 20%  (a 180 min)
  n=  3  media    -8%  mediana    -9%  descartado: red de insiders detectada  (a 180 min)
  n=  2  media    -1%  mediana    -1%  descartado: sin datos de seguridad (no se opera)  (a 180 min)
  n=  1  media   -99%  mediana   -99%  operado  (a 60 min)
  n=  1  media   -99%  mediana   -99%  operado  (a 180 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 2063, "evaluaciones": 4346, "con_volumen": 85, "rugcheck_llamadas": 85, "sin_par": 476, "ws_reconexiones": 3}
known muestra: [["524ieQ6nM4GowhxLYDBRCcaGFBvFrpoKYmhoh4LudijF", {"name": "Printr Stake Pool", "type": "LOCKER"}], ["637VV4FHpynMec2StkVrqNrxyBG2bNqHdr54XToQgqGX", {"name": "Pump Fun", "type": "AMM"}], ["7ZgNzhrfqQFLSQTNQtC3CyidJpFXpSt8S1rXWjSxYe2u", {"name": "Creator", "type": "CREATOR"}]]
websocket: no close frame received or sent
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Low Liquidity": "danger", "Mint Authority still enabled": "danger", "Single holder ownership": "danger", "High holder concentration": "warn", "Mutable metadata": "warn", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger", "Large Amount of LP Unlocked": "danger", "Low amount of LP Providers": "warn", "Missing file metadata": "warn", "Creator history of rugged tokens": "danger"}
rugcheck holder0: {"address": "3c5x4EkWu6J2jFeAALx8kaAznEU2RrA67KkLSYmT4zSH", "amount": 408838957793694, "decimals": 6, "pct": 40.88389577980166, "uiAmount": 408838957.793694, "uiAmountString": "408838957.793694", "owner": "637VV4FHpynMec2StkVrqNrxyBG2bNqHdr54XToQgqGX", "insider": false}