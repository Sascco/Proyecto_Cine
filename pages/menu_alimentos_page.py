# features/steps/alimentos_steps.py
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import MenuAlimentosLocators, CarritoLocators

class MenuAlimentosPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def obtener_items_menu(self):
        return self.driver.find_elements(*MenuAlimentosLocators.MENU_ITEM)

    def obtener_input_busqueda(self):
        try:
            return self.driver.find_element(*MenuAlimentosLocators.SEARCH_INPUT)
        except:
            return None


@given("que estoy en la página de alimentos")
def step_ir_a_pagina_alimentos(context):
    context.driver.get(ALIMENTOS_PAGE_URL)
    context.menu_page = MenuAlimentosPage(context.driver)


@then("Cada ítem debe mostrar su título, imagen, breve descripción y precio")
def step_verificar_detalles_item(context):
    items = context.menu_page.obtener_items_menu()
    for item in items:
        title = item.find_element(*MenuAlimentosLocators.MENU_ITEM_TITLE).text.strip()
        assert title != "", "Falta título en alguna tarjeta de alimento"

        img = item.find_element(*MenuAlimentosLocators.MENU_ITEM_IMAGE)
        assert img.is_displayed(), f"Imagen no visible para '{title}'"

        desc = item.find_element(*MenuAlimentosLocators.MENU_ITEM_DESC).text.strip()
        assert desc != "", f"Falta descripción para '{title}'"

        price = item.find_element(*MenuAlimentosLocators.MENU_ITEM_PRICE).text.strip()
        assert price != "", f"Falta precio para '{title}'"

"""
@when('escribo "{producto}" en la barra de búsqueda')
def step_buscar_producto(context, producto):
    search_input = context.menu_page.obtener_input_busqueda()
    if not search_input:
        logging.warning("BUG: No se encontró la barra de búsqueda en la página de alimentos")
        return
    search_input.clear()
    search_input.send_keys(producto)


@then('debo ver solo los alimentos que contengan "{producto}" en el título')
def step_verificar_resultados_busqueda(context, producto):
    items = context.menu_page.obtener_items_menu()
    assert len(items) > 0, "No se encontraron resultados en la búsqueda"
    for item in items:
        title = item.find_element(*MenuAlimentosLocators.MENU_ITEM_TITLE).text.strip()
        assert producto.lower() in title.lower(), f"El resultado '{title}' no coincide con la búsqueda '{producto}'"


@given('que veo la tarjeta de "{producto}" con precio "{precio}"')
def step_verificar_tarjeta_producto(context, producto, precio):
    item = context.menu_page.buscar_item_por_nombre(producto)
    assert item is not None, f"No se encontró el producto '{producto}'"
    displayed_price = item.find_element(*MenuAlimentosLocators.MENU_ITEM_PRICE).text.strip()
    assert precio in displayed_price, f"El precio esperado '{precio}' no coincide con '{displayed_price}'"


@when('agrego {cantidad:d} unidades de "{producto}" al carrito')
def step_agregar_producto_al_carrito(context, cantidad, producto):
    context.menu_page.agregar_al_carrito(producto, cantidad)


@when('navego al "Carrito" desde la barra superior')
def step_ir_a_carrito(context):
    context.menu_page.ir_al_carrito()


@then("debo ver en el carrito:")
def step_verificar_carrito_tabla(context):
    for row in context.table:
        nombre = row["Producto"]
        cantidad = int(row["Cantidad"])
        precio = Decimal(row["Precio"])
        total = Decimal(row["Total"])

        detalle = context.menu_page.obtener_detalle_carrito(nombre)
        assert detalle is not None, f"'{nombre}' no está en el carrito"
        assert detalle["cantidad"] == cantidad, f"Cantidad incorrecta para {nombre}"
        assert detalle["precio"] == precio, f"Precio incorrecto para {nombre}"
        assert detalle["total"] == total, f"Total incorrecto para {nombre}"


@then('el "Total" general debe mostrar "{total_esperado}"')
def step_verificar_total_general(context, total_esperado):
    esperado = Decimal(total_esperado)
    mostrado = context.menu_page.obtener_total_general()
    assert mostrado == esperado, f"El total esperado era {esperado}, pero se mostró {mostrado}"


@then('el botón "Proceder al pago" debe estar habilitado')
def step_verificar_boton_pago(context):
    boton = context.menu_page.obtener_boton_pago()
    assert boton.is_enabled(), "El botón 'Proceder al pago' no está habilitado"

"""