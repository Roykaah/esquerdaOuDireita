from selenium import webdriver
import requests
from bs4 import BeautifulSoup
noticiaNumero = 0
driver = webdriver.Firefox(executable_path='C:\Drivers_firef\geckodriver.exe')
for i in range(2, 30):
    driver.get('https://www.gazetadopovo.com.br/republica/' + str(i) + '/')
    noticias = driver.find_elements_by_class_name('trigger-gtm')
    urlsTodas = [x.get_attribute("href") for x in noticias]
    urls = []
    for j in range(0, 24):
        urls.append(urlsTodas[j])
    for url in urls:
        response = requests.get(url)
        noticiaNumero = noticiaNumero + 1

        # verifica se a requisição foi bem-sucedida
        if response.status_code != 200:
            raise Exception('Não foi possível acessar a página')

        # extrai o conteúdo HTML da página
        html = response.content

        # analisa o HTML com BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        title = ''
        # extrai o título da matéria
        #for t in soup.find_all('h1'):
        #   title += t
        title = soup.find('h1', {'class': 'post-title'}).text.strip()
        #print(title)
        # extrai o texto da matéria
        text = ''
        for p in soup.find_all('div', {'class': 'wrapper'}):
            text += p.text.strip() + '\n'

        try:
            with open('GazetaDoPovo/' + str(noticiaNumero) + '.txt', 'w') as f:
                f.write(title + '\n' + text)
        except:
            print('falha ao escrever o arquivo numero ' + str(noticiaNumero))
        #except:
        # print('falha ao escrever o arquivo numero ' + str(noticiaNumero))

#driver.execute_script("links =  $('.news-item'); console.log(links);")