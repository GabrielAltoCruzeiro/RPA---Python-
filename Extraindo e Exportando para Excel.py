"""
Automação simples para extração de tabela via Selenium
e exportação dos dados para Excel usando Pandas.
"""

from selenium import webdriver as opçaoSelenium 
from selenium.webdriver.common.by import By
import pandas 


# Inicializa o navegador e acessa o site
navegador = opçaoSelenium.Chrome()
navegador.get("https://www.w3schools.com/html/html_tables.asp")


# Localiza a tabela na página
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="customers"]')
linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")


# Armazena os dados extraídos
dataFrameLista = []

for linhaAtual in linhas:
    print(linhaAtual.text)
    dataFrameLista.append(linhaAtual.text)


# Converte os dados para DataFrame
dataFrame = pandas.DataFrame(
    dataFrameLista,
    columns=['Nome_Coluna_dados']
)


# Exporta para Excel
arquivoExcel = pandas.ExcelWriter('DadosExcel.xlsx', engine='xlsxwriter')
dataFrame.to_excel(arquivoExcel, sheet_name='sheet1', index=False)
arquivoExcel.close()