EJECUCION 20261112_2241

RESUMEN
Equity final: 974.07 (-2.6%)
Max drawdown: -3.6%
Pares vistos: 6071, pasan filtros: 6
Operaciones cerradas: 2, ganadoras: 0
Ganancia media: +0.0%, perdida media: -16.2%
Motivos de descarte:
   4261  volumen 1h < 50k$
   1710  sin par en DexScreener
     57  top 10 holders > 20%
     57  red de insiders detectada
     44  riesgo critico segun RugCheck
     12  LP no bloqueado
      7  mint no revocado
      7  freeze authority activo
      5  sin datos de seguridad (no se opera)
      5  dev vinculado a rugs
      1  score 0.46 < 0.60
      1  score 0.24 < 0.60
      1  score 0.40 < 0.60
      1  ya operado (no promediar a la baja)

EMBUDO (de arriba abajo)
  tokens vistos:               2800
  evaluaciones con precio:     4361
  con volumen >= 50k$:         100
  pasan filtros de seguridad:  6
  aprobados por el Analyst:    3
  compras simuladas:           2

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 34  media   -10%  mediana    -1%  descartado: top 10 holders > 20%  (a 60 min)
  n= 15  media   -28%  mediana    -5%  descartado: top 10 holders > 20%  (a 180 min)
  n= 11  media   -38%  mediana    -4%  descartado: LP no bloqueado  (a 60 min)
  n= 10  media   -17%  mediana    -5%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  9  media   -37%  mediana    -7%  descartado: LP no bloqueado  (a 180 min)
  n=  8  media   -17%  mediana   -32%  descartado: red de insiders detectada  (a 60 min)
  n=  4  media    -0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  4  media    -1%  mediana    -1%  descartado: mint no revocado  (a 60 min)
  n=  4  media   -27%  mediana   -27%  descartado: riesgo critico segun RugCheck  (a 180 min)
  n=  3  media   +47%  mediana   +10%  descartado: score bajo  (a 60 min)
  n=  3  media   +63%  mediana    -8%  descartado: score bajo  (a 180 min)
  n=  3  media    -2%  mediana    -2%  descartado: sin datos de seguridad (no se opera)  (a 180 min)
  n=  2  media    -2%  mediana    -2%  descartado: dev vinculado a rugs  (a 60 min)
  n=  2  media   -49%  mediana   -49%  descartado: red de insiders detectada  (a 180 min)
  sin datos de precio posterior: 4

DIAGNOSTICO
{"tokens_vistos": 2800, "evaluaciones": 4361, "ws_reconexiones": 1, "con_volumen": 100, "rugcheck_llamadas": 100, "sin_par": 1710}
known muestra: [["27M4Rv8TWpMyx9ejbUJXcWK3bpPfr9qaQQs1vufd2jS3", {"name": "Meteora DAMM v2 Pool", "type": "AMM"}], ["2AVRduf5VYrtUXYFFGwPGF2b4f5E3dmT7fky5RZsZ1VH", {"name": "Meteora DAMM v2 Pool", "type": "AMM"}], ["6oYQvgL3RymUdQ5p8MBVTu8apM1rrnFZZDa6qxrv5TVy", {"name": "Pump Fun", "type": "AMM"}]]
websocket: no close frame received or sent
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Mint Authority still enabled": "danger", "Large Amount of LP Unlocked": "danger", "Top 10 holders high ownership": "danger", "Single holder ownership": "danger", "High ownership": "danger", "Low amount of LP Providers": "warn", "Mutable metadata": "warn", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger", "Low Liquidity": "danger", "Creator history of rugged tokens": "danger", "High holder concentration": "warn", "High market cap per holder": "warn"}
rugcheck holder0: {"address": "D5pDAmD6Qj7cdv5sWmcTazYeRQ4MTJ1DqRfkTnmRsh5Q", "amount": 288043413777602, "decimals": 6, "pct": 28.804341377760228, "uiAmount": 288043413.777602, "uiAmountString": "288043413.777602", "owner": "HUehMvkRSSoNs7AAmQbJKurdbPxnZckaePUVgVzge6Ca", "insider": false}