from enum import Enum
from datetime import datetime
from dataclasses import dataclass
from datetime import datetime
import itertools

class CategoriaContas(Enum):
    ENERGIA = "Energia"
    GAS = "Gas"
    ALUGUEL = "Aluguel"
    INTERNET = "Internet"
    RECARGA_CELULAR = "Recarga celular"


@dataclass
class Despesas:
    _contador = itertools.count(start=1)

    id: int = field(init=False)
    descricao: str
    valor: float
    categoria: CategoriaContas
    data: datetime

    def __pos__init__(self):
        self.id = next(self._contador)

     



