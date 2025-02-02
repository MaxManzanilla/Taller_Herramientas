import streamlit as st
import introduccion
import resumenEST
import visualizacion1
import visualizacion2

st.sidebar.title("Menú")
selection = st.sidebar.radio("Selecciona una página:", ["Introducción", "Resumen Estadístico", "Visualización I", "Visualización II"])

if selection == "Introducción":
    introduccion.show()
elif selection == "Resumen Estadístico":
    resumenEST.show()
elif selection == "Visualización I":
    visualizacion1.show()
else:
    visualizacion2.show()
