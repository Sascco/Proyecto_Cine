"""
Configuración global de pytest para tests del sistema de cine
Define fixtures compartidas y hooks para todos los tests
"""

import pytest
from utils.browser import BrowserManager
import os


@pytest.fixture(scope="session")
def browser_manager():
    """
    Crea una instancia del administrador de navegador para la sesión completa
    Se ejecuta una vez al inicio y cierra al final de todos los tests
    """
    manager = BrowserManager()
    yield manager
    manager.quit_driver()


@pytest.fixture(scope="function")
def driver(browser_manager):
    """
    Proporciona un driver limpio para cada test function
    Se ejecuta antes y después de cada test
    """
    driver = browser_manager.get_driver()
    yield driver
    # Limpieza después de cada test
    driver.delete_all_cookies()
    # No cerramos el navegador para reutilizar la instancia