import analise_html_classe

class No:
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []
        self.hierarquia = []


class Mensagem:
    def __init__(self):
        self.m1 = "\t\n\n### BEM-VINDO AO PROGRAMA HSBS (Hardware Suggestion Based on Software)###\n\nVou mostrar algumas opções, caso você vá usar o PC para uma dessas opções, digite s para sim ou n para não\n"
        self.m2 = "DIGITE 's' OU 'n': "
        self.m3 = "\t@@@Escolha deve ser Sim ou Nao (S ou N)!@@@"


class PerguntasUsuario:
    vetEscolha = []

    def escolha(self, raiz):
        m = Mensagem()
        X = PerguntasUsuario
        print(m.m1)

        # Adicionando pergunta sobre o tipo de computador
        while True:
            tipo_computador = input("Você está procurando laptops/notebooks? (s/n): ").lower().strip()
            if tipo_computador.isalpha() and tipo_computador in ["s", "n"]:
                X.vetEscolha.append(1 if tipo_computador == "s" else 0)
                break
            else:
                print(m.m3)

        for filho in raiz.filhos:
            print(filho.dado)

            while True:
                escolha = input(m.m2).lower().strip()

                if escolha.isalpha():
                    if escolha == "s":
                        X.vetEscolha.append(1)
                        break

                    elif escolha == "n":
                        X.vetEscolha.append(0)
                        break

                    else:
                        print(m.m3)
                else:
                    print(m.m3)


lista_att = []


class Analisa:
    def __init__(self, Xlista_produtos, Xqt_opcoes, Xvetor):
        self.lista_produtos = Xlista_produtos
        self.qt_opcoes = Xqt_opcoes
        self.vetor = Xvetor
        self.Pesquisa = None

    def analisa_vet(self):
        X = PerguntasUsuario()

        for i, escolha in enumerate(X.vetEscolha):
            if escolha == 1 and self.vetor[i] == 1:
                self.Pesquisa = 'ALTO'
                break
            elif escolha == 1 and self.vetor[i] == 2:
                self.Pesquisa = 'MEDIO'
            elif escolha == 1 and self.vetor[i] == 3:
                self.Pesquisa = 'LEVE' if self.Pesquisa is None or self.Pesquisa == 'LEVE' else self.Pesquisa

        if self.Pesquisa is None and i == self.qt_opcoes:
            print("Foi digitado apenas N.")

        return self.Pesquisa

    def nova_lista(self, Xanalisa_desempenhos, tipo_computador):
        self.analisa_desempenhos = Xanalisa_desempenhos

        for desempenho, produto in zip(self.analisa_desempenhos, self.lista_produtos):
            if desempenho == self.Pesquisa:
                # Verifica se o usuário deseja ver laptops/notebooks
                if tipo_computador == 1 and ("laptop" in produto['titulo'].lower() or "notebook" in produto['titulo'].lower()):
                    lista_att.append(produto)
                elif tipo_computador == 0 and not ("laptop" in produto['titulo'].lower() or "notebook" in produto['titulo'].lower()):
                    lista_att.append(produto)


def main_raiz(lista_produtos, analisa_desempenhos):
    raiz = No("Raiz")
    raiz.hierarquia.extend([3, 3, 2, 1])
    raiz.filhos.extend([No("Navegar na Web"), No("\nPagar contas"), No("\nAssistir videos"), No("\nJogar")])
    qt_opcoes = 4

    a = PerguntasUsuario()
    a.escolha(raiz)

    # Pega a escolha sobre laptops/notebooks
    tipo_computador = PerguntasUsuario.vetEscolha[0]

    b = Analisa(lista_produtos, qt_opcoes, raiz.hierarquia)
    b.analisa_vet()
    b.nova_lista(analisa_desempenhos, tipo_computador)

    return lista_att
