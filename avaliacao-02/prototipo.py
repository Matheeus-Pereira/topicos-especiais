from typing import KeysView
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup():
    serv = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=serv)
    navegador.get("https://web.whatsapp.com/")
    return navegador

zap = setup()


wait = WebDriverWait(zap, 30)


search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p')))
search_box.send_keys("Darlon")


contact = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div/div[2]')))
contact.click()


chat_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')))


def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        linhas = file.readlines()
    return [linha.strip() for linha in linhas]
 
 
caminho_arquivo = "./teste.txt"
linhas = ler_arquivo(caminho_arquivo)

for linha in linhas:
    if linha: 
       chat_box.send_keys(linha)
       chat_box.send_keys(KeysView.ENTER)
       


