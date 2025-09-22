#Localizadores:
from selenium.webdriver.common.by import By


URL_CINE = "https://fake-cinema.vercel.app/"

class searchlocators:    # Clase que contiene los localizadores para el icono/boton de buscar

    search_icon = (By.CSS_SELECTOR, "svg.lucide-search")

class moviecardlocators:      # Clase que contiene los Localizadores para los componentes de una tarjeta de película individual.
    movie_title_in_card = (By.CSS_SELECTOR, "h3.font-bold.truncate")   # Título de la película
    movie_rating_relative = (By.XPATH, ".//div[contains(@class, 'inline-flex') and contains(@class, 'bg-yellow-500')]") # Clasificación de la película
    movie_duration_relative = (By.CSS_SELECTOR, "span.text-gray-400")   # Duración de la película
    movie_premiere_label_relative = (By.XPATH, ".//div[contains(@class, 'inline-flex') and contains(., 'Estreno')]") # Etiqueta "Estreno" (Es el segundo div.inline-flex, o el que contiene el texto "Estreno"
    movie_detail_link_relative = (By.XPATH, ".//a[text()='Ver detalle']")   # Enlace "Ver detalle"