"""
Archivo de configuración de pytest: define fixtures, hooks y opciones compartidas para todos los tests
"""

import pytest
from utils.browser import BrowserManager
import os


@pytest.fixture(scope="session")
def browser_manager():   #Crea el manager del navegador una vez por sesión
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    manager = BrowserManager()
    yield manager
    manager.quit_driver()

""" #Screenshots automáticos si falla un test##############
def pytest_exception_interact(node, call, report):
    driver = node.funcargs.get("driver", None)
    if driver and report.failed:
        driver.save_screenshot(f"screenshots/{node.name}.png")
"""

@pytest.fixture(scope="function")
def driver(browser_manager):
    driver = browser_manager.get_driver()
    yield driver
    driver.delete_all_cookies()    # Limpieza después de cada test
