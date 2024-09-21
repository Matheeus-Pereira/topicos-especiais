from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



def setup():
   serv = Service(ChromeDriverManager().install())
   navegador = webdriver.Chrome(service=serv)
   navegador.get("https://web.whatsapp.com/")
   return navegador

zap=setup()

zap.implicitly_wait(10)

# zap.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys("Darlon")
# zap.find_element('xpath', '//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div/div[2]').click()
# zap.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]').send_keys("viadinho")

