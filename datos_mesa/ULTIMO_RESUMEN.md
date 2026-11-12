EJECUCION 20261111_2246

RESUMEN
Equity final: 1002.92 (+0.3%)
Max drawdown: -0.3%
Pares vistos: 5478, pasan filtros: 7
Operaciones cerradas: 0, ganadoras: 0
Ganancia media: +0.0%, perdida media: +0.0%
Motivos de descarte:
   4084  volumen 1h < 50k$
   1310  sin par en DexScreener
     48  riesgo critico segun RugCheck
     46  top 10 holders > 20%
     42  red de insiders detectada
     28  mint no revocado
     28  freeze authority activo
     13  LP no bloqueado
      6  sin datos de seguridad (no se opera)
      3  dev vinculado a rugs
      1  score 0.57 < 0.60
      1  score 0.50 < 0.60
      1  score 0.34 < 0.60
      1  score 0.21 < 0.60
      1  score 0.48 < 0.60
      1  score 0.24 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               2476
  evaluaciones con precio:     4168
  con volumen >= 50k$:         85
  pasan filtros de seguridad:  7
  aprobados por el Analyst:    1
  compras simuladas:           1

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 27  media    -0%  mediana    -0%  descartado: mint no revocado  (a 60 min)
  n= 18  media    +1%  mediana    +1%  descartado: mint no revocado  (a 180 min)
  n= 17  media   -14%  mediana    -1%  descartado: top 10 holders > 20%  (a 60 min)
  n= 12  media   -34%  mediana    -2%  descartado: red de insiders detectada  (a 60 min)
  n=  6  media    -0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  6  media   -23%  mediana    -0%  descartado: top 10 holders > 20%  (a 180 min)
  n=  5  media   -29%  mediana   -98%  descartado: score bajo  (a 60 min)
  n=  4  media   -17%  mediana   -15%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  4  media    -2%  mediana    -2%  descartado: sin datos de seguridad (no se opera)  (a 180 min)
  n=  2  media   -37%  mediana   -37%  descartado: red de insiders detectada  (a 180 min)
  n=  1  media   -99%  mediana   -99%  descartado: score bajo  (a 180 min)
  n=  1  media   -10%  mediana   -10%  descartado: volumen 1h < 50k$  (a 60 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 2476, "evaluaciones": 4168, "con_volumen": 85, "rugcheck_llamadas": 85, "sin_par": 1310}
known muestra: [["2JkKw47A3JSdg6DAwQBFeMRTi65PDQYQBTCvJprJRT6R", {"name": "Orca AMM", "type": "AMM"}], ["2hfyA1G4AyqMqEJNLzWtgFQ4ytCorTDEaTbVcRXk3rN2", {"name": "Orca AMM", "type": "AMM"}], ["2s8broQDGrnCrxFgBsbBRgaDhWsyWKFcmjdfX4wSijC2", {"name": "Meteora DLMM Pool", "type": "AMM"}]]
websocket: sin errores
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Mint Authority still enabled": "danger", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger", "Top 10 holders high ownership": "danger", "Single holder ownership": "warn", "Mutable metadata": "warn", "Large Amount of LP Unlocked": "danger", "Low Liquidity": "danger", "High holder concentration": "warn", "High holder correlation": "warn", "Copycat token": "warn", "Creator history of rugged tokens": "danger"}
rugcheck holder0: {"address": "BGLx2hbcLHk5ajMeLB2SP2zw5ZHqYTCazNJEB9uGcz3q", "amount": 3619544548519, "decimals": 8, "pct": 22.565355115476958, "uiAmount": 36195.44548519, "uiAmountString": "36195.44548519", "owner": "S7vYFFWH6BjJyEsdrPQpqpYTqLTrPRK6KW3VwsJuRaS", "insider": false}