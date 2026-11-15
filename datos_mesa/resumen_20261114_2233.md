EJECUCION 20261114_2233

RESUMEN
Equity final: 976.11 (-2.4%)
Max drawdown: -2.4%
Pares vistos: 4467, pasan filtros: 5
Operaciones cerradas: 1, ganadoras: 0
Ganancia media: +0.0%, perdida media: -29.9%
Motivos de descarte:
   4208  volumen 1h < 50k$
    143  sin par en DexScreener
    101  red de insiders detectada
     91  top 10 holders > 20%
     71  riesgo critico segun RugCheck
     54  mint no revocado
     42  freeze authority activo
      5  dev vinculado a rugs
      3  LP no bloqueado
      3  sin datos de seguridad (no se opera)
      1  score 0.55 < 0.60
      1  score 0.59 < 0.60
      1  score 0.48 < 0.60
      1  score 0.22 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               1904
  evaluaciones con precio:     4324
  con volumen >= 50k$:         116
  pasan filtros de seguridad:  5
  aprobados por el Analyst:    1
  compras simuladas:           1

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 52  media    -1%  mediana    +0%  descartado: mint no revocado  (a 60 min)
  n= 30  media    -3%  mediana    +1%  descartado: mint no revocado  (a 180 min)
  n= 29  media +52658%  mediana    -0%  descartado: top 10 holders > 20%  (a 60 min)
  n= 14  media +71364%  mediana    +3%  descartado: top 10 holders > 20%  (a 180 min)
  n=  9  media   -12%  mediana   -13%  descartado: red de insiders detectada  (a 60 min)
  n=  5  media   +72%  mediana    -2%  descartado: red de insiders detectada  (a 180 min)
  n=  3  media   -20%  mediana    +0%  descartado: dev vinculado a rugs  (a 60 min)
  n=  3  media   +10%  mediana    -3%  descartado: score bajo  (a 60 min)
  n=  2  media    -1%  mediana    -1%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  2  media    -0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  2  media    +2%  mediana    +2%  descartado: dev vinculado a rugs  (a 180 min)
  n=  2  media    -5%  mediana    -5%  descartado: riesgo critico segun RugCheck  (a 180 min)
  n=  2  media   +21%  mediana   +21%  descartado: score bajo  (a 180 min)
  n=  1  media   -99%  mediana   -99%  operado  (a 60 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 1904, "evaluaciones": 4324, "con_volumen": 116, "rugcheck_llamadas": 116, "sin_par": 143, "ws_reconexiones": 1}
known muestra: [["2apszvsMyyJxjYkwb2xQYv8dEgxFr46U5CSAMYikHSGS", {"name": "Creator", "type": "CREATOR"}], ["5jc9JTRne3fstVEWugdi8JJXZt9UpvSvgPdJ2LgcoWp4", {"name": "Meteora DAMM v2 Pool", "type": "AMM"}], ["5pSQ38HW1HFsbkKpYwcFjqQVSkK5EahEfE4QTWNTDRRA", {"name": "Meteora DAMM v2 Pool", "type": "AMM"}]]
websocket: no close frame received or sent
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Creator history of rugged tokens": "danger", "Low Liquidity": "danger", "Copycat token": "warn", "Mint Authority still enabled": "danger", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger", "Large Amount of LP Unlocked": "danger", "Top 10 holders high ownership": "danger", "Single holder ownership": "danger", "High ownership": "danger", "Mutable metadata": "warn", "High holder concentration": "warn", "Missing file metadata": "warn"}
rugcheck holder0: {"address": "ANpE58f41CKgZuY2rz32QtvuV2LQAurFh3B9KgViPhHR", "amount": 997482291674904, "decimals": 6, "pct": 99.7482291674904, "uiAmount": 997482291.674904, "uiAmountString": "997482291.674904", "owner": "7Drspj54kHV7ty88KtXcf99zB3Qi85g2k7ffHRtTC3S9", "insider": false}