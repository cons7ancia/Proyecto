import streamlit as st
import pandas as pd
import plotly_express as px

veh_data = pd.read_csv('vehicles_us.csv')

st.header('Detalle de vehiculos')

hist_button = st.button('Construir histograma') 
        
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(veh_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir grafico de dispersion')
        
if hist_button:
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(veh_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
