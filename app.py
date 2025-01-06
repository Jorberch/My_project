import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') #leer el dataframe

# Asegurarse de que 'date_posted' sea de tipo datetime
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'], errors='coerce')

# Convertir 'model_year' a tipo entero, manejando NaNs con 'coerce'
car_data['model_year'] = car_data['model_year'].fillna(car_data['model_year'].mode()[0]).astype(int)

# Rellenar valores faltantes en 'cylinders' con la mediana
car_data['cylinders'] = car_data['cylinders'].fillna(car_data['cylinders'].median())

# Rellenar valores faltantes en 'odometer' con la mediana
car_data['odometer'] = car_data['odometer'].fillna(car_data['odometer'].median())

# Rellenar valores faltantes en 'paint_color' con el valor más frecuente
car_data['paint_color'] = car_data['paint_color'].fillna(car_data['paint_color'].mode()[0])

# Rellenar valores faltantes en 'is_4wd' con un valor predeterminado (por ejemplo, 0 si no se sabe si es 4WD)
car_data['is_4wd'] = car_data['is_4wd'].fillna(0)


st.header("Análisis Exploratorio de Vehículos") #Crear encabezado
st.write("Vista previa del conjunto de datos:") #vista previa de datos

# Botón para mostrar la tabla
if st.button("Mostrar Tabla"):
    st.write("### Datos de los vehículos:")
    st.dataframe(car_data)


hist_button = st.button('Construir histograma') # crear un botón
# Crear un botón para generar un histograma
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odómetro")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

# Crear un botón para generar un gráfico de dispersión
if st.checkbox("Mostrar Diagrama de Dispersión (Kilometraje vs Precio)"):
    # Construir el gráfico de dispersión
    fig_1 = px.scatter(car_data, x='odometer', y='price', 
                     title='Relación entre Kilometraje y Precio',
                     labels={'odometer': 'Odómetro', 'price': 'Precio'},
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

# Extraer el fabricante de la columna 'model'
car_data['manufacturer'] = car_data['model'].str.split().str[0]

# Crear una lista de fabricantes únicos para el cuadro de selección
manufacturers = car_data['manufacturer'].unique()

# Agregar un cuadro de selección de fabricante
selected_manufacturer = st.selectbox('Selecciona un fabricante', manufacturers)

# Filtrar los datos según el fabricante seleccionado
filtered_df = car_data[car_data['manufacturer'] == selected_manufacturer]

# Contar los tipos de vehículos por fabricante
vehicle_types = filtered_df.groupby(['manufacturer', 'type']).size().reset_index(name='count')

# Crear gráfico de barras agrupadas
fig_bar = px.bar(vehicle_types, 
             x='manufacturer', 
             y='count', 
             color='type', 
             title="Tipos de vehículos por fabricante", 
             labels={'manufacturer': 'Fabricante', 'count': 'Cantidad', 'type': 'Tipo de vehículo'}, 
             barmode='group',
             width=400,  # Ancho del gráfico
             height=400)  # Altura del gráfico)
st.plotly_chart(fig_bar)