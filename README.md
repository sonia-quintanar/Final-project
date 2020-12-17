# Productos de Dermocosmética

![imagen_primor](https://github.com/sonia-quintanar/Final-project/blob/main/images/imagen_primor.jpg)

# Descripción del proyecto:

En este proyecto hemos obtenido los productos de la sección de dermocosmética de la página web de Primor con Web Scraping.


![imagen_primor](https://github.com/sonia-quintanar/Final-project/blob/main/images/productos_dermocosmetica.png)

Hemos obtenido la marca, el nombre y el precio de todas las páginas generando así un DataFrame que hemos exportado para importarlo posteriormente en una base de datos MySQL.

![imagen_primor](https://github.com/sonia-quintanar/Final-project/blob/main/images/MySQL.png)

El objetivo ha sido conectar la base de datos con una API creada en local usando Streamlit donde hemos realizado queries con MySQL para que nos devuelva información relevante.

La información que hemos solicitado se ha basado en la siguiente estructura:

- Obtener todos los productos y precios de una marca elegida.
- Filtrar los productos de la marca elegida anteriormente que tengan un precio menor a un precio elegido.

![imagen_primor](https://github.com/sonia-quintanar/Final-project/blob/main/images/filtro_marca_precio.png)

- Seleccionar todos los productos cosméticos para el cuidado de ojos, faciales y corporales.
- Mostrar la selección anterior de productos para realizar una compra.

![imagen_primor](https://github.com/sonia-quintanar/Final-project/blob/main/images/carrito.png)

# Mejoras del proyecto para realizar en un futuro:

Obtener todos los datos de productos de dermocosmética de otras tiendas especializadas, de supermercados y de páginas de venta online con el objetivo de mostrar los precios de un mismo producto y poder compararlos.

Así podremos saber el precio más bajo de un mismo producto y la tienda donde comprarlo.

El objetivo es conseguir un comparador de precios de productos (en tiendas físicas (especializadas o supermercados) y tiendas online para obtener siempre el precio más bajo de un producto elegido.

# Enlace a la presentación del proyecto realizada:
![presentación](https://docs.google.com/presentation/d/1YWokl0ffQ26eGZN55T5LLBXBAbiLJI3W2NINLTnJpbY/edit#slide=id.gc6f80d1ff_0_0)