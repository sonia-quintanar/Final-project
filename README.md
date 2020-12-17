# tÍTULO PROJECT

![imagen_primor](https://github.com/sonia-quintanar/Final-project/blob/main/images/imagen_primor.jpg)

# Objetivo del proyecto:

En este proyecto hemos obtenido los productos de la sección de dermocosmética de la página web de Primor con Web Scraping.

![imagen_primor](https://github.com/sonia-quintanar/Final-project/blob/main/images/productos_dermocosmetica.png)

Hemos obtenido la marca, el nombre y el precio de todas las páginas de la sección mencionada anteriormente generando así un DataFrame que hemos exportado para importarlo posteriormente en una base de datos de MySQL.

![imagen_primor](https://github.com/sonia-quintanar/Final-project/blob/main/images/MySQL.png)

El siguiente objetivo, ha sido conectar la base de datos con una API creada en local usando Streamlit donde hemos realizado queries con MySQL para que nos devuelva información relevante.

La información que hemos solicitado se ha basado en la siguiente estructura:

- Obtener todos los productos y precios de una marca elegida.
- Filtrar los productos de la marca elegida anteriormente que tengan un precio menor a un precio elegido.
- Seleccionar todos los productos de ojos, faciales y corporales.
- Mostrar la selección anterior en un simulacro de carrito de compra.

# Mejoras a realizar en un futuro:

Obtener datos de productos de dermocosmética de otras tiendas especializadas, de supermercados y de páginas de venta online con el objetivo de mostrar los precios de un mismo producto. 

Así podremos saber el precio más bajo de un producto y la tienda donde comprarlo.

El objetivo es conseguir un comparador de precios de productos en tiendas físicas (especializadas o supermercados) y tiendas online para obtener siempre el precio más bajo de un producto elegido.


# Enlace a la presentación realizada:
