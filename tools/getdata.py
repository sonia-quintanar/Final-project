from sqlalchemy import create_engine, inspect
from dotenv import load_dotenv, find_dotenv
import os 
import pandas as pd
load_dotenv()


user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PWD")

database = 'Primor'
mysql_url = f'mysql://{user}:{password}@localhost/{database}'
engine = create_engine(mysql_url)
conn = engine.connect()
inspector = inspect(engine)


query = "SELECT * FROM Dermocosmética"
res = conn.execute(query)
data = pd.DataFrame(res, columns=[field['name'] for field in inspector.get_columns('Dermocosmética')])

# Marcas:
def listadodemarcas(df):
    listado_marcas = []
    marcas = df["Marca"].tolist()
    marcas
    listado_marcas_set = set(marcas)
    listado_marcas = list(listado_marcas_set) 
    return listado_marcas

def marca_seleccionada(marca):
    query = f"SELECT * FROM Dermocosmética WHERE Marca='{marca}' ORDER BY Precio DESC;"
    res = conn.execute(query)
    data = pd.DataFrame(res, columns=[field['name'] for field in inspector.get_columns('Dermocosmética')])
    return data


# Precios:
def listadodeprecios(df):
    precios = ["5","10","20","30","40","50"]
    precios_set = set(precios)
    listado_precios = list(precios_set) 
    return listado_precios


def precio_seleccionado(precio):
    query = f"SELECT * FROM Dermocosmética WHERE Precio < {precio};"
    res = conn.execute(query)
    data = pd.DataFrame(res, columns=[field['name'] for field in inspector.get_columns('Dermocosmética')])
    return data


def marca_precio(marca, precio):
    query = f"SELECT * FROM Dermocosmética WHERE Marca='{marca}' AND Precio <{precio} ORDER BY Precio ASC;"
    res = conn.execute(query)
    data = pd.DataFrame(res, columns=[field['name'] for field in inspector.get_columns('Dermocosmética')])
    return data

# Ojos:

palabra = "Ojos"
query = f"SELECT * FROM Dermocosmética WHERE Nombre LIKE '%%{palabra}%%' order by Precio DESC;"
res = conn.execute(query)
data_ojos = pd.DataFrame(res, columns=[field['name'] for field in inspector.get_columns('Dermocosmética')])


