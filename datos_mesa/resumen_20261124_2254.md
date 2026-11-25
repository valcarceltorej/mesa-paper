EJECUCION 20261124_2254

RESUMEN
Equity final: 993.95 (-0.6%)
Max drawdown: -3.3%
Pares vistos: 3675, pasan filtros: 7
Operaciones cerradas: 2, ganadoras: 1
Ganancia media: +3.2%, perdida media: -10.7%
Motivos de descarte:
   3173  volumen 1h < 50k$
    454  sin par en DexScreener
     28  riesgo critico segun RugCheck
     25  red de insiders detectada
     19  top 10 holders > 20%
      9  mint no revocado
      7  dev vinculado a rugs
      4  freeze authority activo
      1  score 0.36 < 0.60
      1  score 0.32 < 0.60
      1  score 0.45 < 0.60
      1  score 0.34 < 0.60
      1  score 0.25 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               1528
  evaluaciones con precio:     3221
  con volumen >= 50k$:         48
  pasan filtros de seguridad:  7
  aprobados por el Analyst:    2
  compras simuladas:           2

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n=  9  media   -44%  mediana   -65%  descartado: top 10 holders > 20%  (a 60 min)
  n=  8  media    +0%  mediana    +0%  descartado: mint no revocado  (a 60 min)
  n=  6  media   -26%  mediana   -23%  descartado: dev vinculado a rugs  (a 60 min)
  n=  6  media   -33%  mediana   -19%  descartado: red de insiders detectada  (a 60 min)
  n=  3  media   -25%  mediana   -10%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  3  media   -47%  mediana   -64%  descartado: top 10 holders > 20%  (a 180 min)
  n=  3  media   -49%  mediana   -42%  descartado: dev vinculado a rugs  (a 180 min)
  n=  2  media    -1%  mediana    -1%  descartado: mint no revocado  (a 180 min)
  n=  2  media   +48%  mediana   +48%  descartado: score bajo  (a 60 min)
  n=  1  media   -99%  mediana   -99%  operado  (a 60 min)
  n=  1  media   -99%  mediana   -99%  operado  (a 180 min)
  n=  1  media   -62%  mediana   -62%  descartado: riesgo critico segun RugCheck  (a 180 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 1528, "evaluaciones": 3221, "sin_par": 454, "con_volumen": 48, "rugcheck_llamadas": 48, "ws_reconexiones": 8}
known muestra: [["12roZkxXJ3ZEyGeAE4s7Vwqvv2m54QmBvVG8CbzAduja", {"name": "Meteora DAMM v2 Pool", "type": "AMM"}], ["1k49ap2GKHsK9riGVezqQJhfzLBMtzJwaN2QmY4kSK1", {"name": "Meteora DLMM Pool", "type": "AMM"}], ["26FzmyA8bhvHWthWhrnbFGrax3dsvLg5EsPe8zquvAWv", {"name": "Meteora DLMM Pool", "type": "AMM"}]]
websocket: no close frame received or sent
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Mint Authority still enabled": "danger", "Mutable metadata": "warn", "Low Liquidity": "danger", "Creator history of rugged tokens": "danger", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger", "High holder concentration": "warn"}
rugcheck holder0: {"address": "3pDpC7rRmrPRPvGRaGLJH8wzRUc4B1vHVZ574xPp82BB", "amount": 1060279840280, "decimals": 8, "pct": 9.6092455371657, "uiAmount": 10602.7984028, "uiAmountString": "10602.7984028", "owner": "ByiAbN9MJhfQKGK5WJrfgko6XS88qqERQVRLWZTsvyTf", "insider": false}