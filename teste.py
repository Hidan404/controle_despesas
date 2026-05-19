lista = [
    {"nome": "ronald","idade": 78, "peso": 64},
    {"nome": "sabrina","idade": 35, "peso": None}
]    

#for l in lista:
#    for chave, valor in l.items():
#        print(chave, valor)



numeros = [[1,2,3],[4,5,6]]
#for n in numeros:
#    for n2 in n:
#        print(n2)        


lista_palavras = ["Sabrina", "Vanuza", "Ryan","Reginaldo"] 
#pegar as palavras que terminam com a letra A


def pegar_nomes_final_a(lista):
    lista_nova = []
    for l in lista:
        if l.endswith("a"):
            lista_nova.append(l)
    return lista_nova       
    

#print(pegar_nomes_final_a(lista_palavras))

#somar quantos produtos foi vendido durante um dia
#pegar a quantidades de produtos vindo do usuario


class SomarProdutosVendidos:
    def __init__(self):
        self.soma = 0
        self.valores_entrada= []

    def somar_produtos(self):
        condicao = True
        while condicao:
            preco_produto = float(input("Digite o preço: "))
            self.valores_entrada.append(preco_produto)

            escolha = input("Deseja parar digite\n[S] sair e [N] para continuar: ") 
            if escolha == "S":
                print("saindo...")
                for valor in self.valores_entrada:
                    self.soma+= valor
                condicao = False
            
               

        return self.soma    


#f __name__ == "__main__":
    #somarProdutos = SomarProdutosVendidos()
    #print(somarProdutos.somar_produtos())

def validar_senha(senha):

    if len(senha) < 8:
        return "Fraca"

    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(c in "!@#$%&*" for c in senha)

    if all([tem_maiuscula, tem_minuscula, tem_numero, tem_especial]):
        return "Forte"

    return "Média"
