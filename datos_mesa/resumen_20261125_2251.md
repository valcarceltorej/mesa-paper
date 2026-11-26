EJECUCION 20261125_2251

RESUMEN
Equity final: 997.03 (-0.3%)
Max drawdown: -1.8%
Pares vistos: 4162, pasan filtros: 15
Operaciones cerradas: 1, ganadoras: 0
Ganancia media: +0.0%, perdida media: -3.7%
Motivos de descarte:
   3695  volumen 1h < 50k$
    385  sin par en DexScreener
     53  red de insiders detectada
     45  top 10 holders > 20%
     45  riesgo critico segun RugCheck
      5  mint no revocado
      2  score 0.33 < 0.60
      2  score 0.16 < 0.60
      2  score 0.24 < 0.60
      2  dev vinculado a rugs
      2  score 0.48 < 0.60
      2  sin datos de seguridad (no se opera)
      1  LP no bloqueado
      1  score 0.41 < 0.60
      1  score 0.26 < 0.60
      1  score 0.49 < 0.60
      1  score 0.36 < 0.60
      1  score 0.47 < 0.60
      1  score 0.44 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               1819
  evaluaciones con precio:     3777
  con volumen >= 50k$:         82
  pasan filtros de seguridad:  15
  aprobados por el Analyst:    1
  compras simuladas:           1

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 28  media   -12%  mediana    -2%  descartado: top 10 holders > 20%  (a 60 min)
  n= 12  media   -45%  mediana   -39%  descartado: score bajo  (a 60 min)
  n= 10  media   -14%  mediana    -5%  descartado: red de insiders detectada  (a 60 min)
  n= 10  media   -21%  mediana   -11%  descartado: top 10 holders > 20%  (a 180 min)
  n=  5  media   -45%  mediana   -35%  descartado: score bajo  (a 180 min)
  n=  3  media    -0%  mediana    -1%  descartado: mint no revocado  (a 60 min)
  n=  3  media   -14%  mediana   -14%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  2  media   -41%  mediana   -41%  descartado: dev vinculado a rugs  (a 60 min)
  n=  2  media    -8%  mediana    -8%  descartado: red de insiders detectada  (a 180 min)
  n=  2  media    +0%  mediana    +0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  1  media    -0%  mediana    -0%  descartado: LP no bloqueado  (a 60 min)
  n=  1  media   -83%  mediana   -83%  operado  (a 60 min)
  n=  1  media    -1%  mediana    -1%  descartado: LP no bloqueado  (a 180 min)
  n=  1  media    +1%  mediana    +1%  descartado: mint no revocado  (a 180 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 1819, "evaluaciones": 3777, "con_volumen": 82, "rugcheck_llamadas": 82, "sin_par": 385, "ws_reconexiones": 1}
known muestra: [["CJvQhBKyYvEesTEj9G16arxQeLCYJRCBTiUCbFaETmnF", {"name": "Pump Fun", "type": "AMM"}], ["CTYSrpStTUEAHYnkLTNoYVebCDPbhwK1WZnmfpaNJdFR", {"name": "Pump Fun", "type": "AMM"}], ["DPHumkpNmepgDbvN492bjnUDTrQ2fYb9bAo54UNCKZ6i", {"name": "Creator", "type": "CREATOR"}]]
websocket: no close frame received or sent
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Mint Authority still enabled": "danger", "Mutable metadata": "warn", "Low Liquidity": "danger", "Creator history of rugged tokens": "danger", "Copycat token": "warn"}
rugcheck holder0: {"address": "AG3TQnDy1popaqaBRygdVNZysYgetgUApEmvyP5keyHh", "amount": 596867806401095, "decimals": 6, "pct": 59.686780640109504, "uiAmount": 596867806.401095, "uiAmountString": "596867806.401095", "owner": "CTYSrpStTUEAHYnkLTNoYVebCDPbhwK1WZnmfpaNJdFR", "insider": false}