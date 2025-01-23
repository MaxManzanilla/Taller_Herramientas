import streamlit as st
import altair as alt
import pandas as pd

def render():
    st.title("Gráfico de Caja")
    st.write("Aquí está el gráfico de caja.")

    df = pd.read_csv("Datos/quality_life_2020.csv", sep=";")
    box_plot = alt.Chart(df).mark_boxplot().encode(
        y=alt.Y('Quality of Life Index', title="Quality of Life Index")
    ).properties(width=600, height=400)

    st.altair_chart(box_plot)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Volver a Histograma"):
            st.session_state.page = "histograma" 
            st.rerun()  

    with col2:
        if st.button("Ir a Gráfico de Dispersión"):
            st.session_state.page = "grafica_de_dispersion"  
            st.rerun()  
