from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import PromosLocators




class PromosPage:
    url = "https://fake-cinema.vercel.app/promos"   # Pagina web promos

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(self.url)

    def obtener_titulo_promociones(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(PromosLocators.TITLE_PROMOS)
        ).text

    def obtener_promociones(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(PromosLocators.PROMO_ITEMS)
        )

    def obtener_nombre_promo(self, index):
        promos = self.obtener_promociones()
        return promos[index].find_element(*PromosLocators.PROMO_NAME).text

    def obtener_descripcion_promo(self, index):
        promos = self.obtener_promociones()
        return promos[index].find_element(*PromosLocators.PROMO_DESCRIPTION).text

    def obtener_precio_promo(self, index):
        promos = self.obtener_promociones()
        return promos[index].find_element(*PromosLocators.PROMO_PRICE).text

    def obtener_todas_las_promos(self):
        promos = self.obtener_promociones()
        resultado = []
        for promo in promos:
            resultado.append({
                "nombre": promo.find_element(*PromosLocators.PROMO_NAME).text,
                "descripcion": promo.find_element(*PromosLocators.PROMO_DESCRIPTION).text,
                "precio": promo.find_element(*PromosLocators.PROMO_PRICE).text
            })
        return resultado




