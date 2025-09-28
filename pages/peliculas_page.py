"""
Page Object Model para la página de películas Contiene métodos para interactuar con la cartelera de cine
"""

from pages.base_page import BasePage
from utils.helpers import URL_CINE, SearchLocators, MovieCardLocators


class PeliculasPage(BasePage):
    """Representa la página principal de cartelera de películas"""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://fake-cinema.vercel.app/"

    def abrir(self):
        """Navega a la página principal del cine"""
        self.driver.get(self.url)
        print(f"Navegando a: {self.url}")

    def obtener_titulo_cartelera(self):
        """Obtiene el título de la sección de cartelera"""
        return self.get_text(NavigationLocators.CARTELERA_TITLE)

    def obtener_peliculas(self):
        """Retorna la lista de elementos de tarjetas de películas"""
        return self.find_elements(MovieCardLocators.MOVIE_CARD)

    def hacer_clic_ver_detalle(self, indice_pelicula=0):
        """
        Hace clic en 'Ver detalle' de una película específica

        Args:
            indice_pelicula (int): Índice de la película en la lista (0-based)
        """
        peliculas = self.obtener_peliculas()
        if indice_pelicula < len(peliculas):
            link_detalle = peliculas[indice_pelicula].find_element(
                *MovieCardLocators.MOVIE_DETAIL_LINK
            )
            link_detalle.click()
        else:
            raise IndexError(f"Índice {indice_pelicula} fuera de rango. Total películas: {len(peliculas)}")