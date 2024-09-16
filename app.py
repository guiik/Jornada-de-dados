import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import salvar_no_postgres

def main ():
    st.title('Sistema de CRM e Vendas da ZapFlow - Fronted Semples')
    email = st.text_input(' Campo de texto para inserção do email do vendedor.')
    data = st.date_input('Campo para selecionar a data em que a venda foi realizada.')
    hora = st.time_input('Campo para selecionar o horário em que a venda foi realizada.')
    valor = st.number_input('Campo para inserir o valor da venda realizada.', min_value=0.0, format='%2f')
    qtd = st.number_input('Campo numérico para inserir a quantidade de produtos vendidos')
    produto = st.selectbox('Campo para selecionar o produto vendido', ['ZapFlow com Gemini', 'ZapFlow com chatGPT', 'ZapFlow com Llama3.0'])

    if st.button('salvar'):
        try:
            data_hora = datetime.combine(data, hora)

            # venda  instanciando da minha classe Vendas

            venda = Vendas(
                email=email, 
                data_hora=data_hora, 
                valor=valor, 
                qtd=qtd, 
                produto=produto
            )

            st.write('venda')
            salvar_no_postgres(venda)

        except ValidationError as e:
            st.error(f'Erro de validação: {e}')
            return
        

if __name__ == '__main__':
    main()