import json
from pathlib import Path
from controle_despesas.models.despesa import Despesas, CategoriaContas
import datetime



class ContasSalvarArquivoJson:
    def __init__(self, nome_arquivo):
        self.caminho = Path(__file__).parent.parent.resolve() / f"data/{nome_arquivo}"

    def salvar_no_arquivo(self,despesa: Despesas):
        dados_existentes = self.ler_arquivo()    

        dados_novos = {
            "id": despesa.id,
            "descrição": despesa.descricao,
            "valor": despesa.valor,
            "categoria": despesa.categoria.value,
            "data": despesa.data.isoformat()
        }

        dados_existentes.append(dados_novos)
        try:
            with open(self.caminho, "w", encoding="utf-8") as f:
                json.dump(dados_existentes,f, ensure_ascii=False, indent=4)
        except json.JSONDecodeError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro: {e}")            

    def ler_arquivo(self):
        if not self.caminho.is_file():
            return []
        
        try:
            with open(self.caminho, "r",encoding="utf-8") as f:
                dados = json.load(f)

            lista_dados = []
            for item in dados:
                categoria_objeto = CategoriaContas(item["categoria"])
                data_objeto

        except json.JSONDecodeError as j:
            print(f"Erro: {j}")
            return []
        except Exception as e:
            print(f"Erro: {e}")
            return []
                


c = ContasSalvarArquivoJson()
c.salvar_no_arquivo