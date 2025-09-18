"""Archivo de configuración de pytest: define fixtures, hooks y opciones compartidas para todos los tests"""

import pytest
from utils.driver_factory import create_driver


def pytest_adoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        help="Ejecutar pruebas en modo headless (sin interfaz de usuario)"
    )

@pytest.fixture()
def driver(request):
        headless = request.config.getoption("--headless")
        driver = create_driver(headless=headless)
        yield driver
        driver.quit()
