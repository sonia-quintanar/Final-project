import streamlit as st
from tools.getdata import data, listadodemarcas, marca_seleccionada


st.dataframe(data)

#selectbox para elegir marca

marca = st.selectbox(
    'Elige una marca:',
     listadodemarcas(data))
st.write(('Has seleccionado la marca:', marca))


marca_elegida = marca_seleccionada(marca)
st.dataframe(marca_seleccionada)
