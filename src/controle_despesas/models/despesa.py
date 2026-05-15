from enum import Enum
from datetime import datetime


class CategoriaContas(Enum):
    ENERGIA = 1
    GAS = 2
    ALUGUEL = 3
    INTERNET = 4
    RECARGA_CELULAR = 5


class Despesas:
    def __init__(self, descricao, valor, categoria: CategoriaContas):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria

    def __str__(self):
        return f"Descrição: {self.descricao} | Valor: {self.valor} | Categoria: {categoria.value}"  

