"""
Utilidades y localizadores compartidos para el proyecto de testing de cine
Contiene URLs, selectores y configuraciones comunes
"""

from selenium.webdriver.common.by import By

# URLs de la aplicación
URL_CINE = "https://fake-cinema.vercel.app/"

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
    MENU_ITEM_TITLE = (By.CSS_SELECTOR, "div.p-4 > h3.font-bold.text-lg.mb-1")
    MENU_ITEM_IMAGE = (By.XPATH, "./img[@class='w-full h-40 object-cover']")
    MENU_ITEM_DESC = (By.CSS_SELECTOR, "div.p-4 > p.text-sm.text-gray-300.mb-2")
    MENU_ITEM_PRICE = (By.CSS_SELECTOR, "div.p-4 > p.text-blue-400.font-semibold")
    ADD_TO_CART_BUTTON = (By.XPATH, "/html/body/div/main/div/div/button")
    MENU_ITEM_ADD_BUTTON = (By.CSS_SELECTOR, "button.add-to-cart")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.search-bar")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-button")
    NAV_CART_BUTTON = (By.CSS_SELECTOR, "button.nav-cart")
    CART_ITEM = (By.CSS_SELECTOR, "div.flex.justify-between.border-b.pb-2")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, ".cart-item__title")
    CART_ITEM_QTY = (By.CSS_SELECTOR, ".cart-item__quantity")
    CART_ITEM_UNIT_PRICE = (By.CSS_SELECTOR, ".cart-item__unit-price")
    CART_ITEM_SUBTOTAL = (By.CSS_SELECTOR, ".cart-item__subtotal")
    CART_TOTAL = (By.CSS_SELECTOR, "span.total-price")
    PROCEED_TO_PAY_BUTTON = (By.CSS_SELECTOR, "button.proceed-payment")