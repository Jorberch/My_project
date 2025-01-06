import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') #leer el dataframe
st.header("Análisis Exploratorio de Vehículos") #Crear encabezado
st.write("Vista previa del conjunto de datos:") #vista previa de datos
st.write(car_data.head())

# Crear un botón para generar un histograma
if st.button('Creación de un histograma para el conjunto de datos de anuncios de venta de coches'):
    fig = px.histogram(car_data, x='odometer', nbins=50, title='Distribución de Precios de los Vehículos')
    # Mostrar el gráfico en la aplicación
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para generar un gráfico de dispersión
if st.button("Mostrar Diagrama de Dispersión (Millaje vs Precio)"):
    # Construir el gráfico de dispersión
    fig_1 = px.scatter(car_data, x='odometer', y='price', 
                     title='Relación entre Millaje y Precio',
                     labels={'odometer': 'Millaje', 'price': 'Precio'},
                     color='condition')
    # Mostrar el gráfico en la aplicación
    st.plotly_chart(fig_1)

# Casilla de verificación para el histograma
if st.checkbox("Mostrar Histograma de Precios"):
    # Construir el histograma
    fig_2= px.histogram(car_data, x='price', nbins=50, title='Distribución de Precios de los Vehículos')
    # Mostrar el gráfico en la aplicación
    st.plotly_chart(fig_2)

# Casilla de verificación para el gráfico de dispersión
if st.checkbox("Mostrar Diagrama de Dispersión (Millaje vs Precio)"):
    # Construir el gráfico de dispersión
    fig_3 = px.scatter(car_data, x='odometer', y='price', 
                     title='Relación entre Millaje y Precio',
                     labels={'odometer': 'Millaje', 'price': 'Precio'},
                     color='condition')
    # Mostrar el gráfico en la aplicación
    st.plotly_chart(fig_3)

# Construir el gráfico Distribución de precios por condición, tipo y modelo
    fig_dist = px.sunburst(car_data,
                           path=["condition", "type", "model"],
                           values="price",
                           color="condition",
                           title="Distribución de precios por condición, tipo y modelo",
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig_dist)