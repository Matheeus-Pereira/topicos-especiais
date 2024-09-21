from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

serv = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=serv)

navegador.get("https://web.whatsapp.com/")