import json
from pathlib import Path
from controle_despesas.models.despesa import Despesas, CategoriaContas
import datetime



class ContasSalvarArquivoJson:
    def __init__(self, nome_arquivo):
        self.caminho = Path(__file__).parent.parent.resolve() / f"data/{nome_arquivo}"

    def salvar_no_arquivo(self, despesa: Despesas):
        despesas_antigas = self.ler_arquivo()    
        despesas_antigas.append(despesa)

        dados_para_salvar = []
        for item in despesas_antigas:
            dados_para_salvar.append({
                "id": item.id,
                "descricao": item.descricao, 
                "valor": item.valor,
                "categoria": item.categoria.value,
                "data": item.data.isoformat()
            })

        try:
            with open(self.caminho, "w", encoding="utf-8") as f:
                json.dump(dados_para_salvar, f, ensure_ascii=False, indent=4)
            print(f"Sucesso: Dados salvos em {self.caminho}")
        except Exception as e:
            print(f"Erro ao salvar: {e}")          

    def ler_arquivo(self):
        if not self.caminho.is_file():
            return []
        
        try:
            with open(self.caminho, "r",encoding="utf-8") as f:
                dados = json.load(f)

            lista_dados = []
            for item in dados:
                categoria_objeto = CategoriaContas(item["categoria"])
                data_objeto = CategoriaContas(item["data"])

                despesa = Despesas(
                    descricao= item["descricao"],
                    valor=item["valor"],
                    categoria=categoria_objeto,
                    data=data_objeto
                )

                despesa.id = item["id"]

                lista_dados.append(despesa)

            return lista_dados    

        except json.JSONDecodeError as j:
            print(f"Erro: {j}")
            return []
        except Exception as e:
            print(f"Erro: {e}")
            return []
                



if __name__ == "__main__":
    
    c = ContasSalvarArquivoJson("dados.json")
    
   
    nova_despesa = Despesas(
        descricao="Conta de Internet Fibra",
        valor=99.90,
        categoria=CategoriaContas.INTERNET,
        data=datetime.datetime.now()
    )
    
    
    c.salvar_no_arquivo(nova_despesa)
    
   
    dados_carregados = c.ler_arquivo()
    print("\n--- Conteúdo Atual do Arquivo JSON ---")
    for d in dados_carregados:
        print(f"ID: {d.id} | {d.descricao} | R$ {d.valor} | {d.categoria.name} | {d.data.strftime('%d/%m/%Y')}")