import streamlit as st
import sqlite3
import hashlib
import os
import requests
import json
import numpy as np
from PIL import Image

from ndvi import calculate_ndvi
from vra import generate_vra_map, export_vra_csv
from sentinel import get_token, search_sentinel
from ndvi_map import create_ndvi_colored_map

try:
    from ai_agro import analyze_sentinel_ndvi
except ImportError:
    analyze_sentinel_ndvi = None

from streamlit_folium import st_folium

# 🚨 TEM QUE SER A PRIMEIRA LINHA STREAMLIT
st.set_page_config(page_title="NDVI SaaS v2", layout="wide")

st.title("🌱 NDVI SaaS v2 - Agricultura de Precisão (FieldView Style)")

import numpy as np

if st.button("Rodar NDVI"):
    ndvi = np.random.rand(20,20)

    st.success("Saudável")
    st.info("Sem ação necessária")

# =========================
# TESTE FASTAPI
# =========================
if st.button("Rodar NDVI (Backend)"):

    response = requests.get(f"{API_URL}/ndvi")
    data = response.json()

    st.success(data["status"])
    st.info(data["recommendation"])

# =========================
# TABS
# =========================
tab1, tab2 = st.tabs(["📷 Upload NDVI", "🛰️ Sentinel + IA"])

# =========================================================
# TAB 1
# =========================================================
with tab1:

    uploaded_file = st.file_uploader(
        "Upload imagem (drone ou satélite)",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.subheader("Imagem Original")
        st.image(image, use_container_width=True)

        ndvi = calculate_ndvi(np.random.rand(10,10), np.random.rand(10,10))

        st.subheader("🌿 NDVI")
        st.image(ndvi, use_container_width=True)

        ndvi_map = create_ndvi_colored_map(ndvi)
        st_folium(ndvi_map, width=900, height=500)

        zones = generate_vra_map(ndvi)
        df = export_vra_csv(zones)

        st.subheader("📦 VRA")
        st.dataframe(df)

# =========================================================
# TAB 2
# =========================================================
with tab2:

    st.header("🛰️ NDVI Satélite + IA")

    if st.button("Buscar Sentinel + IA"):

        try:
            client_id = st.secrets["SENTINEL_CLIENT_ID"]
            client_secret = st.secrets["SENTINEL_CLIENT_SECRET"]

            token = get_token(client_id, client_secret)

            st.success("Conectado ao Sentinel!")

            bbox = "POLYGON((-46 -12, -46 -13, -45 -13, -45 -12, -46 -12))"

            data = search_sentinel(token, bbox, "2024-01-01", "2024-01-10")

            st.json(data)

            ndvi_fake = np.random.rand(20, 20)

            if analyze_sentinel_ndvi:
                result = analyze_sentinel_ndvi(ndvi_fake, 0.6, 27)

                st.success(result["status"])
                st.info(result["recommendation"])
            else:
                st.warning("IA não disponível")

        except Exception as e:
            st.error(f"Erro: {str(e)}")

    # =========================
    # IA AGRÍCOLA (SEPARADA)
    # =========================

    st.subheader("🧠 IA Agrícola")

    rainfall = 0.6
    temp = 27

    if st.button("Rodar IA Agrícola") and analyze_sentinel_ndvi:

        result = analyze_sentinel_ndvi(
            np.random.rand(10, 10),
            rainfall,
            temp
        )

        st.success(result["status"])
        st.info(result["recommendation"])