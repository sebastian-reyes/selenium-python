import time

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait


def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless") #Correr en segundo plano
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)

    driver.get("https://www.saucedemo.com/v1/") # Ingresar a la página

    # Ingresar credenciales
    user_input = driver.find_element(By.ID,"user-name")
    user_input.send_keys(USER)
    password_input = driver.find_element(By.ID,"password")
    password_input.send_keys(PASSWORD)

    button = driver.find_element(By.ID,"login-button")
    button.click() # Hacer click en el botón

    time.sleep(10) # Esperar 5 segundos
    driver.quit()

# Definimos variables para el servicio
USER = "standard_user"
PASSWORD = "secret_sauce"

if __name__ == "__main__":
    main()
