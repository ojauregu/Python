import json_tools

json_tools.diff

a={"internalID": "-232dfa67-568a-435f-a695-c23731031e0d", "externalID": " ", "sourceSystemAlias": {"sourceSystem": "MUREX3FX", "aliasName": "P37ID", "alias": "-26966431"}, "entity": "BSTE", "entityCName": "31434.4", "entityOrig": "MADRID", "branch": "MADRID", "branchCName": "22.21", "branchOrig": " ", "portfolio": "ESDGINFBON", "portfolioCName": "11911.21", "portfolioOrig": "ESDG_INF_BOND", "portfolio2": "REPOSMM", "portfolio2CName": "797.21", "portfolio2Orig": "ESSR_REPOSMM", "counterparty": "BSTE", "counterpartyCName": "31434.4", "counterpartyOrig": " ", "dealFamily": "FI", "dealFamilyOrig": "IRD", "dealType": "REPOLEND", "dealTypeOrig": "REPO", "dealSubType": "FIREPO", "dealSubTypeOrig": "REPO", "tradeDate": "2021-12-02", "maturityDate": "2021-12-03", "typology": " ", "typologyOrig": "Repo", "valueDate": "2021-12-02", "status": "VFO", "statusOrig": "1s", "legs": [{"amount1": 4583000.0, "amount2": 5016730.9953, "amount1Currency": "160.4", "amount1CurrencyISO": "EUR", "amount1CurrencyOrig": "EUR", "amount2Currency": "160.4", "amount2CurrencyISO": "EUR", "amount2CurrencyOrig": "EUR", "legDirection": "Sell", "legDirectionOrig": "pay", "nature": "Fixed", "index": " ", "indexOrig": " ", "rate": 0.0, "settlementRate": " ", "underlying": "NA", "underlyingOrig": "IT0005370306", "spread": " ", "deliverable": "false ", "convention": "2.4", "conventionOrig": "LIN ACT/360", "strike": " ", "frequency": "NA", "frequencyOrig": "0 BUSINESSDAY", "callPut": " ", "callPutOrig": " ", "openRepo": "false ", "flows": [{"fixingDate": " ", "settlementDate": "2021-12-03", "startDate": "2021-12-02", "endDate": "2021-12-03", "amount": 0.0, "nominal": 0.0, "currency": "160.4", "currencyISO": "EUR", "currencyOrig": "EUR", "flowType": "Interest", "flowID": " ", "isCash": "true", "flowDirection": "Sell", "flowDirectionOrig": "receive", "isAdditional": " ", "indexPrice": " ", "inflationRate": " "}, {"fixingDate": " ", "settlementDate": "2021-12-02", "startDate": " ", "endDate": " ", "amount": 4583.0, "nominal": 4583000.0, "currency": "NA", "currencyISO": "BTPS26JUL2.1", "currencyOrig": "BTPS26JUL2.1", "flowType": "Security", "flowID": " ", "isCash": "false ", "flowDirection": "Buy", "flowDirectionOrig": "Buy", "isAdditional": " ", "indexPrice": " ", "inflationRate": " "}], "scheduleMethod": " ", "scheduleMethodOrig": " ", "capFloor": " ", "quantity1": 4583.0, "quantity2": " ", "currentQuantity": 4583.0, "underlyingName": " ", "securityMarket": " ", "frequencyDesc": "NA", "conventionDesc": "NA", "price": " ", "dirtyPrice": 109.46391, "yield": " ", "isFlex": " ", "haircut": " ", "haircutCalcBase": " ", "optionStyle": " ", "optionType": " ", "settlementDate": " ", "fixingDate": " ", "referenceRate": " ", "notation": " ", "initialSecurityExchange": "Y", "finalSecurityExchange": "Y", "isIntermediateExchange": " ", "settleExotic": " ", "settleExoticCName": " ", "settleExoticOrig": " ", "securityBasketComponents": " ", "bespoke": " ", "fixingFrequency": " ", "fixingRatioFrequency": " ", "paymentFrequency": " ", "paymentRatioFrequency": " ", "indexFrequency": " ", "basket": " ", "deprecatedInflationRate": " ", "fxQuoteBasis": " ", "fxQuotation": " "}, {"amount1": 5016730.9953, "amount2": 5016640.4153, "amount1Currency": "160.4", "amount1CurrencyISO": "EUR", "amount1CurrencyOrig": "EUR", "amount2Currency": "160.4", "amount2CurrencyISO": "EUR", "amount2CurrencyOrig": "EUR", "legDirection": "Buy", "legDirectionOrig": "receive", "nature": "Fixed", "index": " ", "indexOrig": " ", "rate": -0.65, "settlementRate": " ", "underlying": " ", "underlyingOrig": " ", "spread": " ", "deliverable": "false ", "convention": "2.4", "conventionOrig": "LIN ACT/360", "strike": " ", "frequency": "NA", "frequencyOrig": "1 YEAR", "callPut": " ", "callPutOrig": " ", "openRepo": "false ", "flows": [{"fixingDate": " ", "settlementDate": "2021-12-03", "startDate": "2021-12-02", "endDate": "2021-12-03", "amount": 90.58, "nominal": 5016730.9953, "currency": "160.4", "currencyISO": "EUR", "currencyOrig": "EUR", "flowType": "Interest", "flowID": " ", "isCash": "true", "flowDirection": "Sell", "flowDirectionOrig": "receive", "isAdditional": " ", "indexPrice": " ", "inflationRate": " "}, {"fixingDate": " ", "settlementDate": "2021-12-02", "startDate": " ", "endDate": " ", "amount": 5016730.9953, "nominal": " ", "currency": "160.4", "currencyISO": "EUR", "currencyOrig": "EUR", "flowType": "Principal", "flowID": " ", "isCash": "true", "flowDirection": "Sell", "flowDirectionOrig": "Sell", "isAdditional": " ", "indexPrice": " ", "inflationRate": " "}, {"fixingDate": " ", "settlementDate": "2021-12-03", "startDate": " ", "endDate": " ", "amount": 5016730.9953, "nominal": " ", "currency": "160.4", "currencyISO": "EUR", "currencyOrig": "EUR", "flowType": "Principal", "flowID": " ", "isCash": "true", "flowDirection": "Buy", "flowDirectionOrig": "Buy", "isAdditional": " ", "indexPrice": " ", "inflationRate": " "}], "scheduleMethod": " ", "scheduleMethodOrig": "Periodical", "capFloor": " ", "quantity1": " ", "quantity2": " ", "currentQuantity": " ", "underlyingName": " ", "securityMarket": " ", "frequencyDesc": "NA", "conventionDesc": "NA", "price": " ", "dirtyPrice": " ", "yield": " ", "isFlex": " ", "haircut": 0.0, "haircutCalcBase": "OneDividedByOnePlusMinusX", "optionStyle": " ", "optionType": " ", "settlementDate": " ", "fixingDate": " ", "referenceRate": " ", "notation": " ", "initialSecurityExchange": "Y", "finalSecurityExchange": "Y", "isIntermediateExchange": " ", "settleExotic": " ", "settleExoticCName": " ", "settleExoticOrig": " ", "securityBasketComponents": " ", "bespoke": " ", "fixingFrequency": " ", "fixingRatioFrequency": " ", "paymentFrequency": " ", "paymentRatioFrequency": " ", "indexFrequency": " ", "basket": " ", "deprecatedInflationRate": " ", "fxQuoteBasis": " ", "fxQuotation": " "}], "otherSystemAlias": [{"sourceSystem": "MUREX3FX", "aliasName": "Component", "alias": "-26966431"}, {"sourceSystem": "MUREX3FX", "aliasName": "Contract", "alias": "-25636653"}, {"sourceSystem": "MUREX3FX", "aliasName": "RootContract", "alias": "-25636653"}], "additionalSystemAlias": [{"sourceSystem": "MUREX3FX", "aliasName": "Component", "alias": "26966431"}, {"sourceSystem": "MUREX3FX", "aliasName": "Contract", "alias": "25636653"}, {"sourceSystem": "MUREX3FX", "aliasName": "RootContract", "alias": "25636653"}, {"sourceSystem": "MUREX3FX", "aliasName": "TradeGlobalID", "alias": "TOMS-10809413"}, {"sourceSystem": "MUREX3FX", "aliasName": "ContractVersion", "alias": "1"}, {"sourceSystem": "MUREX3FX", "aliasName": "OriginContract", "alias": "25636653"}, {"sourceSystem": "P37", "aliasName": "GENERATED", "alias": "MIRROR"}], "sourceMsgRaw": " ", "sourceMsgHash": "bw-parser-mx3-fx-11-d2f65-bw0a107rd3q-1638459429061-e2ba455e-04be-49ea-9531-47d87bcd0d69", "action": "Upsert", "actionTypeOrig": " ", "results": " ", "filtered": "true", "parsingLevel": 100, "timestamp": "2021-12-02T15:37:08Z", "aggregatorID": "26966431", "OTCIndicator": " ", "user": "PROCESOS", "desk": "NA", "deskCName": "NA", "isInternal": "true", "dealDirection": "Buy", "dealDirectionOrig": "Buy", "version": " ", "dealStatus": "LIVE", "dealStatusOrig": "live", "adjustedMaturityDate": "2021-12-03", "scheduleGenerator": " ", "collateral": " ", "adjustedValueDate": " ", "channel": " ", "hasSSI": "false ", "lastActionTimestamp": "2021-12-02T15:37:08.266Z", "insertionTimestamp": "2021-12-02T15:37:08Z", "ingestionTimestamp": "2021-12-02T15:37:08Z", "processingTimestamp": "2021-12-02T15:37:09.431Z", "eventTimestamp": "2021-12-02T15:37:08.266Z", "properties": [{"type": "UDF", "name": "BLOCKTRADE", "value": "N"}, {"type": "UDF", "name": "BRKCLSFREQ", "value": "0."}, {"type": "UDF", "name": "CCY", "value": "EUR"}, {"type": "UDF", "name": "CCY2", "value": "EUR"}, {"type": "UDF", "name": "CLS", "value": "SI"}, {"type": "UDF", "name": "COMMENT", "value": "--"}, {"type": "UDF", "name": "COMMISSION", "value": "0."}, {"type": "UDF", "name": "CRDTCHRG", "value": "0."}, {"type": "UDF", "name": "CUS_DIRECT", "value": "Y"}, {"type": "UDF", "name": "DIRECTIAV", "value": "0."}, {"type": "UDF", "name": "DISCMARGIN", "value": "0."}, {"type": "UDF", "name": "DVA", "value": "0."}, {"type": "UDF", "name": "ELECPLATID", "value": "10809413"}, {"type": "UDF", "name": "ELECTPLATF", "value": "VOZ"}, {"type": "UDF", "name": "HRCT", "value": "0."}, {"type": "UDF", "name": "IDCORR", "value": "TOMS10809413MX|TOMS-INS-10809413"}, {"type": "UDF", "name": "IDPROPASES", "value": "0"}, {"type": "UDF", "name": "INDEP_AMNT", "value": "0."}, {"type": "UDF", "name": "INV_RATE", "value": "0."}, {"type": "UDF", "name": "LIQDTYCHRG", "value": "0."}, {"type": "UDF", "name": "MARKETSPRE", "value": "0"}, {"type": "UDF", "name": "MONETCODE", "value": "MO1487"}, {"type": "UDF", "name": "MONETDESC", "value": "FI_Mx_Bond Repo"}, {"type": "UDF", "name": "MRNMONETCO", "value": "MO8354"}, {"type": "UDF", "name": "MRNMONETDE", "value": "FI_Mrn_Bond Repo"}, {"type": "UDF", "name": "MVA", "value": "0."}, {"type": "UDF", "name": "ORIGIN", "value": "DIRECTO"}, {"type": "UDF", "name": "RETCC", "value": "no"}, {"type": "UDF", "name": "RVA", "value": "0."}, {"type": "UDF", "name": "SPRD_CREDT", "value": "0."}, {"type": "UDF", "name": "STRIPDEALI", "value": "0"}, {"type": "UDF", "name": "SUCURSAL", "value": "5493"}, {"type": "UDF", "name": "TL_PURPOSE", "value": "NEG"}, {"type": "UDF", "name": "TRADERCORP", "value": "N128892"}, {"type": "UDF", "name": "TYPMARXIT", "value": "Cliente"}, {"type": "Other Data", "name": "TemplateLabel", "value": "REPO_FIJO"}, {"type": "FinancialData", "name": "NonUnwoundRatio", "value": "1."}, {"type": "FinancialData", "name": "CurrentSpread", "value": " "}, {"type": "FinancialData", "name": "LiveQuantity", "value": "4583."}, {"type": "FinancialData", "name": "PayCond", "value": "dvp"}, {"type": "Other Data", "name": "OriginID", "value": "26966431"}, {"type": "FinancialData", "name": "SistemaFrontOrigen", "value": "TOMS-INS"}]}
b={"internalID": "-232dfa67-568a-435f-a695-c23731031e0d", "externalID": " ", "sourceSystemAlias": {"sourceSystem": "MUREX3FX", "aliasName": "P37ID", "alias": "-26966431"}, "entity": "BSTE", "entityCName": "31434.4", "entityOrig": "MADRID", "branch": "MADRID", "branchCName": "22.21", "branchOrig": " ", "portfolio": "ESDGINFBON", "portfolioCName": "11911.21", "portfolioOrig": "ESDG_INF_BOND", "portfolio2": "REPOSMM", "portfolio2CName": "797.21", "portfolio2Orig": "ESSR_REPOSMM", "counterparty": "BSTE", "counterpartyCName": "31434.4", "counterpartyOrig": " ", "dealFamily": "FI", "dealFamilyOrig": "IRD", "dealType": "REPOLEND", "dealTypeOrig": "REPO", "dealSubType": "FIREPO", "dealSubTypeOrig": "REPO", "tradeDate": "2021-12-02", "maturityDate": "2021-12-03", "typology": " ", "typologyOrig": "Repo", "valueDate": "2021-12-02", "status": "VFO", "statusOrig": "1s", "legs": [{"amount1": 4583000.0, "amount2": 5016730.9953, "amount1Currency": "160.4", "amount1CurrencyISO": "EUR", "amount1CurrencyOrig": "EUR", "amount2Currency": "160.4", "amount2CurrencyISO": "EUR", "amount2CurrencyOrig": "EUR", "legDirection": "Sell", "legDirectionOrig": "pay", "nature": "Fixed", "index": " ", "indexOrig": " ", "rate": 0.0, "settlementRate": " ", "underlying": "NA", "underlyingOrig": "IT0005370306", "spread": " ", "deliverable": "false ", "convention": "2.4", "conventionOrig": "LIN ACT/360", "strike": " ", "frequency": "NA", "frequencyOrig": "5 BUSINESSDAY", "callPut": " ", "callPutOrig": " ", "openRepo": "false ", "flows": [{"fixingDate": " ", "settlementDate": "2021-12-03", "startDate": "2021-12-02", "endDate": "2021-12-03", "amount": 0.0, "nominal": 0.0, "currency": "160.4", "currencyISO": "EUR", "currencyOrig": "EUR", "flowType": "Interest", "flowID": " ", "isCash": "true", "flowDirection": "Sell", "flowDirectionOrig": "receive", "isAdditional": " ", "indexPrice": " ", "inflationRate": " "}, {"fixingDate": " ", "settlementDate": "2021-12-02", "startDate": " ", "endDate": " ", "amount": 4583.0, "nominal": 4583000.0, "currency": "NA", "currencyISO": "BTPS26JUL2.1", "currencyOrig": "BTPS26JUL2.1", "flowType": "Security", "flowID": " ", "isCash": "false ", "flowDirection": "Buy", "flowDirectionOrig": "Buy", "isAdditional": " ", "indexPrice": " ", "inflationRate": " "}], "scheduleMethod": " ", "scheduleMethodOrig": " ", "capFloor": " ", "quantity1": 4583.0, "quantity2": " ", "currentQuantity": 4583.0, "underlyingName": " ", "securityMarket": " ", "frequencyDesc": "NA", "conventionDesc": "NA", "price": " ", "dirtyPrice": 109.46391, "yield": " ", "isFlex": " ", "haircut": " ", "haircutCalcBase": " ", "optionStyle": " ", "optionType": " ", "settlementDate": " ", "fixingDate": " ", "referenceRate": " ", "notation": " ", "initialSecurityExchange": "Y", "finalSecurityExchange": "Y", "isIntermediateExchange": " ", "settleExotic": " ", "settleExoticCName": " ", "settleExoticOrig": " ", "securityBasketComponents": " ", "bespoke": " ", "fixingFrequency": " ", "fixingRatioFrequency": " ", "paymentFrequency": " ", "paymentRatioFrequency": " ", "indexFrequency": " ", "basket": " ", "deprecatedInflationRate": " ", "fxQuoteBasis": " ", "fxQuotation": " "}, {"amount1": 5016730.9953, "amount2": 5016640.4153, "amount1Currency": "160.4", "amount1CurrencyISO": "EUR", "amount1CurrencyOrig": "EUR", "amount2Currency": "160.4", "amount2CurrencyISO": "EUR", "amount2CurrencyOrig": "EUR", "legDirection": "Buy", "legDirectionOrig": "receive", "nature": "Fixed", "index": " ", "indexOrig": " ", "rate": -0.65, "settlementRate": " ", "underlying": " ", "underlyingOrig": " ", "spread": " ", "deliverable": "false ", "convention": "2.4", "conventionOrig": "LIN ACT/360", "strike": " ", "frequency": "NA", "frequencyOrig": "1 YEAR", "callPut": " ", "callPutOrig": " ", "openRepo": "false ", "flows": [{"fixingDate": " ", "settlementDate": "2021-12-03", "startDate": "2021-12-02", "endDate": "2021-12-03", "amount": 90.58, "nominal": 5016730.9953, "currency": "160.4", "currencyISO": "EUR", "currencyOrig": "EUR", "flowType": "Interest", "flowID": " ", "isCash": "true", "flowDirection": "Sell", "flowDirectionOrig": "receive", "isAdditional": " ", "indexPrice": " ", "inflationRate": " "}, {"fixingDate": " ", "settlementDate": "2021-12-02", "startDate": " ", "endDate": " ", "amount": 5016730.9953, "nominal": " ", "currency": "160.4", "currencyISO": "EUR", "currencyOrig": "EUR", "flowType": "Principal", "flowID": " ", "isCash": "true", "flowDirection": "Sell", "flowDirectionOrig": "Sell", "isAdditional": " ", "indexPrice": " ", "inflationRate": " "}, {"fixingDate": " ", "settlementDate": "2021-12-03", "startDate": " ", "endDate": " ", "amount": 5016730.9953, "nominal": " ", "currency": "160.4", "currencyISO": "EUR", "currencyOrig": "EUR", "flowType": "Principal", "flowID": " ", "isCash": "true", "flowDirection": "Buy", "flowDirectionOrig": "Buy", "isAdditional": " ", "indexPrice": " ", "inflationRate": " "}], "scheduleMethod": " ", "scheduleMethodOrig": "Periodical", "capFloor": " ", "quantity1": " ", "quantity2": " ", "currentQuantity": " ", "underlyingName": " ", "securityMarket": " ", "frequencyDesc": "NA", "conventionDesc": "NA", "price": " ", "dirtyPrice": " ", "yield": " ", "isFlex": " ", "haircut": 0.0, "haircutCalcBase": "OneDividedByOnePlusMinusX", "optionStyle": " ", "optionType": " ", "settlementDate": " ", "fixingDate": " ", "referenceRate": " ", "notation": " ", "initialSecurityExchange": "Y", "finalSecurityExchange": "Y", "isIntermediateExchange": " ", "settleExotic": " ", "settleExoticCName": " ", "settleExoticOrig": " ", "securityBasketComponents": " ", "bespoke": " ", "fixingFrequency": " ", "fixingRatioFrequency": " ", "paymentFrequency": " ", "paymentRatioFrequency": " ", "indexFrequency": " ", "basket": " ", "deprecatedInflationRate": " ", "fxQuoteBasis": " ", "fxQuotation": " "}], "otherSystemAlias": [{"sourceSystem": "MUREX3FX", "aliasName": "Component", "alias": "-26966431"}, {"sourceSystem": "MUREX3FX", "aliasName": "Contract", "alias": "-25636653"}, {"sourceSystem": "MUREX3FX", "aliasName": "RootContract", "alias": "-25636653"}], "additionalSystemAlias": [{"sourceSystem": "MUREX3FX", "aliasName": "Component", "alias": "26966431"}, {"sourceSystem": "MUREX3FX", "aliasName": "Contract", "alias": "25636653"}, {"sourceSystem": "MUREX3FX", "aliasName": "RootContract", "alias": "25636653"}, {"sourceSystem": "MUREX3FX", "aliasName": "TradeGlobalID", "alias": "TOMS-10809413"}, {"sourceSystem": "MUREX3FX", "aliasName": "ContractVersion", "alias": "1"}, {"sourceSystem": "MUREX3FX", "aliasName": "OriginContract", "alias": "25636653"}, {"sourceSystem": "P37", "aliasName": "GENERATED", "alias": "MIRROR"}], "sourceMsgRaw": " ", "sourceMsgHash": "bw-parser-mx3-fx-11-d2f65-bw0a107rd3q-1638459429061-e2ba455e-04be-49ea-9531-47d87bcd0d69", "action": "Upsert", "actionTypeOrig": " ", "results": " ", "filtered": "true", "parsingLevel": 100, "timestamp": "2021-12-02T15:37:08Z", "aggregatorID": "26966431", "OTCIndicator": " ", "user": "PROCESOS", "desk": "NA", "deskCName": "NA", "isInternal": "true", "dealDirection": "Buy", "dealDirectionOrig": "Buy", "version": " ", "dealStatus": "LIVE", "dealStatusOrig": "live", "adjustedMaturityDate": "2021-12-03", "scheduleGenerator": " ", "collateral": " ", "adjustedValueDate": " ", "channel": " ", "hasSSI": "false ", "lastActionTimestamp": "2021-12-02T15:37:08.266Z", "insertionTimestamp": "2021-12-02T15:37:08Z", "ingestionTimestamp": "2021-12-02T15:37:08Z", "processingTimestamp": "2021-12-02T15:37:09.431Z", "eventTimestamp": "2021-12-02T15:37:08.266Z", "properties": [{"type": "UDF", "name": "BLOCKTRADE", "value": "N"}, {"type": "UDF", "name": "BRKCLSFREQ", "value": "0."}, {"type": "UDF", "name": "CCY", "value": "EUR"}, {"type": "UDF", "name": "CCY2", "value": "EUR"}, {"type": "UDF", "name": "CLS", "value": "SI"}, {"type": "UDF", "name": "COMMENT", "value": "--"}, {"type": "UDF", "name": "COMMISSION", "value": "0."}, {"type": "UDF", "name": "CRDTCHRG", "value": "0."}, {"type": "UDF", "name": "CUS_DIRECT", "value": "Y"}, {"type": "UDF", "name": "DIRECTIAV", "value": "0."}, {"type": "UDF", "name": "DISCMARGIN", "value": "0."}, {"type": "UDF", "name": "DVA", "value": "0."}, {"type": "UDF", "name": "ELECPLATID", "value": "10809413"}, {"type": "UDF", "name": "ELECTPLATF", "value": "VOZ"}, {"type": "UDF", "name": "HRCT", "value": "0."}, {"type": "UDF", "name": "IDCORR", "value": "TOMS10809413MX|TOMS-INS-10809413"}, {"type": "UDF", "name": "IDPROPASES", "value": "0"}, {"type": "UDF", "name": "INDEP_AMNT", "value": "0."}, {"type": "UDF", "name": "INV_RATE", "value": "0."}, {"type": "UDF", "name": "LIQDTYCHRG", "value": "0."}, {"type": "UDF", "name": "MARKETSPRE", "value": "0"}, {"type": "UDF", "name": "MONETCODE", "value": "MO1487"}, {"type": "UDF", "name": "MONETDESC", "value": "FI_Mx_Bond Repo"}, {"type": "UDF", "name": "MRNMONETCO", "value": "MO8354"}, {"type": "UDF", "name": "MRNMONETDE", "value": "FI_Mrn_Bond Repo"}, {"type": "UDF", "name": "MVA", "value": "0."}, {"type": "UDF", "name": "ORIGIN", "value": "DIRECTO"}, {"type": "UDF", "name": "RETCC", "value": "no"}, {"type": "UDF", "name": "RVA", "value": "0."}, {"type": "UDF", "name": "SPRD_CREDT", "value": "0."}, {"type": "UDF", "name": "STRIPDEALI", "value": "0"}, {"type": "UDF", "name": "SUCURSAL", "value": "5493"}, {"type": "UDF", "name": "TL_PURPOSE", "value": "NEG"}, {"type": "UDF", "name": "TRADERCORP", "value": "N128892"}, {"type": "UDF", "name": "TYPMARXIT", "value": "Cliente"}, {"type": "Other Data", "name": "TemplateLabel", "value": "REPO_FIJO"}, {"type": "FinancialData", "name": "NonUnwoundRatio", "value": "1."}, {"type": "FinancialData", "name": "CurrentSpread", "value": " "}, {"type": "FinancialData", "name": "LiveQuantity", "value": "4583."}, {"type": "FinancialData", "name": "PayCond", "value": "tar"}, {"type": "Other Data", "name": "OriginID", "value": "26966431"}, {"type": "FinancialData", "name": "SistemaFrontOrigen", "value": "TOMS-INS"}]}
c=json_tools.diff(a,b)


print ("-------------------------------------")
print ("-------------------------------------")
print ("-------------------------------------")
print ("-------------------------------------")
print (c)
print ("-------------------------------------")
print ("-------------------------------------")
print ("-------------------------------------")
print ("-------------------------------------")