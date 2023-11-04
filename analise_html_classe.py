#codigo GABRIEL PEREIRA PAIAO
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import math
import re
from bs4 import BeautifulSoup
from choices import mensagem

class ChromeScraper:
    def __init__(self, url):
        self.url = url
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options = self.options)
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
    
    def scrape_pages(self):
        #analisando os produtos por pagina (20 por pagina)
        qtd_items = self.soup.find('div', id='listingCount').get_text().strip()
        index = qtd_items.find(' ') #ache o espaço em branco
        qtd = qtd_items[:index] #me retorna do index até o espaço em branco, deixando apenas o número de items no site
        ultima_pagina = math.ceil(int(qtd)/20)
        lista_produtos = []

        #for pagina in range(1, ultima_pagina + 1):
        for pagina in range(1, 3):
            url_pag = f'{self.url}?page_number={pagina}&page_size=20&facet_filters=&sort=most_searched'
            self.driver.get(url_pag)
            self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            produtos = self.soup.find_all('div', class_=re.compile('productCard'))

            for produto in produtos:
                titulo = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
                preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()
                preco_formatado = preco.replace('\xa0', '')
                print(f'Titulo: {titulo}\nPreco: R${preco}')
                lista_produtos.append({'titulo': titulo, 'preco': preco_formatado})

        self.driver.quit()
        return lista_produtos

if __name__ == "__main__":
    url = 'https://www.kabum.com.br/computadores/pc'
    scraper = ChromeScraper(url)
    lista = scraper.scrape_pages()
    for item in lista:
        print(item)
    #for item in dicionario:
    #    print(item)