from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import MenuAlimentosLocators

class MenuAlimentosPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def abrir(self):
        self.driver.get("https://fake-cinema.vercel.app/alimentos")

    def obtener_items_menu(self):
        return self.driver.find_elements(*MenuAlimentosLocators.MENU_ITEM)

    def obtener_nombres_productos(self):
        items = self.obtener_items_menu()
        return [item.find_element(*MenuAlimentosLocators.MENU_ITEM_TITLE).text.strip() for item in items]

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(MenuAlimentosLocators.MENU_ALIMENTOS_PAGE_TITLE))

    def agregar_producto_al_carrito(self, nombre_producto):
        items = self.obtener_items_menu()
        for item in items:
            titulo = item.find_element(*MenuAlimentosLocators.MENU_ITEM_TITLE).text.strip()
            if titulo == nombre_producto:
                imagen = item.find_element(*MenuAlimentosLocators.ADD_TO_CART_IMAGE)
                imagen.click()
                return
        raise Exception(f"No se encontró el producto '{nombre_producto}' para agregar al carrito")