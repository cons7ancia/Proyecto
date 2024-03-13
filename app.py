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
if disp_button:
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(veh_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


pie_button = st.button('Construir grafico circular')
if pie_button:
    st.write('Creación de un grafico circular de porcentaje de precio por tipo de modelo')
    fig = px.pie(veh_data, 
             values='price', 
             names='type', 
             title='Porcentaje de precio por tipo de trasmision', 
             color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig, use_container_width=True)

bar_button = st.button('Construir grafico de barra')
if bar_button:
    st.write('Creación de un grafico de barra')
    fig = px.bar(veh_data, x="transmission", y="price", title='Precio por tipo de transmision', color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig, use_container_width=True)
