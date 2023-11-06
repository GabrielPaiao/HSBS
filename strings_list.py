#CODIGO LARA
class MaisDesempenho:  # Lista de strings para pesquisa, para usuários que querem mais desempenho
    def __init__(self):
        self.SSD1 = "256GB" #Copiar a mesma esctrutura de filtro menor para suportar mais peças
        self.Icore1 = "I5"

    def filtroMaior(self, lista_produtos):
        nova_lista = []
        for item in lista_produtos:  #Realiza pesquisa na lista de computadores
            if '256GB' in item['titulo'].lower() or 'i5' in item['titulo'].lower():
                nova_lista.append({'titulo': item['titulo'], 'preco': item['preco']})
        return nova_lista
    
class MenosDesempenho:  # Lista de strings para pesquisa, para usuários que querem menos desempenho
    def __init__(self):
        self.Icore1 = "I5"
        self.Icore2 = "I3"
        self.RAM1 = "8GB"
        self.RAM2 = "6GB"
        self.SSD1 = "240GB"
        self.ARM1 = "120 GB"


    def filtroMenor(self, lista_produtos):  
        vetor_strings = [self.Icore1, self.Icore2, self.RAM1, self.RAM2, self.SSD1, self.ARM1]  #Lista de peças para pesquisa

        nova_lista = []
        
        for i in vetor_strings:  
            for item in lista_produtos:  #Realiza pesquisa na lista de computadores
                if i.lower() in item['titulo'].lower():
                    nova_lista.append({'titulo': item['titulo'], 'preco': item['preco']})
                    break
        return nova_lista
