#codigo andré, alterado pelo gabriel para verificar se as classes ainda existem durante a execução
'''ETAPAS:
1. Pegar conteúdo HTML a partidr da url
2. Parsear o conteúdo com o Beautiful Soap
3. Transformar em dicionário (talvez?)
-GABRIEL'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.kabum.com.br/computadores/pc'
response = requests.get(url)

titulos_pc = []

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    computadores_div = soup.find_all('div', class_='sc-93fa31de-15 dCsZrx')

    if not computadores_div:
        print('Nenhuma div encontrada com a classe especificada.')
    else:
        for div in computadores_div:
            titulos = div.find_all('h2')
            for titulo in titulos:
                titulos_pc.append(titulo.text)
else:
    print('Falha ao carregar a página. Código de status:', response.status_code)

if not titulos_pc:
    print('Nenhum título de computador encontrado.')
else:
    for nome_configs in titulos_pc:
        print(nome_configs)
