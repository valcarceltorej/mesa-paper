EJECUCION 20261126_2253

RESUMEN
Equity final: 988.42 (-1.2%)
Max drawdown: -3.0%
Pares vistos: 4519, pasan filtros: 3
Operaciones cerradas: 1, ganadoras: 0
Ganancia media: +0.0%, perdida media: -14.5%
Motivos de descarte:
   3605  volumen 1h < 50k$
    862  sin par en DexScreener
     30  red de insiders detectada
     18  riesgo critico segun RugCheck
     13  top 10 holders > 20%
      7  sin datos de seguridad (no se opera)
      4  dev vinculado a rugs
      2  mint no revocado
      1  score 0.40 < 0.60
      1  score 0.46 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               1917
  evaluaciones con precio:     3657
  con volumen >= 50k$:         53
  pasan filtros de seguridad:  3
  aprobados por el Analyst:    1
  compras simuladas:           1

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 17  media   -17%  mediana    -3%  descartado: red de insiders detectada  (a 60 min)
  n=  9  media   -12%  mediana    -3%  descartado: red de insiders detectada  (a 180 min)
  n=  8  media   -68%  mediana   -69%  descartado: top 10 holders > 20%  (a 60 min)
  n=  6  media   -14%  mediana    -5%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  6  media   -76%  mediana   -77%  descartado: top 10 holders > 20%  (a 180 min)
  n=  4  media    +0%  mediana    +0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  3  media   -11%  mediana    -4%  descartado: dev vinculado a rugs  (a 60 min)
  n=  3  media    -7%  mediana    -8%  descartado: riesgo critico segun RugCheck  (a 180 min)
  n=  2  media    +0%  mediana    +0%  descartado: sin datos de seguridad (no se opera)  (a 180 min)
  n=  2  media   -20%  mediana   -20%  descartado: dev vinculado a rugs  (a 180 min)
  n=  1  media    +0%  mediana    +0%  descartado: mint no revocado  (a 60 min)
  n=  1  media    -6%  mediana    -6%  descartado: score bajo  (a 60 min)
  n=  1  media   +35%  mediana   +35%  descartado: volumen 1h < 50k$  (a 60 min)
  n=  1  media   -99%  mediana   -99%  operado  (a 60 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 1917, "evaluaciones": 3657, "con_volumen": 53, "rugcheck_llamadas": 59, "sin_par": 862, "ws_reconexiones": 1, "error_red": 2, "http_400": 2, "http_502": 4}
known muestra: [["5VrDtLBzkwTxEvpCWnivhC3HTS7qhtY4jiTywaVUd5YY", {"name": "Pump Fun", "type": "AMM"}], ["5m6AmGc98687mZLH3gsiqXs2H4QfAB5CDAyXa6NEknte", {"name": "Pump Fun AMM", "type": "AMM"}], ["7yAYzK4npUwVLPQbN8HcvKHcLy7cu9P21C38zWGmvy86", {"name": "Pump Fun", "type": "AMM"}]]
websocket: no close frame received or sent
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Low Liquidity": "warn", "Creator history of rugged tokens": "danger", "Mint Authority still enabled": "danger", "Mutable metadata": "warn", "Copycat token": "warn"}
rugcheck holder0: {"address": "6vEcMEb1BFcqDcBhBhTf5d3UBCMFhs6rEu1YULfpQoD7", "amount": 939833233923073, "decimals": 6, "pct": 98.19888951623724, "uiAmount": 939833233.923073, "uiAmountString": "939833233.923073", "owner": "BvqMth2e32Uc77gpwww14verUqgrd98gGouGPDoyqVCB", "insider": false}