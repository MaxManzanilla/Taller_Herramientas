import streamlit as st
import pandas as pd

df = pd.read_csv('datos/OECD.csv')

def show():
    st.title("Resumen Estadístico de la Esperanza de Vida")
    
    st.write("""
    En esta sección, puedes obtener estadísticas descriptivas sobre la esperanza de vida.
    Selecciona un año y obtendrás el promedio, desviación estándar, mínimo y máximo para los países de la OCDE y no OCDE.
    """)

    st.write("")  
    year = st.selectbox("Selecciona el año:", df['Año'].unique(), index=0)

    df_year = df[df['Año'] == year]

    st.subheader(f"Estadísticas para el año {year}")
    
    col1, col2 = st.columns([3, 1])

    with col1:
        agrupar_ocde = st.checkbox("Agrupar por OCDE", value=False)

    with col2:
        st.write("")  

    if agrupar_ocde:
        df_ocde = df_year[df_year['OCDE'].notnull()]
        
        df_ocde_grouped = df_ocde.groupby('OCDE')[['Female', 'Male', 'Total']].mean().reset_index()

        st.write(f"Promedio de esperanza de vida por grupo OCDE en {year}")
        st.table(df_ocde_grouped)

        col1, col2, col3 = st.columns(3)  
        with col1:
            st.metric(f"Promedio Female", df_ocde_grouped['Female'].mean().round(2))
            st.metric(f"Desviación estándar Female", df_ocde_grouped['Female'].std().round(2))
            st.metric(f"Mínimo Female", df_ocde_grouped['Female'].min().round(2))
            st.metric(f"Máximo Female", df_ocde_grouped['Female'].max().round(2))

        with col2:
            st.metric(f"Promedio Male", df_ocde_grouped['Male'].mean().round(2))
            st.metric(f"Desviación estándar Male", df_ocde_grouped['Male'].std().round(2))
            st.metric(f"Mínimo Male", df_ocde_grouped['Male'].min().round(2))
            st.metric(f"Máximo Male", df_ocde_grouped['Male'].max().round(2))

        with col3:
            st.metric(f"Promedio Total", df_ocde_grouped['Total'].mean().round(2))
            st.metric(f"Desviación estándar Total", df_ocde_grouped['Total'].std().round(2))
            st.metric(f"Mínimo Total", df_ocde_grouped['Total'].min().round(2))
            st.metric(f"Máximo Total", df_ocde_grouped['Total'].max().round(2))

    else:
        st.write(f"Promedio general de esperanza de vida en {year}")
        
        mean = df_year[['Female', 'Male', 'Total']].mean()
        st.write(mean)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(f"Promedio Female", mean['Female'].round(2))
            st.metric(f"Desviación estándar Female", df_year['Female'].std().round(2))
            st.metric(f"Mínimo Female", df_year['Female'].min().round(2))
            st.metric(f"Máximo Female", df_year['Female'].max().round(2))

        with col2:
            st.metric(f"Promedio Male", mean['Male'].round(2))
            st.metric(f"Desviación estándar Male", df_year['Male'].std().round(2))
            st.metric(f"Mínimo Male", df_year['Male'].min().round(2))
            st.metric(f"Máximo Male", df_year['Male'].max().round(2))

        with col3:
            st.metric(f"Promedio Total", mean['Total'].round(2))
            st.metric(f"Desviación estándar Total", df_year['Total'].std().round(2))
            st.metric(f"Mínimo Total", df_year['Total'].min().round(2))
            st.metric(f"Máximo Total", df_year['Total'].max().round(2))
