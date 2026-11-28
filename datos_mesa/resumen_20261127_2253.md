EJECUCION 20261127_2253

RESUMEN
Equity final: 973.78 (-2.6%)
Max drawdown: -3.4%
Pares vistos: 4249, pasan filtros: 27
Operaciones cerradas: 3, ganadoras: 0
Ganancia media: +0.0%, perdida media: -11.0%
Motivos de descarte:
   3354  volumen 1h < 50k$
    802  sin par en DexScreener
     41  red de insiders detectada
     31  top 10 holders > 20%
     27  riesgo critico segun RugCheck
      4  mint no revocado
      3  dev vinculado a rugs
      3  sin datos de seguridad (no se opera)
      3  score 0.44 < 0.60
      2  score 0.40 < 0.60
      2  score 0.34 < 0.60
      2  score 0.20 < 0.60
      1  score 0.09 < 0.60
      1  score 0.15 < 0.60
      1  score 0.36 < 0.60
      1  score 0.10 < 0.60
      1  score 0.56 < 0.60
      1  score 0.19 < 0.60
      1  score 0.48 < 0.60
      1  score 0.47 < 0.60
      1  score 0.35 < 0.60
      1  score 0.55 < 0.60
      1  score 0.31 < 0.60
      1  score 0.45 < 0.60
      1  score 0.30 < 0.60
      1  score 0.43 < 0.60
      1  score 0.41 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               1806
  evaluaciones con precio:     3447
  con volumen >= 50k$:         93
  pasan filtros de seguridad:  27
  aprobados por el Analyst:    3
  compras simuladas:           3

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 24  media    -8%  mediana    -1%  descartado: red de insiders detectada  (a 60 min)
  n= 21  media   -10%  mediana   -26%  descartado: top 10 holders > 20%  (a 60 min)
  n= 20  media   -17%  mediana   -20%  descartado: score bajo  (a 60 min)
  n= 14  media    -9%  mediana    -1%  descartado: red de insiders detectada  (a 180 min)
  n= 13  media   +91%  mediana   -37%  descartado: score bajo  (a 180 min)
  n= 12  media   +29%  mediana   -12%  descartado: top 10 holders > 20%  (a 180 min)
  n=  3  media   -48%  mediana   -98%  operado  (a 60 min)
  n=  3  media   +56%  mediana    -1%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  3  media    +1%  mediana    +0%  descartado: mint no revocado  (a 60 min)
  n=  2  media   -32%  mediana   -32%  descartado: dev vinculado a rugs  (a 60 min)
  n=  2  media    +0%  mediana    +0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  2  media   -84%  mediana   -84%  operado  (a 180 min)
  n=  2  media   -32%  mediana   -32%  descartado: dev vinculado a rugs  (a 180 min)
  n=  2  media   +30%  mediana   +30%  descartado: riesgo critico segun RugCheck  (a 180 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 1806, "ws_reconexiones": 5, "evaluaciones": 3447, "con_volumen": 93, "rugcheck_llamadas": 95, "sin_par": 802, "http_400": 1, "error_red": 1}
known muestra: [["6iFCkAQWFUWi2wqTCSmweFr1yiFb6gYMF9diP6Vy1Qoi", {"name": "Pump Fun", "type": "AMM"}], ["AFzqFnTqMZ1JYe2hn4szrJuDSMeMGCdux4KLCkHz3GCV", {"name": "Creator", "type": "CREATOR"}], ["E5tphXESiN7zNVv7iM1JV3V6iWNcUwshsFWvs399k1of", {"name": "Printr Stake Pool", "type": "LOCKER"}]]
websocket: no close frame received or sent
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Low Liquidity": "warn", "Creator history of rugged tokens": "danger", "Mint Authority still enabled": "danger", "Mutable metadata": "warn", "Copycat token": "warn"}
rugcheck holder0: {"address": "qjU1UbeqxJv8rB6WQoH86hU3hX16Vzgj95H6r7sTJX2", "amount": 473659793243382, "decimals": 6, "pct": 47.3659793243382, "uiAmount": 473659793.243382, "uiAmountString": "473659793.243382", "owner": "FjQpf6k75geWfhZfe2ivnB3ygXN97HAxECanxN9WEmWb", "insider": false}