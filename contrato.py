from pydantic import BaseModel, EmailStr, PositiveInt, PositiveFloat
from enum import Enum

from datetime import datetime
from typing import Tuple

class ProdutoEnum(str, Enum):
    produto1 = 'ZapFlow com Gemini'
    produto2 = 'ZapFlow com chatGPT'
    produto3 = 'ZapFlow com Llama3.0'


class Vendas(BaseModel):
    '''
    Modelo de dados para as vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        produto (PositiveInt): nome do produto
        quantidade (PositiveInt): quantidade de produtos
        produto (ProdutoEnum): categoria do produto
    '''
    email: EmailStr
    data_hora: datetime
    valor: PositiveFloat
    qtd: PositiveInt
    produto: ProdutoEnum