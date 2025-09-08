# Bibliotecas
import yfinance as yf
import pandas as pd
from sqlmodel import create_engine
from dotenv import load_dotenv
from config import env
import os


# Pegar cotação dos meus ativos
def buscar_commodities(simbolo, periodo = '5y', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period = periodo, interval = intervalo)[['Close']]
    dados['simbolo'] = simbolo
    return dados

# Concatenar os meus ativos
def buscar_todos_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_commodities(simbolo)
        todos_dados.append(dados)
    
    return pd.concat(todos_dados)


# Salvar os dados no banco
def salvar_db(df, schema='public'):
    df.to_sql('tb_commodities', con=conexao, if_exists='replace', index=True, index_label = 'Date', schema=schema)





if __name__ == "__main__":

    load_dotenv(dotenv_path=env)

    db_host = os.getenv('DB_HOST_PROD')
    db_port = os.getenv('DB_PORT_PROD')
    db_name = os.getenv('DB_NAME_PROD')
    db_user = os.getenv('DB_USER_PROD')
    db_pass = os.getenv('DB_PASS_PROD')
    db_schema = os.getenv('DB_SCHEMA_PROD')


    print(db_host)

    # Conectando ao banco
    database_url = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
    engine = create_engine(database_url)
    conexao = engine.connect()

    commodities = ['CL=F', 'GC=F', 'SI=F']
    dados_concatenados = buscar_todos_commodities(commodities)
    salvar_db(dados_concatenados)



    