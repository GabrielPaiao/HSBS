# codigo André e Gabriel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import math
import re
from bs4 import BeautifulSoup


def selection_sort(preco):
    def troca(preco, i, j):
        """Troca de posicoes"""
        aux = preco[i]
        preco[i] = preco[j]
        preco[j] = aux

    # Converte os preços para números, removendo pontos de milhar antes da conversão
    preco_numerico = [float(p.replace('R$', '').replace('.', '').replace(',', '.')) for p in preco]

    i = 0
    while i < len(preco_numerico) - 1:
        indice_minimo = i
        j = i + 1
        while j < len(preco_numerico):
            if preco_numerico[j] < preco_numerico[indice_minimo]:
                indice_minimo = j
            j += 1
        if indice_minimo != i:
            troca(preco_numerico, indice_minimo, i)
        i += 1

        # Converte os preços de volta para strings
    preco_formatado = [f'R${p:.2f}' for p in preco_numerico]
    #print(preco_formatado)


class ChromeScraperKabum:
    #Scraping dos produtos do site kabum
    def __init__(self):
        self.url = 'https://www.kabum.com.br/computadores/pc'
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://www.kabum.com.br/computadores/pc')
        self.driver.implicitly_wait(10)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    def scrap_pages(self):
        # analisando os produtos por pagina (20 por pagina)
        qtd_items = self.soup.find('div', id='listingCount').get_text().strip()
        index = qtd_items.find(' ')  # ache o espaço em branco
        qtd = qtd_items[:index]  # me retorna do index até o espaço em branco, deixando apenas o número de items no site
        #ultima_pagina = math.ceil(int(qtd) / 20)
        lista_produtos = []

        # for pagina in range(1, ultima_pagina + 1):
        for pagina in range(1, 3):
            url_pag = f'https://www.kabum.com.br/computadores/pc?page_number={pagina}&page_size=20&facet_filters=&sort=most_searched'
            self.driver.get(url_pag)
            self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            produtos = self.soup.find_all('div', class_=re.compile('productCard'))

            for produto in produtos:
                titulo = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
                preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()
                preco_formatado = preco.replace('\xa0', '')
                #print(f'\nPreco: R${preco}')
                lista_produtos.append({'titulo': titulo, 'preco': preco_formatado})

        self.driver.quit() #saindo....
        return lista_produtos #retorna lista de dicionario

if __name__ == "__main__":
    url = 'https://www.kabum.com.br/computadores/pc'
    scraper = ChromeScraperKabum()
    lista = scraper.scrap_pages()
    lista_precos = [item['preco'] for item in lista]
    #print("### PRECOS ###\n")
    selection_sort(lista_precos)
