from enum import Enum
from datetime import datetime


class CategoriaContas(Enum):
    ENERGIA = "Energia"
    GAS = "Gas"
    ALUGUEL = "Aluguel"
    INTERNET = "Internet"
    RECARGA_CELULAR = "Recarga celular"


class Despesas:
    def __init__(self, descricao, valor, categoria: CategoriaContas):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria

    def __str__(self):
        return f"Descrição: {self.descricao} | Valor: {self.valor} | Categoria: {self.categoria.value}"  



