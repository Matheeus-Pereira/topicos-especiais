import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time

# Função para ler o arquivo
def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        linhas = file.readlines()
    return [linha.strip() for linha in linhas]

# Função para enviar mensagem via WhatsApp
def abrirZap():
    caminho = "https://web.whatsapp.com/"
    webbrowser.open(caminho);
    
serv = Service(executable_path='.\\chromedriver-win64\\chromedriver.exe');
driver = webdriver.Chrome(service=serv)


def enviar_mensagem(contato, mensagem):
      # Busca o campo de pesquisa de contato
    search_box = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(contato)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)

    # Localiza a caixa de texto para enviar a mensagem
    chat_box = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="6"]')
    chat_box.send_keys(mensagem)
    chat_box.send_keys(Keys.ENTER)
    time.sleep(2)  # Tempo para evitar problemas de envio

# Caminho para o arquivo de texto
caminho_arquivo = ".\\teste.txt"
# Número do contato em formato internacional (Ex: +5511999999999 para Brasil)
contato_whatsapp = "5548920005078"

# Lê o arquivo e envia cada linha como uma mensagem
linhas = ler_arquivo(caminho_arquivo)

abrirZap();

for linha in linhas:
    if linha:  # Verifica se a linha não está vazia
        enviar_mensagem(contato_whatsapp, linha)
        print(f"Mensagem enviada: {linha}")

driver.quit()