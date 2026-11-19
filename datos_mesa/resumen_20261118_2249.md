EJECUCION 20261118_2249

RESUMEN
Equity final: 988.84 (-1.1%)
Max drawdown: -1.1%
Pares vistos: 6382, pasan filtros: 3
Operaciones cerradas: 1, ganadoras: 0
Ganancia media: +0.0%, perdida media: -14.0%
Motivos de descarte:
   5997  volumen 1h < 50k$
    306  sin par en DexScreener
     66  top 10 holders > 20%
     66  red de insiders detectada
     42  riesgo critico segun RugCheck
     38  mint no revocado
     11  freeze authority activo
     10  LP no bloqueado
      4  sin datos de seguridad (no se opera)
      1  score 0.51 < 0.60
      1  score 0.33 < 0.60

EMBUDO (de arriba abajo)
  tokens vistos:               2806
  evaluaciones con precio:     6076
  con volumen >= 50k$:         81
  pasan filtros de seguridad:  3
  aprobados por el Analyst:    1
  compras simuladas:           1

SEGUIMIENTO (que paso con los tokens que llegaron al analisis)
  n= 26  media    +0%  mediana    +0%  descartado: mint no revocado  (a 60 min)
  n= 24  media   -15%  mediana    +0%  descartado: top 10 holders > 20%  (a 60 min)
  n= 12  media   -24%  mediana    +1%  descartado: top 10 holders > 20%  (a 180 min)
  n= 11  media    -1%  mediana    -1%  descartado: mint no revocado  (a 180 min)
  n=  4  media    -0%  mediana    -0%  descartado: sin datos de seguridad (no se opera)  (a 60 min)
  n=  3  media    -2%  mediana    -2%  descartado: riesgo critico segun RugCheck  (a 60 min)
  n=  2  media    -3%  mediana    -3%  descartado: riesgo critico segun RugCheck  (a 180 min)
  n=  2  media   -12%  mediana   -12%  descartado: red de insiders detectada  (a 60 min)
  n=  1  media   -98%  mediana   -98%  operado  (a 60 min)
  sin datos de precio posterior: 0

DIAGNOSTICO
{"tokens_vistos": 2806, "evaluaciones": 6076, "con_volumen": 81, "rugcheck_llamadas": 81, "sin_par": 306, "ws_reconexiones": 2}
known muestra: [["12jVqQ27tF9rcdxxUcPZ3ym3AqnmtcA4poUGeRWdaUWB", {"name": "Meteora DLMM Pool", "type": "AMM"}], ["14QgQpEXrcNipN1gq73sS1XmLt9JgW9jGqi6pSeFtu25", {"name": "Orca AMM", "type": "AMM"}], ["1b7C7m3REiR4cv5x8pAYJUkncxEoa1CZEFx9BwZRPQL", {"name": "Meteora DLMM Pool", "type": "AMM"}]]
websocket: server rejected WebSocket connection: HTTP 502
rugcheck claves: ["creator", "creatorBalance", "creatorTokens", "deployPlatform", "detectedAt", "events", "fileMeta", "freezeAuthority", "graphInsidersDetected", "insiderNetworks", "knownAccounts", "launchpad", "lockerOwners", "lockerScanStatus", "lockers", "markets", "mint", "mintAuthority", "price", "risks", "rugged", "score", "score_normalised", "token", "tokenMeta", "tokenProgram", "tokenType", "token_extensions", "topHolders", "totalHolders", "totalLPProviders", "totalMarketLiquidity", "totalStableLiquidity", "transferFee", "validation", "verification"]
rugcheck riesgos vistos: {"Mint Authority still enabled": "danger", "Mutable metadata": "warn", "Top 10 holders high ownership": "danger", "Single holder ownership": "danger", "High ownership": "danger", "Low Liquidity": "danger", "Permanent Control Enabled": "danger", "Freeze Authority still enabled": "danger", "High holder concentration": "warn", "Fee config enabled": "warn", "Name Mismatch": "warn", "Large Amount of LP Unlocked": "danger"}
rugcheck holder0: {"address": "7AN6avKCJPMkXkW8kPwMuHmaWvJeHH69e8rKpLf9rdfk", "amount": 229261858182103957, "decimals": 6, "pct": 27.894188624355827, "uiAmount": 229261858182.10397, "uiAmountString": "229261858182.103957", "owner": "Cfq1ts1iFr1eUWWBm8eFxUzm5R3YA3UvMZznwiShbgZt", "insider": false}