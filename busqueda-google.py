import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Users\\myarr\\OneDrive\\Escritorio\\Documentación Python\\Drivers\\chromedriver")
driver.get('https://www.google.es')

sleep(3.0)

cookies = driver.find_element(by=By.XPATH, value="//button[.//div[text()='Aceptar todo']]")
cookies.click()

sleep(3.0)
campo_texto = driver.find_element(by=By.NAME, value="q")
boton = driver.find_element(by=By.NAME, value="btnK")
action = ActionChains(driver)



campo_texto.send_keys("amazon")
action.send_keys("DELETE")
sleep(0.5)
boton.click()