from controle_despesas.repositories.contas_repository import ContasSalvarArquivoJson
from datetime import datetime
from controle_despesas.models.despesa import CategoriaContas, Despesas


class SerivicesDespesas:
    def __init__(self,nome_arquivo):
        self.repositorio_despesa = ContasSalvarArquivoJson(nome_arquivo)

    def adicionar_despesa(self,descricao: str, valor: float,categoria: CategoriaContas, data: datetime):
        try:

            despesa = Despesas(
                descricao= descricao,
                valor= valor,
                categoria= categoria,
                data= data
            )
            if self.validardespesa(despesa):
                return self.repositorio_despesa.salvar_no_arquivo(despesa=despesa)


        except Exception as e:
            return f"Erro: {e}"

    def validardespesa(self, despesa: Despesas):
        if not isinstance(despesa.descricao,str) or not len(despesa.descricao) > 0:
            raise ValueError("Descricao não pode ser vazia e vazia")

        if not isinstance(despesa.valor,(int, float)):
            raise ValueError("Valor tem que ser numero inteiro ou decimal")

        if not isinstance(despesa.categoria,CategoriaContas):
            raise ValueError("Categoria invalida ")

        if not isinstance(despesa.data, datetime):
            raise ValueError("Data no formato invalido") 

        return True     



if __name__ == "__main__":
    servico = SerivicesDespesas("data.json")
    servico.adicionar_despesa("como um anjo",150,CategoriaContas.INTERNET,datetime.now())        

