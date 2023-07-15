from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

navegador.get('https://www.walissonsilva.com/blog')
# sleep(3)

elemento = navegador.find_element(By.CSS_SELECTOR, 'input')

elemento.send_keys('data')
sleep(5)


navegador.quit()