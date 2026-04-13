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