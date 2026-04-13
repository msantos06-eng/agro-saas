# app.py
import streamlit as st

from auth import init_db, create_user, login_user
from database import init_data_tables, add_farm, get_farms
from map import generate_map
from dashboard import show_dashboard
from ai import analyze_farm
from streamlit_folium import st_folium

st.set_page_config(page_title="Agro SaaS", layout="wide")

init_db()
init_data_tables()

# ======================
# LOGIN
# ======================
st.sidebar.title("🔐 Login")

menu = st.sidebar.radio("Menu", ["Login", "Cadastro"])

if menu == "Cadastro":
    user = st.sidebar.text_input("Usuário")
    pwd = st.sidebar.text_input("Senha", type="password")

    if st.sidebar.button("Criar conta"):
        create_user(user, pwd)
        st.success("Usuário criado!")

elif menu == "Login":
    user = st.sidebar.text_input("Usuário")
    pwd = st.sidebar.text_input("Senha", type="password")

    if st.sidebar.button("Entrar"):
        if login_user(user, pwd):
            st.session_state["auth"] = True
        else:
            st.error("Login inválido")

# ======================
# APP
# ======================
if st.session_state.get("auth"):

    st.title("🌾 Agro SaaS Enterprise")

    tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🗺️ Mapa", "➕ Cadastro"])

    farms = get_farms()

    with tab1:
        show_dashboard(farms)

    with tab2:
        m = generate_map(farms)
        st_folium(m, width=900, height=500)

    with tab3:
        st.subheader("Cadastrar Fazenda")

        name = st.text_input("Nome")
        area = st.number_input("Área (ha)")
        lat = st.number_input("Latitude")
        lon = st.number_input("Longitude")

        if st.button("Salvar"):
            add_farm(name, area, lat, lon)
            st.success("Fazenda adicionada!")

        if area:
            st.info(analyze_farm(area))
else:
    st.warning("Faça login para acessar o sistema")