EJECUCION 20261115_2235

RESUMEN
Equity final: 971.99 (-2.8%)
Max drawdown: -3.1%
Pares vistos: 5173, pasan filtros: 5
Operaciones cerradas: 1, ganadoras: 0
Ganancia media: +0.0%, perdida media: -34.4%
Motivos de descarte:
   4489  volumen 1h < 50k$
    615  sin par en DexScreener
     27  sin datos de seguridad (no se opera)
     23  red de insiders detectada
     22  riesgo critico segun RugCheck
     22  top 10 holders > 20%
      9  mint no revocado
      6  freeze authority activo
      3  LP no bloqueado
      1  score 0.37 < 0.60
      1  score 0.28 < 0.60
      1  score 0.26 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               2244
  evaluaciones con precio:     4558
  con volumen >= 50k$:         69
  pasan filtros de seguridad:  5
  aprobados por el Analyst:    2
  compras simuladas:           2

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 24  media    -0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n= 15  media    -0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 180 min)
  n= 12  media   -11%  mediana    -2%  descartado: top 10 holders > 20%  (a 60 min)
  n=  9  media    -3%  mediana    -1%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  8  media    -7%  mediana    -4%  descartado: riesgo critico segun RugCheck  (a 180 min)
  n=  6  media    +0%  mediana    -0%  descartado: mint no revocado  (a 60 min)
  n=  5  media   -49%  mediana   -93%  descartado: red de insiders detectada  (a 60 min)
  n=  5  media   -31%  mediana    -4%  descartado: top 10 holders > 20%  (a 180 min)
  n=  3  media   -50%  mediana   -73%  descartado: score bajo  (a 60 min)
  n=  2  media   -48%  mediana   -48%  operado  (a 60 min)
  n=  2  media   -84%  mediana   -84%  descartado: score bajo  (a 180 min)
  n=  2  media   -83%  mediana   -83%  descartado: red de insiders detectada  (a 180 min)
  n=  1  media   -97%  mediana   -97%  operado  (a 180 min)
  n=  1  media    +0%  mediana    +0%  descartado: mint no revocado  (a 180 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 2244, "evaluaciones": 4558, "con_volumen": 69, "rugcheck_llamadas": 69, "sin_par": 615, "ws_reconexiones": 2}
known muestra: [["2UHspHhcVF3TQ5WwxYLAopB59tMYp82fykGjnfL1AeDZ", {"name": "Pump Fun", "type": "AMM"}], ["4SbS7YhBUNGZSFVARcjwqAsqixS4V94RNcWHqrGQ8c3a", {"name": "Pump Fun", "type": "AMM"}], ["4rxc8Wgfs6Rt1NnZd7myWvGXK2ZvNCVkodBhpiEPtgCC", {"name": "Meteora DAMM v2 Pool", "type": "AMM"}]]
websocket: server rejected WebSocket connection: HTTP 502
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Low Liquidity": "danger", "Single holder ownership": "danger", "Mint Authority still enabled": "danger", "High holder concentration": "warn", "Missing file metadata": "warn", "Mutable metadata": "warn", "Top 10 holders high ownership": "danger", "High market cap per holder": "warn", "High ownership": "danger", "High holder correlation": "warn", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger"}
rugcheck holder0: {"address": "AaJN1pCcNkzesLceREVaXkqQr7WJJjoyt5pQJL8NV3Gp", "amount": 217405225928000, "decimals": 6, "pct": 22.441044001361497, "uiAmount": 217405225.928, "uiAmountString": "217405225.928", "owner": "FT1dAhiZa9PK7F6Lfx3fMeFLgCDJqS7pXVmXkrQa4rXM", "insider": false}