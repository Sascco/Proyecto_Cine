
from selenium.webdriver.common.by import By

# URLs de la aplicación
URL_CINE = "https://fake-cinema.vercel.app/"
ALIMENTOS_PAGE_URL = "https://fake-cinema.vercel.app/alimentos"
PROMOS_PAGE_URL = "https://fake-cinema.vercel.app/promos"


class SearchLocators:
    search_icon = (By.CSS_SELECTOR, "svg.lucide-search")    # Ícono de búsqueda (svg.lucide-search en tu código original)
    search_input = (By.CSS_SELECTOR, "input[type='search'], input.search-bar, input[type='text']") # Input de búsqueda (fallback si lo necesitas)

class MovieCardLocators:
    """Localizadores para las tarjetas de películas"""
    MOVIE_CARD = (By.CSS_SELECTOR, "div.p-4.text-white")
    MOVIE_TITLE = (By.CSS_SELECTOR, "h3.font-bold.truncate")
    MOVIE_RATING = (By.XPATH, ".//div[contains(@class, 'inline-flex') and contains(@class, 'bg-yellow-500')]")
    MOVIE_DURATION = (By.CSS_SELECTOR, "span.text-gray-400")
    MOVIE_PREMIERE_LABEL = (By.XPATH, ".//div[contains(@class, 'inline-flex') and contains(., 'Estreno')]")
    MOVIE_DETAIL_LINK = (By.XPATH, ".//a[text()='Ver detalle']")

class NavigationLocators:
    """Localizadores para navegación y elementos generales"""
    CARTELERA_TITLE = (By.XPATH, "//h2[contains(text(), 'Cartelera')]")
    PAGE_HEADER = (By.TAG_NAME, "h1")

class MenuAlimentosLocators:
    """Localizadores para la pagina el menú ALIMENTOS"""
    MENU_ALIMENTOS_LINK = (By.XPATH, "/html/body/div/header/div/div[1]/nav/a[2]")
    MENU_ALIMENTOS_PAGE_TITLE = (By.XPATH, "/html/body/div/main/h1")
    MENU_ITEM = (By.CSS_SELECTOR, "a.bg-\\[\\#0d1f3a\\].rounded-lg.overflow-hidden") # Locator para cada tarjeta de producto
    MENU_ITEM_TITLE = (By.CSS_SELECTOR, "h3.font-bold.text-lg.mb-1") # Locator para el título dentro de cada tarjeta
    MENU_ITEM_IMAGE = (By.XPATH, "./img[@class='w-full h-40 object-cover']")
    MENU_ITEM_DESC = (By.CSS_SELECTOR, "div.p-4 > p.text-sm.text-gray-300.mb-2")
    MENU_ITEM_PRICE = (By.CSS_SELECTOR, "div.p-4 > p.text-blue-400.font-semibold")
    ADD_TO_CART_BUTTON = (By.XPATH, "/html/body/div/main/div/div/button")
    MENU_ITEM_ADD_BUTTON = (By.CSS_SELECTOR, "button.add-to-cart")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.search-bar")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-button")

class PromosLocators:
    PROMOS_TITLE = (By.CSS_SELECTOR, "h1.text-2xl.font-bold.mb-4")  # Título "Promociones"
    PROMO_CARD_TITLE = (By.XPATH, "/html/body/div/main/div/a[3]/div/h3")  # Todas las tarjetas
    PROMO_NAME = (By.XPATH, "/html/body/div/main/div/a[3]/div/h3")  # Nombre en tarjeta
    PROMO_DESCRIPTION = (By.XPATH, "/html/body/div/main/div/a[3]/div/p[1]")  # Descripción en tarjeta
    PROMO_PRICE = (By.XPATH, "/html/body/div/main/div/a[3]/div/p[2]")  # Precio en tarjeta

