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

link = "https://thesaint.com.br/?fbclid=PAdGRleAM6dthleHRuA2FlbQIxMQABp18Ga0zr6ehn3HhTWQo4q4U6HFVsJLSXWDHSundAr9d1SIibHdPVv6mU1rmw_aem_AcsO6loHqMKKB9qBOcEmpg"

htmll = get_html(link)

dados_abas = get_aba(htmll)


print(dados_abas)