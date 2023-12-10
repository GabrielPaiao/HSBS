# codigo André e Gabriel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import math
import re
from bs4 import BeautifulSoup

#Nó adjacente no grafo
class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class GraphAL:
    def __init__(self, num):
        self.v = num
        self.graph = [None] * self.v

    # Adiciona uma aresta direcionada do vértice de origem 's' para o vértice de destino 'd'
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

class GraphProdutos:
    def __init__(self, produtos):
        self.grafo = None
        self.construir_grafo(produtos)
    #Constrói o grafo com base nas relações de desempenho entre os produtos
    def construir_grafo(self, produtos):
        num_vertices = len(produtos)
        grafo = GraphAL(num_vertices)

        for i in range(num_vertices):
            for j in range(i + 1, num_vertices): # Se o desempenho do produto i for maior que o desempenho do produto j,
                # adiciona uma aresta direcionada de i para j
                if produtos[i]['desempenho'] > produtos[j]['desempenho']:
                    grafo.add_edge(i, j)

        self.grafo = grafo

def selection_sort(preco):
    def troca(preco, i, j):
        """Troca de posicoes"""
        aux = preco[i]
        preco[i] = preco[j]
        preco[j] = aux

    # # Converte os preços para números, removendo pontos de milhar antes da conversão
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
    return preco_formatado

desempenhos_analisa_kabum = []
desempenhos_analisa_amazon = []

class ChromeScraperAmazon:
    def __init__(self):
        self.base_url = 'https://www.amazon.com.br/s?rh=n%3A17923695011&fs=true&pf_rd_i=17351089011&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_p=93e8fe49-3055-4d71-b202-41c439591616&pf_rd_r=J49E6BYKK92NGF72ZBTH&pf_rd_s=merchandised-search-5&ref=lp_17923695011_sar'
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)
        self.pecasMaiorDesempenho = ['RYZEN 7', 'I7', '3080','3050', '3070', '3060', 'RYZEN 9', 'I9', 'XEON', '32GB', '16GB']
        self.pecasMedioDesempenho = ['3050', '2060', '1660', '1650', 'RYZEN 7', 'I7', 'RYZEN 5', 'I5', 'CHIP M1', '8GB']
        self.pecasMenorDesempenho = ["1650", "1050", "750", "580", "570", "550", "VEGA", "PRO 555X", "INTEGRADA", "IRIS PLUS", "A10", "A8", "ATHLON", "A6", "GOLD", "CELERON"]

    def scrap_pages(self):
        lista_produtos = []
        for pagina in range(1, 3+2):
            url_pag = f'https://www.amazon.com.br/s?i=computers&rh=n%3A17923695011&fs=true&page={pagina}&pf_rd_i=17351089011&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_p=93e8fe49-3055-4d71-b202-41c439591616&pf_rd_r=J49E6BYKK92NGF72ZBTH&pf_rd_s=merchandised-search-5&qid=1702049777&ref=sr_pg_1'
            self.driver.get(url_pag)
            self.driver.implicitly_wait(10)
            self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

            produtos = self.soup.find_all('div', class_=re.compile('s-result-item s-asin'))

            for produto in produtos:
                titulo = produto.find('span', class_='a-size-base-plus a-color-base a-text-normal').get_text().strip()
                preco_element = produto.find('span', class_='a-price')
                if preco_element:
                    preco = preco_element.find('span', class_='a-offscreen').get_text().strip()
                    preco = preco.replace('\xa0', '')
                else: 
                    preco = 'Nenhuma opção de compra em destaque'
                link = produto.find('a', href = True)['href']
                link_completo = f'https://amazon.com.br/{link}'
                alto = sum(1 for peca in self.pecasMaiorDesempenho if peca in titulo.upper()) #analise desempenho
                medio = sum(1 for peca in self.pecasMedioDesempenho if peca in titulo.upper())
                leve = sum(1 for peca in self.pecasMenorDesempenho if peca in titulo.upper())
                desempenho = 'ALTO' if alto > medio > leve else ('MEDIO' if medio > alto > leve or medio == alto == leve else 'LEVE')
                
                lista_produtos.append({'titulo': titulo, 'preco': preco, 'desempenho': desempenho, 'link': link_completo})
                desempenhos_analisa_amazon.append(desempenho)
        
        self.driver.quit()
        return lista_produtos

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
        self.pecasMaiorDesempenho = ['RYZEN 7', 'I7', '3080','3050', '3070', '3060', 'RYZEN 9', 'I9', 'XEON', '32GB', '16GB']
        self.pecasMedioDesempenho = ['3050', '2060', '1660', '1650', 'RYZEN 7', 'I7', 'RYZEN 5', 'I5', 'CHIP M1', '8GB']
        self.pecasMenorDesempenho = ["1650", "1050", "750", "580", "570", "550", "VEGA", "PRO 555X", "INTEGRADA", "IRIS PLUS", "A10", "A8", "ATHLON", "A6", "GOLD", "CELERON"]

    def scrap_pages(self):
        # analisando os produtos por pagina (20 por pagina)
        qtd_items = self.soup.find('div', id='listingCount').get_text().strip()
        index = qtd_items.find(' ')  # ache o espaço em branco
        qtd = qtd_items[:index]  # me retorna do index até o espaço em branco, deixando apenas o número de items no site
        #ultima_pagina = math.ceil(int(qtd) / 20)
        lista_produtos = []

        #for pagina in range(1, ultima_pagina + 1):
        for pagina in range(1, 10):
            url_pag = f'https://www.kabum.com.br/computadores/pc?page_number={pagina}&page_size=20&facet_filters=&sort=most_searched'
            self.driver.get(url_pag)
            self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            produtos = self.soup.find_all('div', class_=re.compile('productCard'))

            for produto in produtos:
                titulo = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
                preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()
                preco_formatado = preco.replace('\xa0', '')
                link = produto.find('a', href=True)['href']  # Extrai o link do produto
                link_completo = f'https://www.kabum.com.br{link}' #tava saindo sem esse começo do link

                alto = sum(1 for peca in self.pecasMaiorDesempenho if peca in titulo.upper()) #analise desempenho
                medio = sum(1 for peca in self.pecasMedioDesempenho if peca in titulo.upper())
                leve = sum(1 for peca in self.pecasMenorDesempenho if peca in titulo.upper())
                desempenho = 'ALTO' if alto > medio > leve else ('MEDIO' if medio > alto > leve or medio == alto == leve else 'LEVE')
                
                lista_produtos.append({'titulo': titulo, 'preco': preco_formatado, 'desempenho': desempenho, 'link': link_completo})
                desempenhos_analisa_kabum.append(desempenho)
        
        analise_produtos = lista_produtos
        self.driver.quit() #saindo....
        return lista_produtos #retorna lista de dicionario
    
if __name__ == '__main__':
    scraper = ChromeScraperKabum()
    lista = scraper.scrap_pages()
    scraper_kabum = ChromeScraperKabum()
    lista_kabum = scraper_kabum.scrap_pages()

    scraper_amazon = ChromeScraperAmazon()
    lista_amazon = scraper_amazon.scrap_pages()

    for item in lista:
        print(item)
    lista_produtos = lista_kabum + lista_amazon
    grafo_produtos = GraphProdutos(lista_produtos)

    # Imprime as relações no grafo
    print("Relações de Desempenho:")
    for i in range(grafo_produtos.grafo.v):
        print(f"Produto {i} ({lista_produtos[i]['titulo']}):", end=" ")
        node = grafo_produtos.grafo.graph[i]
        while node:
            print(f"-> {node.vertex} ({lista_produtos[node.vertex]['titulo']})", end=" ")
            node = node.next
        print()