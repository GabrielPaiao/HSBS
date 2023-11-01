#codigo GABRIEL PEREIRA PAIAO
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import math
import re
from bs4 import BeautifulSoup

url = 'https://www.kabum.com.br/computadores/pc'

# Configurações do Selenium para simular um navegador (chrome)
option = Options()
option.add_argument('--headless')#faz em background, nao aparece
driver = webdriver.Chrome(options=option)

driver.get(url)
driver.implicitly_wait(10)

# Obtenha o conteúdo da página após o carregamento completo
soup = BeautifulSoup(driver.page_source, 'html.parser')

#analisando os produtos por pagina (20 por pagina)
qtd_items = soup.find('div', id='listingCount').get_text().strip()
index = qtd_items.find(' ') #ache o espaço em branco
qtd = qtd_items[:index] #me retorna do index até o espaço em branco, deixando apenas o número de items no site
ultima_pagina = math.ceil(int(qtd)/20)

dic_produtos = {'titulo': [], 'preco': []} #dicionario

for pagina in range(1, ultima_pagina + 1): #passando por todas as paginas
    url_pag = f'https://www.kabum.com.br/computadores/pc?page_number={pagina}&page_size=20&facet_filters=&sort=most_searched'
    soup = BeautifulSoup(driver.page_source, 'html.parser') #parsing dnv
    produtos = soup.find_all('div', class_=re.compile('productCard')) #procura todos os elementos que tem uma classe com o nome productCard

    for produto in produtos: #para cada produto
        titulo = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()
        print(f'Titulo: {titulo}\nPreco: R${preco}')

        dic_produtos['titulo'].append(titulo) #adicionando os dados no dicionario
        dic_produtos['preco'].append(preco)

'''dataframe = pd.DataFrame(dic_produtos)
dataframe.to_csv('um diretorio aqui do seu pc')''' #pra por tudo no excel ou outro app de planilhas (se quiser)

# Fechar o navegador após concluir
driver.quit()
