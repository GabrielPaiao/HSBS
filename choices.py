class node:
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []
    
class maisDesempenho(node):
    def __init__(self, dado):
        super().__init__(dado)
        self.dado = dado

class menosDesempenho(node):
    def __init__(self, dado):
        super().__init__(dado)
        self.dado = dado
    
class mensagem:
    def __init__(self):
        self.m1 = "Vou mostrar algumas opções, caso você vá usar o PC para uma dessas opções, digite s para sim ou n para não\n"
        self.m2 = "Digite s ou n: "
        self.m3 = "Caractere invalido! Digite s ou n"

raiz = node("Raiz")
no1 = menosDesempenho("Navegar na Web")
no2 = menosDesempenho("Pagar contas")
no3 = maisDesempenho("Jogar")
no4 = maisDesempenho("Assistir videos")
raiz.filhos.append(no1)
raiz.filhos.append(no2)
raiz.filhos.append(no3)
raiz.filhos.append(no4)


m = mensagem()
print(m.m1)
n = 0
vetEscolha = []
escolha = 'a'
for filho in raiz.filhos:
    print(filho.dado)
    escolha = input(m.m2)
    if escolha == "s" or escolha == "S":
        vetEscolha.append(1)
        n += 1
        
    elif escolha == "n" or escolha == "N":
        vetEscolha.append(0)
        n +=1
        
    else:
        print(m.m3)