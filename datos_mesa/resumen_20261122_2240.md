EJECUCION 20261122_2240

RESUMEN
Equity final: 957.79 (-4.2%)
Max drawdown: -4.4%
Pares vistos: 4905, pasan filtros: 11
Operaciones cerradas: 4, ganadoras: 0
Ganancia media: +0.0%, perdida media: -13.4%
Motivos de descarte:
   3390  volumen 1h < 50k$
   1431  sin par en DexScreener
     56  red de insiders detectada
     48  riesgo critico segun RugCheck
     42  top 10 holders > 20%
     31  mint no revocado
      8  sin datos de seguridad (no se opera)
      5  dev vinculado a rugs
      2  freeze authority activo
      2  score 0.29 < 0.60
      1  score 0.15 < 0.60
      1  ya operado (no promediar a la baja)
      1  score 0.41 < 0.60
      1  score 0.31 < 0.60
      1  score 0.35 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               2298
  evaluaciones con precio:     3474
  con volumen >= 50k$:         86
  pasan filtros de seguridad:  11
  aprobados por el Analyst:    5
  compras simuladas:           4

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 30  media    +0%  mediana    +0%  descartado: mint no revocado  (a 60 min)
  n= 18  media    -0%  mediana    +0%  descartado: mint no revocado  (a 180 min)
  n= 11  media   -29%  mediana   -17%  descartado: red de insiders detectada  (a 60 min)
  n=  7  media    +0%  mediana    +0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  7  media   -38%  mediana   -43%  descartado: top 10 holders > 20%  (a 60 min)
  n=  7  media   -22%  mediana   -12%  descartado: red de insiders detectada  (a 180 min)
  n=  4  media   -98%  mediana   -99%  operado  (a 60 min)
  n=  3  media   -43%  mediana   -42%  descartado: dev vinculado a rugs  (a 60 min)
  n=  3  media    -0%  mediana    -0%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  2  media    +0%  mediana    +0%  descartado: sin datos de seguridad (no se opera)  (a 180 min)
  n=  2  media   -59%  mediana   -59%  descartado: volumen 1h < 50k$  (a 60 min)
  n=  1  media   -99%  mediana   -99%  operado  (a 180 min)
  n=  1  media   -72%  mediana   -72%  descartado: score bajo  (a 60 min)
  n=  1  media   -76%  mediana   -76%  descartado: dev vinculado a rugs  (a 180 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 2298, "evaluaciones": 3474, "con_volumen": 86, "rugcheck_llamadas": 86, "sin_par": 1431, "ws_reconexiones": 1}
known muestra: [["1qR3JkkG7Sdr19YfoQWiZy9BzuKnApBJaTRaEz6RHGv", {"name": "Meteora DLMM Pool", "type": "AMM"}], ["21QrKaPkrcGhEk9rDzGqjGZ4wXh5TKWPxPioJWP5gCsa", {"name": "Meteora DLMM Pool", "type": "AMM"}], ["28h7R3mNfFENJPmRv2RtTypaaSncW9sCfVgpz1Gh2sVY", {"name": "Meteora DLMM Pool", "type": "AMM"}]]
websocket: no close frame received or sent
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Mint Authority still enabled": "danger", "Single holder ownership": "warn", "High holder concentration": "warn", "Mutable metadata": "warn", "Low Liquidity": "warn", "Creator history of rugged tokens": "danger", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger", "Copycat token": "warn", "High holder correlation": "warn"}
rugcheck holder0: {"address": "BUbXRWQyJa3L1guB4uEsW9VzF3faZBgFmswKS4LKiguZ", "amount": 173410018470399, "decimals": 9, "pct": 21.113965081376655, "uiAmount": 173410.018470399, "uiAmountString": "173410.018470399", "owner": "4yhXa4iERFGma3T1HMMjH8nJ8EdFqbahCV5Yomm8Z3do", "insider": false}