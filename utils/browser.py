from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class BrowserManager:
    def __init__(self):
        self.driver = None

    def get_driver(self): #Función que configura y devuelve un driver de Chrome
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Abre la ventana maximizada
        #chrome_options.add_argument("--headless")  # Descomenta para modo sin ventana

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()