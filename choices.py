#codigo Lara
import strings_list

class Node:
    def __init__(self, dado):  # Classe da arvore de escolhas
        self.dado = dado
        self.filhos = []
        self.hierarquia = []  # Vetor que hierarquiza cada nó


class Mensagem:  # Classe de mensagens que irão aparecer para o usuario
    def __init__(self):
        self.m1 = "Vou mostrar algumas opções, caso você vá usar o PC para uma dessas opções, digite s para sim ou n para não\n"  # Mensagens que estão sendo usadas no momento
        self.m2 = "Digite s ou n: "
        self.m3 = "\tEscolha deve ser Sim ou Nao (S ou N)!"


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


class Analisa:  # Classe que analisa as respostas do usuário
    def __init__(self, raiz):
        self.vetor = raiz.hierarquia

    def analisa_vet(self, lista_produtos):  # Analisa cada posição dos vetores de hierarquia e escolhas
        X = PerguntasUsuario()
        menosDesempenho = False
        maisDesempenho = False

        for i in range(len(X.vetEscolha)):

            if X.vetEscolha[i] == 1 and self.vetor[i] == 2:
                maisDesempenho = True
                break

            elif X.vetEscolha[i] == 1 and self.vetor[i] == 1:
                menosDesempenho = True
                i += 1

            elif i == 3 and maisDesempenho == False and menosDesempenho == False:
                print("Foi digitado apenas N.")

            else:
                i += 1

        if maisDesempenho == True:
            #print(strings_list.MaisDesempenho().teste())
            return strings_list.MaisDesempenho().filtroMaior(lista_produtos)

        elif menosDesempenho == True:
            #print(strings_list.MenosDesempenho())
            strings_list.MenosDesempenho()

        else:
            print("Voce apenas digitou n")


def def_raiz(lista_produtos):
    raiz = Node("Raiz")  # Nomeando nós da arvore de escolhas e hierarquizando

    no1 = Node("Navegar na Web")
    raiz.hierarquia.append(1)

    no2 = Node("Pagar contas")
    raiz.hierarquia.append(1)

    no3 = Node("Jogar")
    raiz.hierarquia.append(2)

    no4 = Node("Assistir videos")
    raiz.hierarquia.append(2)

    raiz.filhos.append(no1)  # Colocando cada nó na arvore
    raiz.filhos.append(no2)
    raiz.filhos.append(no3)
    raiz.filhos.append(no4)

    a = PerguntasUsuario()
    a.escolha(raiz)

    b = Analisa(raiz)
    return b.analisa_vet(lista_produtos)
