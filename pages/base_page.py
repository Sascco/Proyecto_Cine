"""Acciones generales: como dar click, escribir, visitar una pagina web. lo que vamos hacer en la pagina de forma general """

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def visit(self, url: str):                                          # Navega a una URL
        self.driver.get(url)

    def click(self, locator: tuple[By, str]):                           # Hace click en un elemento localizado por un tuple (By, selector).
        self.driver.find_element(*locator).click()

    def type(self, locator: tuple[By, str], text: str):                 # Limpia y escribe texto en un input.
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def text_of_element(self, locator: tuple[By, str]) -> str:          # Obtiene el texto de un elemento.
        return self.driver.find_element(*locator).text

    def element_is_visible(self, locator: tuple[By, str]) -> bool:      # Devuelve True si el elemento está visible, False si no existe o está oculto.
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False
