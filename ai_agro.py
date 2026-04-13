import numpy as np

def analyze_ndvi(ndvi):

    avg = ndvi.mean()

    if avg < 0.3:
        return "Estresse crítico", "Irrigação urgente"
    elif avg < 0.6:
        return "Médio vigor", "Monitorar nutrientes"
    return "Saudável", "Sem ação"
def analyze_sentinel_ndvi(ndvi_array, rainfall, temp):

    ndvi_mean = np.mean(ndvi_array)

    score = (
        ndvi_mean * 0.6 +
        rainfall * 0.2 +
        (1 - abs(temp - 25) / 25) * 0.2
    )

    if score < 0.35:
        return {
            "status": "CRÍTICO",
            "recommendation": "Correção de solo + irrigação imediata + replantio parcial"
        }

    elif score < 0.6:
        return {
            "status": "ATENÇÃO",
            "recommendation": "Aplicação localizada (VRA) + fertilização variável"
        }

    else:
        return {
            "status": "SAUDÁVEL",
            "recommendation": "Manter manejo atual + monitoramento semanal"
        }