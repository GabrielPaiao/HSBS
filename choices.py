#codigo Lara

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
    def __init__(self, dado):  #Classe da arvore de escolhas do usuario
        self.dado = dado
        self.filhos = []

class pecas_maisDesempenho: #Lista de strings para pesquisa, para usuários que querem mais desempenho
    def __init__(self):  # !Lembrar que é interessante colocar em um arquivo separado
        self.SSD1 = "256GB"

class pecas_menosDesempenho:  #Lista de strings para pesquisa, para usuários que querem menos desempenho
    def __init__(self):      
        self.Icore1 = "I5"
        self.Icore2 = "I3"
        self.RAM1 = "8GB"
        self.SSD1 = "240GB"


class mensagem:  #Classe de mensagens que irão aparecer para o usuario
    def __init__(self):
        self.m1 = "Vou mostrar algumas opções, caso você vá usar o PC para uma dessas opções, digite s para sim ou n para não\n" #Mensagens que estão sendo usadas no momento
        self.m2 = "Digite s ou n: "
        self.m3 = "\tEscolha deve ser Sim ou Nao (S ou N)!"

    def escolha(raiz):
        vetEscolha = []
        m = mensagem()
        print(m.m1)

        for filho in raiz.filhos:  #Inicio do laço de perguntas para o usuário
            print(filho.dado)

            while True:  
                escolha = input(m.m2)
                if escolha.isalpha():
                    if escolha == "s" or escolha == "S":
                        vetEscolha.append(1)
                        break
            
                    elif escolha == "n" or escolha == "N":
                        vetEscolha.append(0)
                        break
            
                    else:
                        print(m.m3)
                else:
                    print(m.m3)
        
        if vetEscolha[2] == 1 or vetEscolha[3] == 1:
            a = pecas_maisDesempenho()

        else:
            a = pecas_menosDesempenho()
            

raiz = node("Raiz")  #Nomeando nós da arvore de escolhas
no1 = node("Navegar na Web")
no2 = node("Pagar contas")
no3 = node("Jogar")
no4 = node("Assistir videos")

raiz.filhos.append(no1)  #Colocando cada nó na arvore
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
mensagem.escolha(raiz)
