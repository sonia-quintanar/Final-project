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


def listadodemarcas(df):
    listado_marcas = []
    marcas = df["Marca"].tolist()
    marcas
    listado_marcas_set = set(marcas)
    listado_marcas = list(listado_marcas_set) 
    return listado_marcas

def marca_seleccionada(df):
    query = f"SELECT * FROM Dermocosmética WHERE Marca={marca}"
    res = conn.execute(query)
    data = pd.DataFrame(res, columns=[field['name'] for field in inspector.get_columns('Democosmética')])
    return data

    #query = f"SELECT Marca FROM Dermocosmética WHERE Marca, Precio LIKE '%%{marca}%%' ORDER BY Precio
