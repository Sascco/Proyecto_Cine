"""Acciones generales: como dar click, escribir, visitar una pagina web. lo que vamos hacer en la pagina de forma general """
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Encuentra un elemento con espera de 10 segundos"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Encuentra múltiples elementos"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_element_visible(self, locator):
        """Verifica si un elemento es visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False