#codigo Lara
import analise_html_classe

class No:
    def __init__(self, dado):  # Classe da arvore de escolhas
        self.dado = dado
        self.filhos = []
        self.hierarquia = []  # Vetor que hierarquiza cada nó


class Mensagem:  # Classe de mensagens que irão aparecer para o usuario
    def __init__(self):
        self.m1 = "\t\n\n### BEM-VINDO AO PROGRAMA HSBS (Hardware Suggestion Based on Software)###\n\nVou mostrar algumas opções, caso você vá usar o PC para uma dessas opções, digite s para sim ou n para não\n"  # Mensagens que estão sendo usadas no momento
        self.m2 = "DIGITE 's' OU 'n': "
        self.m3 = "\t@@@Escolha deve ser Sim ou Nao (S ou N)!@@@"


class PerguntasUsuario:  # Classe que imprime e recebe informações
    vetEscolha = []

    def escolha(self, raiz):  # Função que imprime e recebe informações
        m = Mensagem()
        X = PerguntasUsuario
        print(m.m1)
        
        for filho in raiz.filhos:  # Inicio do laço de perguntas para o usuário
            print(filho.dado)

            while True:
                escolha = input(m.m2).lower().strip()

                if escolha.isalpha():
                    if escolha == "s":
                        X.vetEscolha.append(1)  # Adiciona 1 no vetor usado para pesquisa de peças
                        break

                    elif escolha == "n":
                        X.vetEscolha.append(0)  # Adiciona 0 no vetor usado para pesquisa de peças
                        break

                    else:
                        print(m.m3)
                else:
                    print(m.m3)

lista_att = []
 # Usado para calcular o desempenho (Alto, Medio e Leve)
class Analisa:  # Classe que analisa as respostas do usuário
    def __init__(self, Xlista_produtos, Xqt_opcoes, Xvetor):
        self.lista_produtos = Xlista_produtos
        self.qt_opcoes = Xqt_opcoes
        self.vetor = Xvetor
        self.Pesquisa = None
    def analisa_vet(self):  # Analisa cada posição dos vetores de hierarquia e escolhas
        X = PerguntasUsuario()
        
        for i in range(len(X.vetEscolha)):  #Percorre todo o vetor de saida de escolhas do usuario

            if X.vetEscolha[i] == 1 and self.vetor[i] == 1:  #Se a saida for S e o numero de hierarquia for 1, então, saida é desempenho alto 
                self.Pesquisa = 'ALTO'
                break

            elif X.vetEscolha[i] == 1 and self.vetor[i] == 2:  #Se a saida for 1 e o numero de hierarquia for 2, a saida é desempenho médio
                self.Pesquisa = 'MEDIO'
                i += 1
            
            elif X.vetEscolha[i] == 1 and self.vetor[i] == 3:  #Se a saida for 1 e o numero de hierarquia for 3, a saida é desempenho leve
                if self.Pesquisa == None or self.Pesquisa == 'LEVE':
                    self.Pesquisa = 'LEVE'
                    i += 1

                else:
                    i += 1

            elif i == self.qt_opcoes and self.Pesquisa == '':
                print("Foi digitado apenas N.") 

            else:
                i += 1
        return self.Pesquisa
    
    def nova_lista(self, Xanalisa_desempehos):
        self.analisa_desempenhos = Xanalisa_desempehos
        i = 0

        for desempenho in self.analisa_desempenhos:
            if desempenho == self.Pesquisa:
                x = self.lista_produtos[i]
                lista_att.append(x)
            i += 1

def main_raiz(lista_produtos, analisa_desempenhos):
    raiz = No("Raiz")  # Nomeando nós da arvore de escolhas e hierarquizando

    no1 = No("Navegar na Web")
    raiz.hierarquia.append(3)      # Hierarquia 3 = Desempenho Leve
                                                
    no2 = No("\nPagar contas")
    raiz.hierarquia.append(3)

    no3 = No("\nAssistir videos")    # Hierarquia 2 = Desempenho Medio
    raiz.hierarquia.append(2)

    no4 = No("\nJogar")              # Hierarquia 1 = Desempenho Alto
    raiz.hierarquia.append(1)

    qt_opcoes = 4

    raiz.filhos.append(no1)  # Colocando cada nó na arvore
    raiz.filhos.append(no2)
    raiz.filhos.append(no3)
    raiz.filhos.append(no4)

    a = PerguntasUsuario()
    a.escolha(raiz)

    b = Analisa(lista_produtos, qt_opcoes, raiz.hierarquia)
    b.analisa_vet()
    b.nova_lista(analisa_desempenhos)
    return lista_att