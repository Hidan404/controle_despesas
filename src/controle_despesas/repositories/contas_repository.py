import json
from pathlib import Path
from controle_despesas.models.despesa import CategoriaContas


class ContasSalvarArquivoJson:
    def __init__(self, nome_arquivo):
        self.caminho = Path(__file__).parent.resolve() / f"{nome_arquivo}"

    def salvar_no_arquivo(self, descricao: string, valor: float, categoria: CategoriaContas):
        dados_existentes = self.ler_arquivo()    

        dados_novos = {
            "descrição": descricao,
            "valor": valor,
            "categoria": categoria
        }

        dados_existentes.append(dados_novos)
        try:
            with open(self.caminho, "w", encoding="utf-8") as f:
                return json.dumps(dados_existentes,f, ensure_ascii=False, indent=4)
        except json.JSONDecodeError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro: {e}")            

    def ler_arquivo(self):
        if self.caminho.is_file():
            try:
                with open(self.caminho, "r") as file:
                     return json.load(file)
            except json.JSONDecodeError as e:
                print(f"Erro: {e}")
                return []
        return []        


