import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Importar Page Objects
from pages.menu_alimentos_page import MenuAlimentosPage
from pages.peliculas_page import PeliculasPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def before_all(context):
    """Configura WebDriver antes de ejecutar las pruebas."""
    logger.info("=== Iniciando pruebas de Fake Cinema ===")

    chrome_options = Options()
    chrome_options.add_argument("--headless")        # ✅ modo headless activado
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    service = ChromeService(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.implicitly_wait(10)

    # Diccionario de Pages para acceder desde steps
    context.pages = {
        "menu_alimentos": MenuAlimentosPage,
        "peliculas": PeliculasPage,
        # más adelante puedes agregar: "carrito": CartPage
    }


def before_scenario(context, scenario):
    logger.info(f"\n--- Escenario iniciado: {scenario.name} ---")


def after_scenario(context, scenario):
    logger.info(f"--- Escenario finalizado: {scenario.name} ---")
    context.driver.delete_all_cookies()


def after_all(context):
    """Cierra WebDriver al finalizar todas las pruebas."""
    if hasattr(context, "driver"):
        context.driver.quit()
        logger.info("=== WebDriver cerrado. Fin de pruebas ===")
