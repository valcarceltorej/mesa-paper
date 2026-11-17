EJECUCION 20261116_2243

RESUMEN
Equity final: 976.81 (-2.3%)
Max drawdown: -2.3%
Pares vistos: 8062, pasan filtros: 9
Operaciones cerradas: 2, ganadoras: 0
Ganancia media: +0.0%, perdida media: -14.6%
Motivos de descarte:
   6868  volumen 1h < 50k$
   1110  sin par en DexScreener
     49  top 10 holders > 20%
     47  riesgo critico segun RugCheck
     33  mint no revocado
     33  freeze authority activo
     32  red de insiders detectada
      9  sin datos de seguridad (no se opera)
      7  dev vinculado a rugs
      2  LP no bloqueado
      1  ya operado (no promediar a la baja)
      1  score 0.42 < 0.60
      1  score 0.32 < 0.60
      1  score 0.22 < 0.60
      1  score 0.44 < 0.60
      1  score 0.45 < 0.60
      1  score 0.35 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               3503
  evaluaciones con precio:     6952
  con volumen >= 50k$:         84
  pasan filtros de seguridad:  9
  aprobados por el Analyst:    3
  compras simuladas:           2

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 31  media    -0%  mediana    +0%  descartado: mint no revocado  (a 60 min)
  n= 18  media    -7%  mediana    -2%  descartado: mint no revocado  (a 180 min)
  n= 12  media   -21%  mediana    -5%  descartado: red de insiders detectada  (a 60 min)
  n= 12  media   -37%  mediana   -65%  descartado: top 10 holders > 20%  (a 60 min)
  n=  8  media    -0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  5  media    +0%  mediana    +0%  descartado: sin datos de seguridad (no se opera)  (a 180 min)
  n=  4  media   -24%  mediana    -4%  descartado: red de insiders detectada  (a 180 min)
  n=  3  media   -20%  mediana   -13%  descartado: score bajo  (a 60 min)
  n=  2  media   -95%  mediana   -95%  operado  (a 60 min)
  n=  2  media    +1%  mediana    +1%  descartado: LP no bloqueado  (a 60 min)
  n=  2  media    +2%  mediana    +2%  descartado: LP no bloqueado  (a 180 min)
  n=  2  media    -5%  mediana    -5%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  2  media   +89%  mediana   +89%  descartado: score bajo  (a 180 min)
  n=  1  media    -0%  mediana    -0%  rechazado por Executor  (a 60 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 3503, "evaluaciones": 6952, "con_volumen": 84, "rugcheck_llamadas": 84, "sin_par": 1110, "ws_reconexiones": 2}
known muestra: [["13yWm3tAcgvJjZ4m7ViT4FKyu39ktsQM3tx6LL9XXc5g", {"name": "Meteora DLMM Pool", "type": "AMM"}], ["26LTgFWktSPzpfDentgukehwWi9e8992ErhZz86iSp1r", {"name": "Printr Stake Pool", "type": "LOCKER"}], ["2Hcycxt9BefSS4PsJoQCwyaxstrPQTbmiJg6BwJLdJk5", {"name": "Orca AMM", "type": "AMM"}]]
websocket: server rejected WebSocket connection: HTTP 502
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Mint Authority still enabled": "danger", "Freeze Authority still enabled": "danger", "Top 10 holders high ownership": "danger", "Single holder ownership": "warn", "High ownership": "danger", "Mutable metadata": "warn", "Low Liquidity": "warn", "Permanent Control Enabled": "danger", "Creator history of rugged tokens": "danger", "High holder concentration": "warn"}
rugcheck holder0: {"address": "2pWK2bHBah35yPDQdndtwTXry1JtR8LKF59tQrqgaU6s", "amount": 750000000000000000, "decimals": 9, "pct": 75.00011512004528, "uiAmount": 750000000, "uiAmountString": "750000000", "owner": "GySFHFS5ZiN4Z5YnyPZcjjxpYcGvD7qHZYVjE9QzMHVH", "insider": false}