# Bibliotecas
import sys
import os
import pandas as pd
import streamlit as st
from sqlmodel import create_engine
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.config import env



# Conectando ao banco
load_dotenv(dotenv_path=env)

db_host = os.getenv('DB_HOST_PROD')
db_port = os.getenv('DB_PORT_PROD')
db_name = os.getenv('DB_NAME_PROD')
db_user = os.getenv('DB_USER_PROD')
db_pass = os.getenv('DB_PASS_PROD')
db_schema = os.getenv('DB_SCHEMA_PROD')

database_url = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
engine = create_engine(database_url)
conexao = engine.connect()


# Pegando os dados
def get_data():
    query = """
        select 
            *
        from public.dm_commodities;
        """
    
    df = pd.read_sql(query, con = conexao)

    return df

# Configurar a página do Streamlit
st.set_page_config(page_title = "Dashboard de Commodities", layout = 'wide')

# Titulo do Dash
st.title('Dashboard de Commodities')

# Descricao
st.write("""
         Este dashboard mostra os dados de commodities e suas transações
         """)

# Obter os dados
df = get_data()

st.dataframe(df)