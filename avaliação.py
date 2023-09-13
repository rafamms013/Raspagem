from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def CadastraCarro():
    driver = webdriver.Firefox()
    driver.get("http://weka.inf.ufes.br/IFESTP/login.php")

    txtLogin = driver.find_element(By.NAME, "username")
    txrSenha = driver.find_element(By.NAME, "password")

    txtLogin.send_keys("Nathan")
    txrSenha.send_keys("")
    time.sleep(3)

    btnOk = driver.find_element(By.NAME, "submit")
    btnOk.click()
    time.sleep(3)

    time.sleep(3)
    btnInserir = driver.find_element(By.XPATH, "/html/body/div/div/div/button")
    btnInserir.click()
    time.sleep(3)

    marca = driver.find_element(By.ID, "marca")
    modelo = driver.find_element(By.ID, "modelo")
    municipio = driver.find_element(By.ID, "municipio")
    valor = driver.find_element(By.ID, "valor")
    ano = driver.find_element(By.ID, "ano")
    tipo = driver.find_element(By.ID, "c_hatch")
    cambio = driver.find_element(By.ID, "cambioAutomatico")
    cor = Select(driver.find_element(By.ID, "cor"))

    driver = webdriver.Firefox()
    driver.get("https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/seda/estado-es/norte-do-espirito-santo?me=40000&pe=60000&rs=65")

    #btnAnuncio=driver.find_element(By.XPATH,"/html/body/main/div/div/div/main/div/div/section/a")
    btnAnuncio=driver.find_element(By.CLASS_NAME, "sc-dJjYzT dOvWTZ")
    btnAnuncio.click()
    time.sleep(3)

    marca.send_keys(By.CLASS_NAME,'sc-bZQynM fqHmWf')
    #listamarca=[marca[3]]
    modelo.send_keys(By.CLASS_NAME,'sc-bZQynM fqHmWf')
    #listamodelo=[modelo[2]]
    municipio.send_keys(By.CLASS_NAME,'ad__sc-1f2ug0x-1 cpGpXB sc-jTzLTM ieZUgc')
    valor.send_keys(By.CLASS_NAME,'sc-ifAKCX bFGyjy')
    ano.send_keys(By.CLASS_NAME,'sc-bZQynM fqHmWf')
    #listaano=[ano[5]]
    tipo.click()
    cambio.click()
    cor.select_by_visible_text('sc-jTzLTM cseqXy')

    btnOK = driver.find_element(By.NAME, "insert")
    btnOK.click()
    time.sleep(2)

    driver.close()

CadastraCarro()
