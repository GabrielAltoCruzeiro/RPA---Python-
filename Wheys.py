from selenium import webdriver as opçaoSelenium
from selenium.webdriver.common.by import By 
from time import sleep as tempo 
import pyautogui as teclado
import pandas as pd

navegador = opçaoSelenium.Chrome()
navegador.get('https://www.gsuplementos.com.br/?gad_source=1&gad_campaignid=23582388653&gbraid=0AAAAAD3gQWM6CT9Dv1Z0PcyWqpgkHnCfo&gclid=CjwKCAiA2PrMBhA4EiwAwpHyC7waSV6J9y7czNQT-hntHMtNS7BUVDEVu2rAfxA-OhE4Lcg488zbIhoCtBgQAvD_BwE')

# listas growth 
WheysGrowthDataframe = []
PreçoGrowthDataframe = []




tempo(6)

navegador.find_element(By.ID, 'busca-principal-topo').send_keys('Whey 1kg concentrado')
teclado.press('enter')

tempo(6)

WheysG = navegador.find_elements(By.XPATH,"//a[@class='card__name']")
PreçosG = navegador.find_elements(By.XPATH,"//span[@class='price']")



for WheyAtual in WheysG:
    WheysGrowthDataframe.append(WheyAtual.text)

for PreçoAtualG in PreçosG:
    PreçoGrowthDataframe.append(PreçoAtualG.text)

   


df = pd.DataFrame({
    'WHEY CONCENTRADO 1KG GROWHT':  WheysGrowthDataframe,
    'PREÇO '
    ':': PreçoGrowthDataframe
    
})

arquivoExcel = df.to_excel("dadosWhey.xlsx", index=False)



