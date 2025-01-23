import streamlit as st
import altair as alt
import pandas as pd

def render():
    st.title("Gráfico de Dispersión")
    st.write("Aquí está el gráfico de dispersión.")

    df = pd.read_csv("Datos/quality_life_2020.csv", sep=";")
    scatter_chart = alt.Chart(df).mark_circle().encode(
        x='Quality of Life Index', 
        y='Safety Index'
    ).properties(width=600, height=400)

    st.altair_chart(scatter_chart)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Volver a Gráfico de Caja"):
            st.session_state.page = "grafica_de_caja" 
            st.rerun()  

    with col2:
        if st.button("Ir a Inicio"):
            st.session_state.page = "inicio"  
            st.rerun()  