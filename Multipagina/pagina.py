import streamlit as st

def load_page(page_name):
    """Carga la página correspondiente según el nombre."""
    if page_name == "inicio":
        import inicio
        inicio.render()
    elif page_name == "tabla_de_datos":
        import tabla_de_datos
        tabla_de_datos.render()
    elif page_name == "grafica_de_barras":
        import grafica_de_barras
        grafica_de_barras.render()
    elif page_name == "histograma":
        import histograma
        histograma.render()
    elif page_name == "grafica_de_caja":
        import grafica_de_caja
        grafica_de_caja.render()
    elif page_name == "grafica_de_dispersion":
        import grafica_de_dispersion
        grafica_de_dispersion.render()

def navigate():
    """Navega según la página almacenada en session_state."""
    if 'page' not in st.session_state:
        st.session_state.page = "inicio"  
    load_page(st.session_state.page)

navigate()
