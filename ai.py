def analyze_sentinel_ndvi(ndvi, rainfall, temp):

    avg_ndvi = float(ndvi.mean())

    if avg_ndvi < 0.3:
        status = "Estresse crítico"
        recommendation = "Irrigação urgente + análise de solo"
    elif avg_ndvi < 0.6:
        status = "Médio vigor"
        recommendation = "Monitorar e ajustar nutrição"
    else:
        status = "Alto vigor"
        recommendation = "Área saudável"

    return {
        "status": status,
        "recommendation": recommendation,
        "avg_ndvi": avg_ndvi
    }