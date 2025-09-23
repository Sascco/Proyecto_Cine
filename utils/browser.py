"""
Módulo para gestión del navegador WebDriver
Configura y controla las instancias de Chrome para testing
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class BrowserManager:
    """Gestiona la creación y configuración del WebDriver"""

    def __init__(self, headless=False):
        """
        Inicializa el administrador del navegador

        Args:
            headless (bool): Si es True, ejecuta el navegador en modo sin interfaz
        """
        self.driver = None
        self.headless = headless

    def get_driver(self):
        """Configura y retorna una instancia de Chrome WebDriver"""
        chrome_options = Options()

        # Configuración de opciones de Chrome
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        if self.headless:
            chrome_options.add_argument("--headless=new")

        # Crear instancia del driver
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        # Configuración de timeouts
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(30)

        return self.driver

    def quit_driver(self):
        """Cierra la instancia del navegador si existe"""
        if self.driver:
            self.driver.quit()
            self.driver = None