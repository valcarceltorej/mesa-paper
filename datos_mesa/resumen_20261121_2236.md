EJECUCION 20261121_2236

RESUMEN
Equity final: 1000.00 (+0.0%)
Max drawdown: 0.0%
Pares vistos: 4398, pasan filtros: 7
Operaciones cerradas: 0, ganadoras: 0
Ganancia media: +0.0%, perdida media: +0.0%
Motivos de descarte:
   4012  volumen 1h < 50k$
    321  sin par en DexScreener
     56  red de insiders detectada
     50  riesgo critico segun RugCheck
     46  top 10 holders > 20%
     39  mint no revocado
      5  dev vinculado a rugs
      5  freeze authority activo
      2  score 0.47 < 0.60
      1  score 0.41 < 0.60
      1  score 0.28 < 0.60
      1  score 0.27 < 0.60
      1  score 0.26 < 0.60
      1  score 0.36 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               1900
  evaluaciones con precio:     4077
  con volumen >= 50k$:         65
  pasan filtros de seguridad:  7
  aprobados por el Analyst:    0
  compras simuladas:           0

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 39  media    -0%  mediana    -0%  descartado: mint no revocado  (a 60 min)
  n= 19  media    -1%  mediana    -1%  descartado: mint no revocado  (a 180 min)
  n=  7  media   -14%  mediana    -6%  descartado: red de insiders detectada  (a 60 min)
  n=  7  media   -44%  mediana   -11%  descartado: red de insiders detectada  (a 180 min)
  n=  5  media   -28%  mediana    -9%  descartado: score bajo  (a 60 min)
  n=  5  media   -41%  mediana   -43%  descartado: score bajo  (a 180 min)
  n=  3  media   -24%  mediana    -7%  descartado: top 10 holders > 20%  (a 60 min)
  n=  1  media    -0%  mediana    -0%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  1  media   -20%  mediana   -20%  descartado: dev vinculado a rugs  (a 60 min)
  n=  1  media    -2%  mediana    -2%  descartado: riesgo critico segun RugCheck  (a 180 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 1900, "evaluaciones": 4077, "con_volumen": 65, "rugcheck_llamadas": 65, "sin_par": 321, "ws_reconexiones": 1}
known muestra: [["1qR3JkkG7Sdr19YfoQWiZy9BzuKnApBJaTRaEz6RHGv", {"name": "Meteora DLMM Pool", "type": "AMM"}], ["21QrKaPkrcGhEk9rDzGqjGZ4wXh5TKWPxPioJWP5gCsa", {"name": "Meteora DLMM Pool", "type": "AMM"}], ["28h7R3mNfFENJPmRv2RtTypaaSncW9sCfVgpz1Gh2sVY", {"name": "Meteora DLMM Pool", "type": "AMM"}]]
websocket: no close frame received or sent
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Mint Authority still enabled": "danger", "Single holder ownership": "warn", "High holder concentration": "warn", "Mutable metadata": "warn", "Low Liquidity": "danger", "Creator history of rugged tokens": "danger", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger"}
rugcheck holder0: {"address": "BUbXRWQyJa3L1guB4uEsW9VzF3faZBgFmswKS4LKiguZ", "amount": 173410018470399, "decimals": 9, "pct": 20.363385406636382, "uiAmount": 173410.018470399, "uiAmountString": "173410.018470399", "owner": "4yhXa4iERFGma3T1HMMjH8nJ8EdFqbahCV5Yomm8Z3do", "insider": false}