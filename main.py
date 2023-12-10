"""
Projeto-Project: HSBS - Hardware Suggetions Based on Software
Gabriel Pereira Paião; Lara Lima Silva; André; Pedro Henrique;
IFSP - Jacareí, SP - Brasil
"""
import analise_html_classe
from analise_html_classe import selection_sort
import escolhas

print('Olá! Antes de começar, um carregamento rápido....')
produtos_kabum = analise_html_classe.ChromeScraperKabum().scrap_pages() #uma lista de dics pra cada pc {titulo - preço - desmpenho}
produtos_amazon = analise_html_classe.ChromeScraperAmazon().scrap_pages()

#SELECTION SORT
lista_precos_kabum = selection_sort([item['preco'] for item in produtos_kabum])
lista_precos_amazon = selection_sort([item['preco'] for item in produtos_amazon if item['preco'] != 'Nenhuma opção de compra em destaque'])

vetorGeralProdutos = []
vetorGeralDesempenhos = []

produtos_ordenados_kabum = []
for j in range(len(lista_precos_kabum)):
    for i in range(len(produtos_kabum)):
        if produtos_kabum[i]['preco'].replace('.', '').replace(',', '.') == lista_precos_kabum[j]:
            produtos_ordenados_kabum.append(produtos_kabum[i])

vetorGeralProdutos.append(produtos_ordenados_kabum)

produtos_ordenados_amazon = []
for j in range(len(lista_precos_amazon)):
    for i in range(len(produtos_amazon)):
        if produtos_amazon[i]['preco'].replace('.', '').replace(',', '.') == lista_precos_amazon[j]:
            produtos_ordenados_amazon.append(produtos_amazon[i])

vetorGeralProdutos.append(produtos_ordenados_amazon)

analisa_desempenhos_kabum = []

for produto in produtos_ordenados_kabum:
    analisa_desempenhos_kabum.append(produto['desempenho'])

vetorGeralDesempenhos.append(analisa_desempenhos_kabum)

analisa_desempenhos_amazon = []

for produto in produtos_ordenados_amazon:
    analisa_desempenhos_amazon.append(produto['desempenho'])


tipo, PesquisaFinal = escolhas.main_raiz()

escolhas_kabum = escolhas.nova_lista(produtos_ordenados_kabum, analisa_desempenhos_kabum, tipo, PesquisaFinal)
escolhas_amazon = escolhas.nova_lista(produtos_ordenados_amazon, analisa_desempenhos_amazon, tipo, PesquisaFinal)

print("\n-------------PRODUTOS COMPATÍVEIS-------------: ")
print("LOJA KaBum:")
for item in escolhas_kabum:
    print("--------------------------------------------------------------------------------------------------")
    print(f"PC: {item['titulo']}\nPRECO: {item['preco']}\nDESEMPENHO: {item['desempenho']}\nLINK: {item['link']}")

print("\n\n--------------------------------------------------------------------------------------------------\nLOJA Amazon:")
for item in escolhas_amazon:
    print("--------------------------------------------------------------------------------------------------")
    print(f"PC: {item['titulo']}\nPRECO: {item['preco']}\nDESEMPENHO: {item['desempenho']}\nLINK: {item['link']}")