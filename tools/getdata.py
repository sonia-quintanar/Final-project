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


#Una función que de el dataframe te de solamente columna Marcas sin repetir
def funcionquehacequery(marca)
    query = "SELECT * FROM Dermocosmética WHERE {marca}"
    de