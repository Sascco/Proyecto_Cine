"""
Clase base para Page Objects
Proporciona métodos comunes para interacción con elementos web
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Clase base que contiene métodos comunes para todas las páginas"""


    def __init__(self, driver, timeout=10):
        """
        Inicializa la página base

        Args:
            driver: Instancia de WebDriver
            timeout (int): Tiempo máximo de espera en segundos
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        """Encuentra un elemento esperando a que esté presente"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Encuentra múltiples elementos"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        """Hace clic en un elemento después de esperar a que sea clickeable"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """Escribe texto en un campo de entrada"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Obtiene el texto de un elemento"""
        return self.find_element(locator).text

    def is_element_visible(self, locator, timeout=None):
        """Verifica si un elemento es visible"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, text, timeout=10):
        """Espera a que la URL contenga un texto específico"""
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))