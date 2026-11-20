EJECUCION 20261119_2245

RESUMEN
Equity final: 899.05 (-10.1%)
Max drawdown: -12.2%
Pares vistos: 5442, pasan filtros: 9
Operaciones cerradas: 3, ganadoras: 0
Ganancia media: +0.0%, perdida media: -42.9%
Motivos de descarte:
   5041  volumen 1h < 50k$
    354  sin par en DexScreener
     26  riesgo critico segun RugCheck
     22  red de insiders detectada
     19  top 10 holders > 20%
     12  mint no revocado
     12  freeze authority activo
     11  LP no bloqueado
      3  sin datos de seguridad (no se opera)
      1  score 0.49 < 0.60
      1  score 0.46 < 0.60
      1  score 0.54 < 0.60
      1  score 0.41 < 0.60
      1  score 0.45 < 0.60
      1  score 0.22 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               2225
  evaluaciones con precio:     5088
  con volumen >= 50k$:         47
  pasan filtros de seguridad:  9
  aprobados por el Analyst:    3
  compras simuladas:           3

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 10  media    -0%  mediana    -1%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  9  media    -0%  mediana    -0%  descartado: mint no revocado  (a 60 min)
  n=  7  media    -8%  mediana    +1%  descartado: top 10 holders > 20%  (a 60 min)
  n=  6  media   +15%  mediana   +10%  descartado: score bajo  (a 60 min)
  n=  5  media   -34%  mediana   -17%  descartado: red de insiders detectada  (a 60 min)
  n=  5  media    -4%  mediana    -3%  descartado: riesgo critico segun RugCheck  (a 180 min)
  n=  4  media   -46%  mediana   -55%  descartado: score bajo  (a 180 min)
  n=  4  media    -0%  mediana    -0%  descartado: mint no revocado  (a 180 min)
  n=  3  media    +0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  3  media   -52%  mediana   -51%  descartado: top 10 holders > 20%  (a 180 min)
  n=  3  media   -98%  mediana   -98%  descartado: red de insiders detectada  (a 180 min)
  n=  2  media   -98%  mediana   -98%  operado  (a 60 min)
  n=  2  media    -0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 180 min)
  n=  2  media   -98%  mediana   -98%  operado  (a 180 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 2225, "evaluaciones": 5088, "con_volumen": 47, "rugcheck_llamadas": 47, "sin_par": 354, "ws_reconexiones": 195}
known muestra: [["2wmVCSfPxGPjrnMMn7rchp4uaeoTqN39mXFC2zhPdri9", {"name": "Creator", "type": "CREATOR"}]]
websocket: [Errno 111] Connect call failed ('216.155.134.164', 443)
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Low Liquidity": "danger", "Mint Authority still enabled": "danger", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger", "Large Amount of LP Unlocked": "danger", "Mutable metadata": "warn", "Copycat token": "warn", "Single holder ownership": "warn", "High holder concentration": "warn", "High market cap per holder": "warn", "Top 10 holders high ownership": "danger"}
rugcheck holder0: null