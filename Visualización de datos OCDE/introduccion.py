import streamlit as st
import pandas as pd

df = pd.read_csv('datos/OECD.csv')

def show():
    st.title("Introducción a los Datos de Esperanza de Vida")
    st.write(f"""
    Este conjunto de datos contiene información sobre la esperanza de vida en países pertenecientes y no pertenecientes a la OCDE.
    La fuente de los datos proviene de la Organización para la Cooperación y el Desarrollo Económicos (OCDE), abarcando desde el 2015 hasta el 2023, proporcionando una visión global de la evolución de la esperanza de vida en todos los países listados.

    Los datos están organizados por país y año, y incluyen las  categorías:
    - **Esperanza de vida total**: Promedio hombres y mujeres.
    - **Esperanza de vida para hombres**: Datos específicos para el género masculino.
    - **Esperanza de vida para mujeres**: Datos específicos para el género femenino.

    En cuanto a los países, la mayoria están clasificados como miembros de la OCDE y una minoria no. Los países miembros de la OCDE están identificados con el valor "OCDE" en la columna correspondiente, mientras que los países no miembros tienen el valor "No OCDE".

    La información de este conjunto de datos abarca un total de **{df['Pais'].nunique()} países**.
    """)
