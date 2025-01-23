import streamlit as st
import altair as alt
import pandas as pd

def render():
    st.title("Gráfica de Barras")
    st.write("Aquí está el gráfico de barras.")

    
    df = pd.read_csv("Datos/quality_life_2020.csv", sep=";")
    chart = alt.Chart(df).mark_bar().encode(
        x='Country', 
        y='Quality of Life Index'
    ).properties(width=600, height=400)
    
    st.altair_chart(chart)

    
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Volver a Tabla de Datos"):
            st.session_state.page = "tabla_de_datos"  
            st.rerun()  

    with col2:
        if st.button("Ir a Histograma"):
            st.session_state.page = "histograma"
            st.rerun()  
