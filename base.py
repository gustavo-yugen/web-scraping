# bibliotecas.
#================================================================
import requests
from bs4 import BeautifulSoup

# pegar os dados do site.
#================================================================
def get_html (url: str):

    # html em bits:
    bits = requests.get(url)

    # html em texto:
    html = BeautifulSoup(bits.text, "html.parser")
    return html

# pegar o html da aba superior (pagina inicial).
#================================================================
def get_aba (html: BeautifulSoup):
    html_das_abas = html.find('div', class_="sections nav-sections")
    return html_das_abas
