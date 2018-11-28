def resultProb(result, freqTable_obj):
    total = freqTable_obj.TableData("TOTAL", "CRYPTO_DATA") + freqTable_obj.TableData("TOTAL", "NOT_CRYPTO_DATA")
    return freqTable_obj.TableData("TOTAL", result) / total

def eventProb(event, freqTable_obj):
    total = freqTable_obj.TableData("TOTAL", "CRYPTO_DATA") + freqTable_obj.TableData("TOTAL", "NOT_CRYPTO_DATA")
    return (freqTable_obj.TableData(event, "CRYPTO_DATA") + freqTable_obj.TableData(event, "NOT_CRYPTO_DATA")) / total


def aprioriProb(event, result, freqTable_obj):
    return freqTable_obj.TableData(event, result) / freqTable_obj.TableData("TOTAL", result)

def apostorioriProb(result, event, freqTable_obj):
    return aprioriProb(event, result, freqTable_obj) * resultProb(result, freqTable_obj) / eventProb(event, freqTable_obj)
