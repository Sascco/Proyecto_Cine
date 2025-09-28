"""Fábrica de drivers: crea y configura instancias de Selenium WebDriver (Chrome, Firefox, etc.) para usarlas en los tests """


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def create_driver(headless: bool = True):
    options = webdriver.ChromeOptions()

    # Argumentos comunes
    options.add_argument("--start-maximized")

    # Modo headless (si se activa)
    if headless:
        options.add_argument("--headless=new")  # Para Chrome 109+
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(5)
    return driver


