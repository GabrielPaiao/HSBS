"""
Projeto-Project: HSBS - Hardware Suggetions Based on Software
Gabriel Pereira Paião; Lara Lima Silva; André; Pedro Henrique;
IFSP - Jacareí, SP - Brasil
"""
import analise_html_classe
import choices
import strings_list

print('Olá! Antes de começar, um carregamento rápido....')
produtos = analise_html_classe.ChromeScraperKabum().scrap_pages() #uma lista de dics pra cada pc {titulo - preço}
print(produtos)

produtos_att = choices.def_raiz(produtos)

print(produtos_att)