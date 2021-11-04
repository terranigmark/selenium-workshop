from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Pasamos el path de nuestro driver como un "object service"
s = Service('./chromedriver')
driver = webdriver.Chrome(service = s)
# Indicamos que visitaremos el sitio oficial de Python
driver.get("https://www.python.org")
# Hacemos una pausa de 5 segundos antes de la siguiente instrucción
sleep(5)

# Cerramos la ventana del navegador
driver.quit()
