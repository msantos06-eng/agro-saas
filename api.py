from fastapi import FastAPI
import numpy as np
from ndvi import calculate_ndvi

app = FastAPI()

@app.get("/ndvi")
def run_ndvi():

    red = np.random.rand(10,10)
    nir = np.random.rand(10,10)

    ndvi = calculate_ndvi(red, nir)
    avg = float(ndvi.mean())

    if avg < 0.3:
        status = "Estresse crítico"
        recommendation = "Irrigação urgente"
    elif avg < 0.6:
        status = "Médio vigor"
        recommendation = "Monitorar nutrientes"
    else:
        status = "Alto vigor"
        recommendation = "Área saudável"

    return {
        "status": status,
        "recommendation": recommendation,
        "map": "https://dummyimage.com/600x300/green/white.png"
    }