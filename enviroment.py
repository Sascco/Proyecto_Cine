# environment.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import logging

# Configurar logging para webdriver_manager
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def before_all(context):
    context.browser = 'chrome'  # Cambia a 'firefox' si lo deseas

def before_scenario(context, scenario):
    """
    Setup para cada escenario: inicializa el WebDriver.
    """
    try:
        if context.browser == 'chrome':
            service = ChromeService(ChromeDriverManager().install())
            context.driver = webdriver.Chrome(service=service)
        elif context.browser == 'firefox':
            service = FirefoxService(GeckoDriverManager().install())
            context.driver = webdriver.Firefox(service=service)
        else:
            raise ValueError(f"Navegador '{context.browser}' no soportado.")

        context.driver.maximize_window()
        context.driver.implicitly_wait(10)
        logger.info(f"WebDriver inicializado para escenario: {scenario.name}")
    except Exception as e:
        logger.error(f"Error en before_scenario para {scenario.name}: {e}")
        scenario.set_status('failed')
        raise

def after_scenario(context, scenario):
    """
    Teardown para cada escenario: cierra el WebDriver.
    """
    if hasattr(context, 'driver'):
        context.driver.quit()
        logger.info(f"WebDriver cerrado para escenario: {scenario.name}")
