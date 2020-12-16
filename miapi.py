import streamlit as st
from PIL import Image
from tools.getdata import data, listadodemarcas, marca_seleccionada, listadodeprecios, precio_seleccionado, marca_precio, data_ojos
st.markdown("<h1 style='text-align: center; color: black;'>¿Cómo encontrar mi producto con el precio más bajo?</h1>", unsafe_allow_html=True)

image = Image.open('images/imagen_primor.jpg')
st.image (image,use_column_width=True)
st.write(
"""
En este proyecto extraemos con Web Scraping los productos de la sección de Dermocosmética dentro de Parafarmacia de la página de [Primor.](https://www.primor.eu/66-dermocosmetica) 

Alojamos los datos obtenidos en MySQL:
"""
)

st.dataframe(data)

#selectbox para elegir marca:
marca = st.selectbox(
    'Elige una marca:',
     listadodemarcas(data))
'Estos son los productos de la marca', marca,':'

marca_elegida = marca_seleccionada(marca)
st.dataframe(marca_elegida)


#selectbox para elegir precio < X €:
precio = st.selectbox(
    'Elige un precio (en €):',
     listadodeprecios(data))
'Estos son los productos de la marca', marca, 'con un precio inferior a', precio,'€ ordenados de menor a mayor precio:'
#precio_elegido = precio_seleccionado (precio)
#st.dataframe(precio_elegido)

marca_precio_elegido = marca_precio (marca, precio)
st.dataframe(marca_precio_elegido)


st.markdown("<h1 style='text-align: center; color: black;'>¿Mi Carrito de compra?</h1>", unsafe_allow_html=True)
# Ojos:
st.write(
"""
Los productos para mi ojos son:
"""
)

st.dataframe(data_ojos)
