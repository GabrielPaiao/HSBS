"""
Projeto-Project: HSBS - Hardware Suggetions Based on Software
Gabriel Pereira Paião; Lara Lima Silva; André; Pedro Henrique;
IFSP - Jacareí, SP - Brasil
"""
import analise_html_classe
from analise_html_classe import selection_sort
import choices

print('Olá! Antes de começar, um carregamento rápido....')
produtos = analise_html_classe.ChromeScraperKabum().scrap_pages() #uma lista de dics pra cada pc {titulo - preço - desmpenho}

#SELECTION SORT
lista_precos = selection_sort([item['preco'] for item in produtos])

produtos_ordenados = []
for j in range(len(lista_precos)):
    for i in range(len(produtos)):
        if produtos[i]['preco'].replace('.', '').replace(',', '.') == lista_precos[j]:
            produtos_ordenados.append(produtos[i])
            #print(produtos_ordenados[j])

produtos_att = choices.def_raiz(produtos_ordenados)

print("\nPRODUTOS COMPATÍVEIS: ")
for item in produtos_att:
    print("--------------------------------------------------------------------------------------------------")
    print(f"PC: {item['titulo']}\nPRECO: {item['preco']}\nDESEMPENHO: {item['desempenho']}")
