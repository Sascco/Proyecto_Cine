"""
Utilidades y localizadores compartidos para el proyecto de testing de cine
Contiene URLs, selectores y configuraciones comunes
"""

from selenium.webdriver.common.by import By

# URLs de la aplicación
URL_CINE = "https://fake-cinema.vercel.app/"

class SearchLocators:
    """Localizadores para la funcionalidad de búsqueda"""
    SEARCH_ICON = (By.CSS_SELECTOR, "svg.lucide-search")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search'], input[placeholder*='buscar']")

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
