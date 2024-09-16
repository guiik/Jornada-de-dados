import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os
from sqlalchemy import select, bindparam

# Carregando as variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv('DB_HOST') #aqui estamos pegando as mesmas variáveis de ambiente que estão no arquivo .env
DB_NAME = os.getenv('DB_NAME') 
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

def salvar_no_postgres(dados: Vendas):
    """Função para salvar os dados no banco de dados PostgreSQL."""
    try:
        conn = psycopg2.connect( #aqui estamos criando a conexão com o banco de dados
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor() #cursor é uma sequencia de insersão no banco de dados
        
        #inserção de dados no banco de dados
        insert_query = sql.SQL('''
            INSERT INTO vendas (email, data_hora, valor, qtd, produto)
            VALUES (%s, %s, %s, %s, %s)
        ''')
        cursor.execute(insert_query, (
            dados.email, 
            dados.data_hora, 
            dados.valor, 
            dados.qtd, 
            dados.produto))
        
        conn.commit() #aqui estamos confirmando a inserção dos dados no banco de dados
        cursor.close() #aqui estamos fechando o cursor
        conn.close() #aqui estamos fechando a conexão com o banco de dados
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f'Erro ao salvar no banco de dados: {e}')
        return   
