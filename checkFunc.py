from bs4 import BeautifulSoup
import requests
# Importando a lib pra testar a conexão.
# Dá pra deixar só com o útlimo import, mas assim evita erros.
try:
    import httplib
except:
    import http.client as httplib

# Função que vai checar a conexão.
def check(url="www.google.com", timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception as e:
        #print(e)           #'Descomenta' pra mostrar os erros no console
        return False

# Função para pegar o IP do computador
def myIp(url="https://www.myip.com/", timeout=3):
    # Utilizando BeautifulSoup para pegar o IP
    # Algumas mudanças para evitar erros caso inicie o app sem internet
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        elements = soup.find_all("div", class_="texto_1")
    # O primeiro elemento é o IPv6 e o segundo é o IPv4
        result = elements[1].text
        return result
    except Exception as e:
        return "No connection..."