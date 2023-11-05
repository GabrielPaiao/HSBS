"""
Projeto-Project: HSBS - Hardware Suggetions Based on Software
Gabriel Pereira Paião; Lara Lima Silva; André; Pedro Henrique;
IFSP - Jacareí, SP - Brasil
"""
import analise_html_classe

print('Olá! Antes de começar, um carregamento rápido....')
produtos = analise_html_classe.ChromeScraperKabum().scrap_pages() #um dic pra cada pc {titulo - preço}

