from enum import Enum
from datetime import datetime
from dataclasses import dataclass, field
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
   
    
    descricao: str
    valor: float
    categoria: CategoriaContas
    data: datetime
    id: int = 0


     



