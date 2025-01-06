import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') #leer el dataframe
st.header("Análisis Exploratorio de Vehículos") #Crear encabezado
st.write("Vista previa del conjunto de datos:") #vista previa de datos

# Botón para mostrar la tabla
if st.button("Mostrar Tabla"):
    st.write("### Datos de los vehículos:")
    st.dataframe(car_data)



# Crear un botón para generar un histograma
if st.checkbox('Creación de un histograma para el conjunto de datos de anuncios de venta de coches'):
    fig = px.histogram(car_data, x='odometer', nbins=50, title='Distribución de Precios de los Vehículos')
    # Mostrar el gráfico en la aplicación
    st.plotly_chart(fig)

# Crear un botón para generar un gráfico de dispersión
if st.checkbox("Mostrar Diagrama de Dispersión (Millaje vs Precio)"):
    # Construir el gráfico de dispersión
    fig_1 = px.scatter(car_data, x='odometer', y='price', 
                     title='Relación entre Millaje y Precio',
                     labels={'odometer': 'Millaje', 'price': 'Precio'},
                     color='condition')
    # Mostrar el gráfico en la aplicación
    st.plotly_chart(fig_1)


# Construir el gráfico Distribución de precios por condición, tipo y modelo
fig_dist = px.sunburst(car_data,
path=["condition", "type", "model"],
values="price",
color="condition",
title="Distribución de precios por condición, tipo y modelo",
width=800,  # Ancho del gráfico
height=800,  # Altura del gráfico
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig_dist)