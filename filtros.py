#CODIGO LARA
class MaisDesempenho:  # Lista de strings para pesquisa, para usuários que querem mais desempenho
    def __init__(self):
        self.SSD1 = "256GB"
        self.Icore1 = "I5"

    def teste(self):
        print("MAIS desempenho")


class MenosDesempenho:  # Lista de strings para pesquisa, para usuários que querem menos desempenho
    def __init__(self):
        self.Icore1 = "I5"
        self.Icore2 = "I3"
        self.RAM1 = "8GB"
        self.RAM2 = "6GB"
        self.SSD1 = "240GB"
        self.ARM1 = "120 GB"

    def teste2(self):
        print("MENOS desempenho")