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
                tipo_computador = 1 if tipo_computador == "s" else 0
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
        return tipo_computador


lista_att = []

class Analisa:
    def __init__(self, Xqt_opcoes, XvetHierarquia):
        self.qt_opcoes = Xqt_opcoes
        self.vetor = XvetHierarquia
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
                if self.Pesquisa is None or self.Pesquisa == 'LEVE':
                    self.Pesquisa = 'LEVE' 

        if self.Pesquisa is None and i == self.qt_opcoes:
            print("Foi digitado apenas N.")
            return 0
        
        return self.Pesquisa
        

def main_raiz():
    raiz = No("Raiz")
    raiz.hierarquia.extend([3, 3, 2, 1, 3, 2])
    raiz.filhos.extend([No("Navegar na Web"), No("\nPagar contas"), No("\nAssistir videos"), No("\nJogar"), No("\nUsar Pacote Office"), No("\nFazer chamadas de video")])
    qt_opcoes = 6

    a = PerguntasUsuario()
    tipo_computador =  a.escolha(raiz)

    b = Analisa(qt_opcoes, raiz.hierarquia)
    PesquisaFinal = b.analisa_vet()

    return tipo_computador, PesquisaFinal

def nova_lista(VetorProd, VetorDesem, tipo_computador, XPesquisa):
    lista_att = []
    for desempenho, produto in zip(VetorDesem, VetorProd):
        titulo = produto['titulo'].lower().strip()
        if desempenho == XPesquisa:   

            if tipo_computador == 1:
                if ('laptop' in titulo) or ('notebook' in titulo):
                    lista_att.append(produto)

            else:
                if ('pc' in titulo) or ('computador' in titulo):
                    lista_att.append(produto)
            
    return lista_att
