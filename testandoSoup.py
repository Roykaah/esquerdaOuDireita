import requests
from bs4 import BeautifulSoup

# faz a requisição GET à página
url = 'https://www.brasildefato.com.br/2023/03/17/racismo-na-alesp-na-posse-deputada-thainara-foi-tratada-mais-de-10-vezes-como-assessora'
response = requests.get(url)

# verifica se a requisição foi bem-sucedida
if response.status_code != 200:
    raise Exception('Não foi possível acessar a página')

# extrai o conteúdo HTML da página
html = response.content

# analisa o HTML com BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# extrai o título da matéria
title = soup.find('h1', {'class': 'title'}).text.strip()

# extrai o texto da matéria
text = ''
for p in soup.find_all('div', {'class': 'text-content'}):
    text += p.text.strip() + '\n'

# imprime o resultado
print(title)
#print(text)

with open('BrasilDeFato/1.txt', 'w') as f:
    f.write(title + '\n' + text)
