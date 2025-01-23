import streamlit as st
import altair as alt
import pandas as pd

def render():
    st.title("Histograma")
    st.write("Aquí está el histograma.")

    df = pd.read_csv("Datos/quality_life_2020.csv", sep=";")
    histogram = alt.Chart(df).mark_bar().encode(
        x=alt.X('Quality of Life Index', bin=alt.Bin(maxbins=10)),
        y='count()'
    ).properties(width=600, height=400)

    st.altair_chart(histogram)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Volver a Gráfica de Barras"):
            st.session_state.page = "grafica_de_barras"  
            st.rerun()  

    with col2:
        if st.button("Ir a Gráfica de Caja"):
            st.session_state.page = "grafica_de_caja"  
            st.rerun()  
