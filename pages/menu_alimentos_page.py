# pages/menu_alimentos_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import ALIMENTOS_PAGE_URL, MenuAlimentosLocators
import re
from decimal import Decimal, InvalidOperation


class MenuAlimentosPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def abrir(self):
        self.driver.get(ALIMENTOS_PAGE_URL)

    def obtener_items_menu(self):
        self.wait.until(EC.presence_of_all_elements_located(MenuAlimentosLocators.MENU_ITEM))
        return self.driver.find_elements(*MenuAlimentosLocators.MENU_ITEM)

    def obtener_titulos_menu(self):
        items = self.obtener_items_menu()
        titles = []
        for item in items:
            try:
                titles.append(item.find_element(*MenuAlimentosLocators.MENU_ITEM_TITLE).text.strip())
            except Exception:
                titles.append("")
        return titles

    def escribir_en_busqueda(self, texto):
        inp = self.driver.find_element(*MenuAlimentosLocators.SEARCH_INPUT)
        inp.clear()
        inp.send_keys(texto)

    def presionar_buscar(self):
        btn = self.driver.find_element(*MenuAlimentosLocators.SEARCH_BUTTON)
        btn.click()
        self.wait.until(EC.presence_of_all_elements_located(MenuAlimentosLocators.MENU_ITEM))

    def buscar_alimento(self, texto):
        self.escribir_en_busqueda(texto)
        self.presionar_buscar()

    def agregar_al_carrito_por_nombre(self, nombre, cantidad=1):
        items = self.obtener_items_menu()
        for item in items:
            try:
                title_el = item.find_element(*MenuAlimentosLocators.MENU_ITEM_TITLE)
            except Exception:
                continue
            if nombre.lower() in title_el.text.lower():
                add_btn = item.find_element(*MenuAlimentosLocators.MENU_ITEM_ADD_BUTTON)

                # Esperar que el botón esté clickeable
                self.wait.until(EC.element_to_be_clickable(MenuAlimentosLocators.MENU_ITEM_ADD_BUTTON))
                add_btn = item.find_element(*MenuAlimentosLocators.MENU_ITEM_ADD_BUTTON)

                # Hacer clic tantas veces como cantidad
                for _ in range(int(cantidad)):
                    add_btn.click()

                    # Opcional: esperar que el contador cambie si hay uno visible
                    # self.wait.until(lambda d: self._contador_actualizado(...))

                return
        raise AssertionError(f"No se encontró el producto '{nombre}' para agregar al carrito")

    def agregar_varios_productos(self, productos):
        for p in productos:
            nombre = p.get("Producto") or p.get("Ítem") or p.get("Item")
            cantidad = int(p.get("Cantidad", 1))
            self.agregar_al_carrito_por_nombre(nombre, cantidad)

    def ir_al_carrito(self):
        self.driver.find_element(*MenuAlimentosLocators.NAV_CART_BUTTON).click()
        self.wait.until(EC.presence_of_all_elements_located(MenuAlimentosLocators.CART_ITEM))

    def obtener_items_carrito(self):
        self.wait.until(EC.presence_of_all_elements_located(MenuAlimentosLocators.CART_ITEM))
        return self.driver.find_elements(*MenuAlimentosLocators.CART_ITEM)

    def obtener_detalle_carrito(self):
        detalles = []
        items = self.obtener_items_carrito()
        for item in items:
            try:
                title = item.find_element(*MenuAlimentosLocators.CART_ITEM_TITLE).text.strip()
            except Exception:
                title = ""
            try:
                qty_text = item.find_element(*MenuAlimentosLocators.CART_ITEM_QTY).text.strip()
                qty = int(re.sub(r'\D', '', qty_text) or 0)
            except Exception:
                qty = 1
            try:
                unit_text = item.find_element(*MenuAlimentosLocators.CART_ITEM_UNIT_PRICE).text.strip()
                unit = self._parse_price(unit_text)
            except Exception:
                unit = Decimal("0.00")
            subtotal = qty * unit
            detalles.append({
                "Ítem": title,
                "Cantidad": qty,
                "Precio Unitario": unit,
                "Subtotal": subtotal
            })
        return detalles

    def obtener_total_carrito(self):
        el = self.driver.find_element(*MenuAlimentosLocators.CART_TOTAL)
        texto = el.text.strip()
        return self._parse_price(texto)

    def boton_proceder_pago_habilitado(self):
        btn = self.driver.find_element(*MenuAlimentosLocators.PROCEED_TO_PAY_BUTTON)
        return btn.is_enabled()

    def _parse_price(self, text):
        if not text:
            return Decimal("0.00")
        cleaned = text.replace("USD", "").replace("$", "").replace(",", ".")
        m = re.search(r"[-+]?\d*\.?\d+", cleaned)
        if not m:
            return Decimal("0.00")
        try:
            return Decimal(m.group(0)).quantize(Decimal("0.01"))
        except InvalidOperation:
            return Decimal("0.00")