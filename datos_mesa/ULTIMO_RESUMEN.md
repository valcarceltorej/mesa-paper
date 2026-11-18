EJECUCION 20261117_2251

RESUMEN
Equity final: 884.79 (-11.5%)
Max drawdown: -11.5%
Pares vistos: 6201, pasan filtros: 23
Operaciones cerradas: 3, ganadoras: 0
Ganancia media: +0.0%, perdida media: -49.4%
Motivos de descarte:
   5315  volumen 1h < 50k$
    802  sin par en DexScreener
     38  riesgo critico segun RugCheck
     33  red de insiders detectada
     27  top 10 holders > 20%
     16  mint no revocado
     14  freeze authority activo
      9  LP no bloqueado
      6  sin datos de seguridad (no se opera)
      4  dev vinculado a rugs
      3  score 0.40 < 0.60
      2  score 0.46 < 0.60
      2  score 0.32 < 0.60
      2  score 0.18 < 0.60
      2  score 0.47 < 0.60
      1  score 0.27 < 0.60
      1  score 0.45 < 0.60
      1  score 0.17 < 0.60
      1  score 0.41 < 0.60
      1  score 0.14 < 0.60
      1  score 0.44 < 0.60
      1  score 0.33 < 0.60
      1  score 0.43 < 0.60
      1  score 0.34 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               2758
  evaluaciones con precio:     5399
  con volumen >= 50k$:         84
  pasan filtros de seguridad:  23
  aprobados por el Analyst:    3
  compras simuladas:           3

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 18  media   -20%  mediana    -9%  descartado: score bajo  (a 60 min)
  n= 12  media    +4%  mediana    -1%  descartado: red de insiders detectada  (a 60 min)
  n= 11  media   -37%  mediana   -36%  descartado: top 10 holders > 20%  (a 60 min)
  n=  9  media    +0%  mediana    +0%  descartado: mint no revocado  (a 60 min)
  n=  7  media   +29%  mediana    -5%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  6  media    -3%  mediana    -1%  descartado: red de insiders detectada  (a 180 min)
  n=  5  media   -39%  mediana   -17%  descartado: score bajo  (a 180 min)
  n=  5  media   +17%  mediana    -9%  descartado: riesgo critico segun RugCheck  (a 180 min)
  n=  4  media    -0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  4  media   -40%  mediana   -38%  descartado: top 10 holders > 20%  (a 180 min)
  n=  2  media   -99%  mediana   -99%  operado  (a 60 min)
  n=  2  media    -7%  mediana    -7%  descartado: dev vinculado a rugs  (a 60 min)
  n=  2  media    -3%  mediana    -3%  descartado: mint no revocado  (a 180 min)
  n=  2  media    -6%  mediana    -6%  descartado: dev vinculado a rugs  (a 180 min)
  sin datos de precio posterior: 1

DIAGNOSTICO
{"tokens_vistos": 2758, "evaluaciones": 5399, "con_volumen": 84, "rugcheck_llamadas": 84, "sin_par": 802, "http_429": 7}
known muestra: [["88bzw2cTzi8tgTBDFLY6ECfDVuRkHQ7novcE3gMCf2hu", {"name": "Creator", "type": "CREATOR"}], ["DTyZ6DCZzxmBVRJjDepJ4oqrrDKzK2zbce5jaPiQ1eg", {"name": "Printr Stake Pool", "type": "LOCKER"}], ["DzN8EgT6UULz6pmeVgqriC5XEfHiNapi1XbXc3zRazpG", {"name": "Pump Fun AMM", "type": "AMM"}]]
websocket: sin errores
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Low Liquidity": "danger", "Mint Authority still enabled": "danger", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger", "Mutable metadata": "warn", "Creator history of rugged tokens": "danger", "Single holder ownership": "danger", "High holder concentration": "warn", "Large Amount of LP Unlocked": "danger", "Missing file metadata": "warn", "High market cap per holder": "warn", "High holder correlation": "warn", "Fee config enabled": "warn"}
rugcheck holder0: {"address": "8QcwH1u6GHBB7AdWKDcA1GLjmg63Qm6jcFe5casYp8cf", "amount": 859897814431310, "decimals": 6, "pct": 89.67254584212296, "uiAmount": 859897814.43131, "uiAmountString": "859897814.43131", "owner": "h7KMkKyusF4CfGtSCB1yL9T5vVPfe1XLWFpFan2jTCU", "insider": false}