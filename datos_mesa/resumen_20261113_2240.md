EJECUCION 20261113_2240

RESUMEN
Equity final: 998.00 (-0.2%)
Max drawdown: -3.2%
Pares vistos: 4697, pasan filtros: 7
Operaciones cerradas: 2, ganadoras: 1
Ganancia media: +7.9%, perdida media: -10.4%
Motivos de descarte:
   4129  volumen 1h < 50k$
    512  sin par en DexScreener
     30  riesgo critico segun RugCheck
     26  red de insiders detectada
     12  top 10 holders > 20%
      5  sin datos de seguridad (no se opera)
      3  dev vinculado a rugs
      1  score 0.38 < 0.60
      1  score 0.15 < 0.60
      1  score 0.25 < 0.60
      1  score 0.11 < 0.60
      1  score 0.20 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               1994
  evaluaciones con precio:     4185
  con volumen >= 50k$:         56
  pasan filtros de seguridad:  7
  aprobados por el Analyst:    2
  compras simuladas:           2

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 16  media    -4%  mediana    -1%  descartado: red de insiders detectada  (a 60 min)
  n= 10  media   -27%  mediana   -29%  descartado: top 10 holders > 20%  (a 60 min)
  n= 10  media   -21%  mediana    -5%  descartado: red de insiders detectada  (a 180 min)
  n=  6  media   -10%  mediana   -12%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  6  media   -65%  mediana   -70%  descartado: top 10 holders > 20%  (a 180 min)
  n=  4  media    -0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  3  media   -49%  mediana   -77%  descartado: score bajo  (a 60 min)
  n=  3  media   -11%  mediana   -11%  descartado: riesgo critico segun RugCheck  (a 180 min)
  n=  2  media    -0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 180 min)
  n=  1  media   -98%  mediana   -98%  operado  (a 60 min)
  n=  1  media   -98%  mediana   -98%  operado  (a 180 min)
  n=  1  media   -22%  mediana   -22%  descartado: dev vinculado a rugs  (a 60 min)
  n=  1  media   -91%  mediana   -91%  descartado: score bajo  (a 180 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 1994, "evaluaciones": 4185, "con_volumen": 56, "rugcheck_llamadas": 56, "sin_par": 512, "ws_reconexiones": 2}
known muestra: [["5NUh2qVr4qcA7vGfghBTaubsyAFwyzbx15UxBjazJQqR", {"name": "Pump Fun", "type": "AMM"}], ["76the3QCMQwfX7dMwRSY8vFah1K21BMKUGsCT7ep6uYN", {"name": "Creator", "type": "CREATOR"}], ["8yLrhsuJBFNQrmDiV2o2SfCBG1QfPv475Cmo9U5W9ArA", {"name": "Meteora DAMM v2 Pool", "type": "AMM"}]]
websocket: server rejected WebSocket connection: HTTP 502
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Low Liquidity": "danger", "High holder correlation": "warn", "Copycat token": "warn", "Creator history of rugged tokens": "danger"}
rugcheck holder0: {"address": "34pMdQMYvW9Taot4kfy1M3wCKhWMUmxwaPQXERkHjX2D", "amount": 982556154397359, "decimals": 6, "pct": 98.25612799912994, "uiAmount": 982556154.397359, "uiAmountString": "982556154.397359", "owner": "5NUh2qVr4qcA7vGfghBTaubsyAFwyzbx15UxBjazJQqR", "insider": false}