import streamlit as st
import pandas as pd

def render():
    st.title("Tabla de Datos")
    st.write("Aquí puedes ver la tabla de datos.")

    df = pd.read_csv("Datos/quality_life_2020.csv", sep=";")
    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Volver a Inicio"):
            st.session_state.page = "inicio"  
            st.rerun()  

    with col2:
        if st.button("Ir a Gráfica de Barras"):
            st.session_state.page = "grafica_de_barras"  
            st.rerun()  
