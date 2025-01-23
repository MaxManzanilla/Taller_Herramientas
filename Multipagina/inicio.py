import streamlit as st

def render():
    st.title("Bienvenido a la aplicación")

    st.write("En esta aplicación se explorarán diferentes gráficos y tablas de datos.")
    
    if st.button("Ir a Tabla de Datos"):
        st.session_state.page = "tabla_de_datos"  
        st.rerun()  
