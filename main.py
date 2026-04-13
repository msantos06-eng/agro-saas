from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/ndvi")
def ndvi():

    ndvi = np.random.rand(20,20)
    avg = float(ndvi.mean())

    if avg < 0.3:
        status = "Estresse crítico"
        recommendation = "Irrigação urgente"
    elif avg < 0.6:
        status = "Médio vigor"
        recommendation = "Monitorar nutrientes"
    else:
        status = "Saudável"
        recommendation = "Sem ação"

    return {
        "status": status,
        "recommendation": recommendation,
        "mean_ndvi": avg
    }
import streamlit as st
import requests

st.title("🌱 Agro SaaS Pro")

API_URL = "http://localhost:8000"

if st.button("Rodar NDVI"):
    response = requests.get(f"{API_URL}/ndvi")

    data = response.json()

    st.success(data["status"])
    st.info(data["recommendation"])
    st.image(data["map"])
