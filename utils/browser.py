from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BrowserManager:
    def __init__(self):
        self.driver = None

    def get_driver(self):
        """Obtiene un driver de Chrome"""
        # Descargar automáticamente el ChromeDriver correcto
        service = ChromeService(ChromeDriverManager().install())

        # Crear el driver de Chrome
        self.driver = webdriver.Chrome(service=service)

        # Maximizar la ventana
        self.driver.maximize_window()

        return self.driver

    def close_driver(self):
        """Cierra el driver si existe"""
        if self.driver:
            self.driver.quit()
            self.driver = None