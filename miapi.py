import streamlit as st
from PIL import Image
from tools.getdata import data, listadodemarcas, marca_seleccionada, listadodeprecios, precio_seleccionado, marca_precio, data_ojos, listadodeojos, ojos_seleccionada, data_cara, listadodecara, cara_seleccionada, data_corporal, listadodecorporal, corporal_seleccionada

st.markdown("<h1 style='text-align: center; color: black;'>¿Qué productos de dermocosmética vende Primor?</h1>", unsafe_allow_html=True)

image = Image.open('images/imagen_primor.jpg')
st.image (image,use_column_width=True)
st.write(
"""
En este proyecto extraemos con Web Scraping los productos de la sección de Dermocosmética dentro de Parafarmacia de la página de [Primor.](https://www.primor.eu/66-dermocosmetica) 

Alojamos los datos obtenidos en MySQL:
"""
)
st.markdown("<h1 style='text-align: center; color: black;'>Productos</h1>", unsafe_allow_html=True)

st.dataframe(data)

#selectbox para elegir marca:

st.markdown("<h1 style='text-align: center; color: black;'>Marcas</h1>", unsafe_allow_html=True)

#image = Image.open('images/imagen_marcas1.jpg')
#st.image (image,use_column_width=True)

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


marca_precio_elegido = marca_precio (marca, precio)
st.dataframe(marca_precio_elegido)


st.markdown("<h1 style='text-align: center; color: black;'>¿Realizamos un pedido? Compra los productos para tu Ojos, Cara y Cuerpo.</h1>", unsafe_allow_html=True)
# Ojos:

st.write(
"""
- Los productos para tus ojos son:
"""
)

image = Image.open('images/imagen_facial1.jpg')
st.image (image,use_column_width=True)
st.dataframe(data_ojos)

ojos = st.selectbox(
    'Elige un producto:',
     listadodeojos(data_ojos))


# Facial:

st.write(
"""
- Los productos para tu cara son:
"""
)

image = Image.open('images/imagen_facial.jpg')
st.image (image,use_column_width=True)

st.dataframe(data_cara)

cara = st.selectbox(
    'Elige un producto:',
     listadodecara(data_cara))


# Corporal:

st.write(
"""
- Tus productos corporales son:
"""
)

image = Image.open('images/imagen_corporal.jpg')
st.image (image,use_column_width=True)

st.dataframe(data_corporal)

corporal = st.selectbox(
    'Elige un producto:',
     listadodecorporal(data_corporal))

# Carrito de compra:

st.markdown("<h1 style='text-align: center; color: black;'>Ver mi Carrito de Compra</h1>", unsafe_allow_html=True)

'Tu producto para ojos elegido:'

ojos_elegida = ojos_seleccionada(ojos)
st.dataframe(ojos_elegida)


'Tu producto de cara elegido:'

cara_elegida = cara_seleccionada(cara)
st.dataframe(cara_elegida)


'Tu producto corporal elegido:'

corporal_elegida = corporal_seleccionada(corporal)
st.dataframe(corporal_elegida)

image = Image.open('images/imagen_carrito.jpg')
st.image (image,use_column_width=True)