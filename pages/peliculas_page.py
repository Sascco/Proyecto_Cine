from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PeliculasPage(BasePage):

    # Localizadores
    CARTELERA_TITULO = (By.XPATH, "//h2[contains(text(), 'Cartelera')]")
    VER_DETALLE = (By.XPATH, "/html/body/div/main/section[2]/div[2]/div[4]/div/a"")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://fake-cinema.vercel.app/"  # ← Esta línea debe ser exactamente así

    def abrir(self):
        """Navega a la página principal"""
        print(f"Navegando a: {self.url}")
        self.driver.get(self.url)
        print("Página cargada")

    def obtener_titulo_cartelera(self):
        titulo_element = self.driver.find_element(*self.CARTELERA_TITULO)
        return titulo_element.text

    def ver_detalles_pelicula(self):
        elemento = self.find_element(*self.VER_DETALLE)
        elemento.click()
