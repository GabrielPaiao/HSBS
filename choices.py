#codigo Lara
import strings_list

class Node:
    def __init__(self, dado):  # Classe da arvore de escolhas
        self.dado = dado
        self.filhos = []
        self.hierarquia = []  # Vetor que hierarquiza cada nó

    def adicionaFilhos(self, valor):
        novo_filho = Node(valor)
        self.filhos.append(novo_filho)


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


class Analisa:  # Classe que analisa as respostas do usuário
    def __init__(self, raiz):
        self.vetor = raiz.hierarquia

    def analisa_vet(self, lista_produtos):  # Analisa cada posição dos vetores de hierarquia e escolhas
        X = PerguntasUsuario()
        menosDesempenho = False
        maisDesempenho = False

        for i in range(len(X.vetEscolha)):  #Percorre todo o vetor de saida de escolhas do usuario

            if X.vetEscolha[i] == 1 and self.vetor[i] == 2:  #Se a saida for 1 e o numero de hierarquia for 2, a saida é mais desempenho true
                maisDesempenho = True
                break

            elif X.vetEscolha[i] == 1 and self.vetor[i] == 1:  #Se a saida for 1 e o numero de hierarquia for 1, a saida é menos desempenho true
                menosDesempenho = True
                i += 1

            elif i == 3 and maisDesempenho == False and menosDesempenho == False:
                print("Foi digitado apenas N.")

            else:
                i += 1

        if maisDesempenho == True:  
            return strings_list.MaisDesempenho().filtroMaior(lista_produtos)  #Se precisar de mais desempenho então executa a função filtroMaior

        elif menosDesempenho == True:
            return strings_list.MenosDesempenho().filtroMenor(lista_produtos)  #Se precisar de menos desempenho então executa a função filtroMenor

        else:
            print("Voce apenas digitou n")


def def_raiz(lista_produtos):
    raiz = Node("Raiz")  # Nomeando nós da arvore de escolhas e hierarquizando

    no1 = Node("Navegar na Web")
    raiz.hierarquia.append(1)

    no2 = Node("\nPagar contas")
    raiz.hierarquia.append(1)

    no3 = Node("\nJogar")
    raiz.hierarquia.append(2)

    no4 = Node("\nAssistir videos")
    raiz.hierarquia.append(2)

    raiz.filhos.append(no1)  # Colocando cada nó na arvore
    raiz.filhos.append(no2)
    raiz.filhos.append(no3)
    raiz.filhos.append(no4)

    a = PerguntasUsuario()
    a.escolha(raiz)

    b = Analisa(raiz)
    return b.analisa_vet(lista_produtos)