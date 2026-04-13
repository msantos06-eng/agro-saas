# dashboard.py
import streamlit as st
import pandas as pd

def show_dashboard(farms):
    st.subheader("📊 Dashboard Agro SaaS")

    if not farms:
        st.info("Nenhuma fazenda cadastrada")
        return

    df = pd.DataFrame(farms, columns=["ID","Nome","Área","Lat","Lon"])

    st.metric("Total Fazendas", len(df))
    st.metric("Área Total (ha)", df["Área"].sum())

    st.bar_chart(df.set_index("Nome")["Área"])