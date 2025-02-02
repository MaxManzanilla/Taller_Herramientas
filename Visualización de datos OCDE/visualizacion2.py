import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos/OECD.csv')

def show():
    st.title("Visualización II: Series de tiempo de la esperanza de vida")

    select_all = st.checkbox("Ver todos los países")

    if select_all:
        countries = df['Pais'].unique()  
    else:
        countries = st.multiselect("Selecciona los países:", options=df['Pais'].unique())

    if len(countries) == 0:
        st.warning("Por favor, selecciona al menos un país para comparar.")
        return

    gender_option = st.radio("Selecciona qué comparar:", ("Total", "Female", "Male"))

    years_range = st.slider("Selecciona el rango de años:", 
                            min_value=int(df['Año'].min()), 
                            max_value=int(df['Año'].max()), 
                            value=(int(df['Año'].min()), int(df['Año'].max())))

    df_filtered = df[df['Pais'].isin(countries)]
    df_filtered = df_filtered[df_filtered['Año'].between(years_range[0], years_range[1])]

    fig, ax = plt.subplots(figsize=(10, 6))
    for country in countries:
        country_data = df_filtered[df_filtered['Pais'] == country]
        ax.plot(country_data['Año'], country_data[gender_option], label=country)

    ax.set_title(f"Evolución de la esperanza de vida: {gender_option}")
    ax.set_xlabel('Año')
    ax.set_ylabel('Esperanza de vida')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

    st.pyplot(fig)
