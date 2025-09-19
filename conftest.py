"""Archivo de configuración de pytest: define fixtures, hooks y opciones compartidas para todos los tests"""
import pytest
from utils.browser import BrowserManager

@pytest.fixture(scope="session")
def browser_manager():
    """Crea el manager del navegador una vez por sesión"""
    manager = BrowserManager()
    yield manager
    manager.close_driver()

@pytest.fixture(scope="function")
def driver(browser_manager):
    """Proporciona un driver limpio para cada test"""
    driver = browser_manager.get_driver()
    yield driver
    driver.quit()                #Se cierra el navegador
