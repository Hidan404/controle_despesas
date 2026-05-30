import itertools
import json
from pathlib import Path
from controle_despesas.models.despesa import Despesas, CategoriaContas
import datetime



class ContasSalvarArquivoJson:
    def __init__(self, nome_arquivo):
        self.caminho = Path(__file__).parent.parent.resolve() / f"data/{nome_arquivo}"

    def _proximo_id(self):
        dados = self.ler_arquivo()
        if not dados:
            return 1
        return max(d.id for d in dados) + 1
    

    def salvar_no_arquivo(self, despesa: Despesas):
        despesas_antigas = self.ler_arquivo()    
        despesas_antigas.append(despesa)
        
        if despesa.id == 0:
            despesa.id = self._proximo_id()

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
                
                
                data_objeto = datetime.datetime.fromisoformat(item["data"])

                despesa = Despesas(
                    descricao=item["descricao"],
                    valor=item["valor"],
                    categoria=categoria_objeto,
                    data=data_objeto
                )

                despesa.id = item["id"]

                lista_dados.append(despesa)    

                

            return lista_dados    

        except json.JSONDecodeError as j:
            print(f"Erro: ler1 {j}")
            return []
        except Exception as e:
            print(f"Erro: ler2 {e}")
            return []


    def deletar_id_arquivo(self,id_deletar):
        dados = self.ler_arquivo()
        indice_encontrado = None

        for i, d in enumerate(dados):
            if d.id == id_deletar:
                indice_encontrado = i
                break

        if indice_encontrado is not None:
            dados.pop(indice_encontrado)
            
            dados_para_salva = []
            for d in dados:
                dados_para_salva.append({
                    "descricao": d.descricao,
                    "valor": d.valor,
                    "categoria": d.categoria.value,
                    "data": d.data.isoformat()
                })

            
            with open(self.caminho, "w", encoding="utf-8") as f:
                json.dump(dados_para_salva, f, ensure_ascii=False, indent=4)
                print("dados deletados e atualizados com sucesso")    
           






if __name__ == "__main__":
    
    c = ContasSalvarArquivoJson("dados.json")
    
   
    nova_despesa = Despesas(
        descricao="Conta de gas",
        valor=199.90,
        categoria=CategoriaContas.GAS,
        data=datetime.datetime.now()
    )
    
    
    c.salvar_no_arquivo(nova_despesa)
    
   
    dados_carregados = c.ler_arquivo()
    print("\n--- Conteúdo Atual do Arquivo JSON ---")
    for d in dados_carregados:
        print(f"ID: {d.id} | {d.descricao} | R$ {d.valor} | {d.categoria.name} | {d.data.strftime('%d/%m/%Y')}")
        

    #c.deletar_id_arquivo(2)    