EJECUCION 20261110_1751

RESUMEN
Equity final: 944.60 (-5.5%)
Max drawdown: -5.5%
Pares vistos: 8287, pasan filtros: 27
Operaciones cerradas: 4, ganadoras: 0
Ganancia media: +0.0%, perdida media: -17.6%
Motivos de descarte:
   5411  volumen 1h < 50k$
   2694  sin par en DexScreener
    103  red de insiders detectada
     76  riesgo critico segun RugCheck
     57  top 10 holders > 20%
     27  sin datos de seguridad (no se opera)
     14  mint no revocado
      9  dev vinculado a rugs
      8  freeze authority activo
      4  LP no bloqueado
      3  score 0.48 < 0.60
      2  score 0.56 < 0.60
      2  score 0.50 < 0.60
      2  score 0.57 < 0.60
      2  score 0.49 < 0.60
      2  score 0.55 < 0.60
      2  score 0.12 < 0.60
      1  score 0.53 < 0.60
      1  score 0.10 < 0.60
      1  score 0.33 < 0.60
      1  score 0.36 < 0.60
      1  score 0.51 < 0.60
      1  score 0.20 < 0.60
      1  score 0.58 < 0.60
      1  score 0.11 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               3830
  evaluaciones con precio:     5593
  con volumen >= 50k$:         183
  pasan filtros de seguridad:  27
  aprobados por el Analyst:    4
  compras simuladas:           4

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 41  media   -10%  mediana    -1%  descartado: red de insiders detectada  (a 60 min)
  n= 28  media    -5%  mediana    +0%  descartado: top 10 holders > 20%  (a 60 min)
  n= 20  media    +0%  mediana    +0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n= 19  media   +24%  mediana   -18%  descartado: score bajo  (a 60 min)
  n= 18  media    -6%  mediana    -0%  descartado: red de insiders detectada  (a 180 min)
  n= 12  media   -10%  mediana    +1%  descartado: top 10 holders > 20%  (a 180 min)
  n= 11  media    -4%  mediana    -0%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n= 11  media    +0%  mediana    -0%  descartado: mint no revocado  (a 60 min)
  n=  9  media    +0%  mediana    +0%  descartado: sin datos de seguridad (no se opera)  (a 180 min)
  n=  8  media    -7%  mediana    -1%  descartado: riesgo critico segun RugCheck  (a 180 min)
  n=  6  media   -59%  mediana   -79%  descartado: score bajo  (a 180 min)
  n=  5  media   -39%  mediana    -3%  descartado: dev vinculado a rugs  (a 60 min)
  n=  2  media   -97%  mediana   -97%  operado  (a 60 min)
  n=  2  media    -1%  mediana    -1%  descartado: LP no bloqueado  (a 60 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 3830, "evaluaciones": 5593, "con_volumen": 183, "rugcheck_llamadas": 183, "sin_par": 2694, "ws_reconexiones": 2}
known muestra: [["31twpfPDSttWhQi1ML85GdCrMuKRKr24Z5ZpWHVVKnAe", {"name": "Pump Fun AMM", "type": "AMM"}], ["37K8K4Bg3RTQPTbRoLazg6UPKGMT3RSQZmXLuxzGmfGM", {"name": "Meteora DAMM v2 Pool", "type": "AMM"}], ["3n987xK6rs17qAJnB3z68AAjz99iAW8i7WPU4G2onDEk", {"name": "Pump Fun AMM", "type": "AMM"}]]
websocket: server rejected WebSocket connection: HTTP 502
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Low Liquidity": "danger", "Copycat token": "warn", "Creator history of rugged tokens": "danger", "Mint Authority still enabled": "danger", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger", "High holder concentration": "warn", "Mutable metadata": "warn", "Large Amount of LP Unlocked": "danger", "Top 10 holders high ownership": "danger", "Single holder ownership": "warn", "Fee config enabled": "warn"}
rugcheck holder0: {"address": "ECUMNDQqztQvi1asYvQGi1rWtFWeoivZa9PdPxpjvhNB", "amount": 939546005206640, "decimals": 6, "pct": 97.53989660958091, "uiAmount": 939546005.20664, "uiAmountString": "939546005.20664", "owner": "31twpfPDSttWhQi1ML85GdCrMuKRKr24Z5ZpWHVVKnAe", "insider": false}