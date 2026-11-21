EJECUCION 20261120_2243

RESUMEN
Equity final: 974.65 (-2.5%)
Max drawdown: -2.5%
Pares vistos: 4399, pasan filtros: 5
Operaciones cerradas: 2, ganadoras: 0
Ganancia media: +0.0%, perdida media: -15.9%
Motivos de descarte:
   3927  volumen 1h < 50k$
    334  sin par en DexScreener
    114  riesgo critico segun RugCheck
    110  red de insiders detectada
    100  top 10 holders > 20%
     91  mint no revocado
     13  sin datos de seguridad (no se opera)
      3  LP no bloqueado
      3  freeze authority activo
      2  dev vinculado a rugs
      1  score 0.43 < 0.60
      1  score 0.49 < 0.60
      1  score 0.58 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               2011
  evaluaciones con precio:     4065
  con volumen >= 50k$:         139
  pasan filtros de seguridad:  5
  aprobados por el Analyst:    2
  compras simuladas:           2

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 67  media    -2%  mediana    -1%  descartado: mint no revocado  (a 60 min)
  n= 25  media    -4%  mediana    -4%  descartado: mint no revocado  (a 180 min)
  n= 11  media    +0%  mediana    +0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  8  media   -25%  mediana    -0%  descartado: red de insiders detectada  (a 60 min)
  n=  8  media   -40%  mediana   -52%  descartado: top 10 holders > 20%  (a 60 min)
  n=  7  media    +0%  mediana    +0%  descartado: sin datos de seguridad (no se opera)  (a 180 min)
  n=  5  media   -21%  mediana    -1%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  3  media   -33%  mediana    -2%  descartado: red de insiders detectada  (a 180 min)
  n=  2  media   -98%  mediana   -98%  operado  (a 60 min)
  n=  2  media    +5%  mediana    +5%  descartado: score bajo  (a 60 min)
  n=  2  media   -40%  mediana   -40%  descartado: riesgo critico segun RugCheck  (a 180 min)
  n=  2  media   -66%  mediana   -66%  descartado: top 10 holders > 20%  (a 180 min)
  n=  1  media   -24%  mediana   -24%  descartado: volumen 1h < 50k$  (a 60 min)
  n=  1  media   -72%  mediana   -72%  descartado: dev vinculado a rugs  (a 60 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 2011, "ws_reconexiones": 2, "evaluaciones": 4065, "con_volumen": 139, "rugcheck_llamadas": 139, "sin_par": 334}
known muestra: [["2wmVCSfPxGPjrnMMn7rchp4uaeoTqN39mXFC2zhPdri9", {"name": "Creator", "type": "CREATOR"}]]
websocket: no close frame received or sent
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Mint Authority still enabled": "danger", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger", "Large Amount of LP Unlocked": "danger", "Low Liquidity": "danger", "Mutable metadata": "warn", "Single holder ownership": "warn", "High holder concentration": "warn", "Creator history of rugged tokens": "danger", "Copycat token": "warn"}
rugcheck holder0: null