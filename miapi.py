import streamlit as st
from PIL import Image
from tools.getdata import data, listadodemarcas, marca_seleccionada

st.markdown("<h1 style='text-align: center; color: black;'>¿Cómo encontrar mi producto con el precio más bajo?</h1>", unsafe_allow_html=True)

image = Image.open('images/imagen_primor.jpg')
st.image (image,use_column_width=True)
st.write(
"""
En este proyecto extraemos con Web Scraping los productos de la sección de Dermocosmética dentro de Parafarmacia de la página de [Primor.](https://www.primor.eu/66-dermocosmetica) Alojamos los datos obtenidos en MySQL.
"""
)

st.dataframe(data)

#selectbox para elegir marca

marca = st.selectbox(
    'Elige una marca:',
     listadodemarcas(data))
st.write(('Has seleccionado la marca:', marca))


marca_elegida = marca_seleccionada(marca)
st.dataframe(marca_seleccionada)


#selectbox para elegir precio < 15 €

precio = st.selectbox(
    'Elige un precio:',
     listadodeprecios(data))
st.write(('Tu precio elegido es:', precio))

precio_elegido = precio_seleccionado(precio)
st.dataframe(precio_seleccionado)