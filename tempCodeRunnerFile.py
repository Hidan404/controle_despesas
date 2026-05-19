senha = input("Digite sua senha: ")
alfabeto_maiusculo = "A,B,C,D,E,F,G,H,I,J,L,M,N,O,P,Q,R,S,T,U,V,Z,Y".split(",")
ALFABETO = alfabeto_maiusculo

def validar_senha():
    if len(senha) >= 8 and senha.isalnum():
        for a in alfabeto_maiusculo:
            for l in senha:
                if l in a:
                    return "Forte"

print(validar_senha())
