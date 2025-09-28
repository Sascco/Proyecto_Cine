import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import MenuAlimentosLocators, SearchLocators
from pages.menu_alimentos_page import MenuAlimentosPage   # <-- IMPORTA EL PAGE OBJECT

logging.basicConfig(level=logging.INFO)

# ------------------ GIVEN ------------------
@given(u'que estoy en la página Alimentos')
def step_impl(context):
    context.driver.get("https://fake-cinema.vercel.app/alimentos")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    context.menu_page = MenuAlimentosPage(context.driver)

# ------------------ WHEN ------------------
@when("la página carga completamente")
def step_esperar_carga_pagina(context):
    context.menu_page.wait_until_loaded()

@when("Presiono el botón de buscar")   # BUG - Botón no funcional
def presionar_buscar(context):
    logging.warning("BUG: El botón de búsqueda no hace nada. Revisar JIRA-1234")
    icon = context.driver.find_element(*SearchLocators.search_icon)
    icon.click()

# ------------------ THEN ------------------
@then("debo ver una lista de alimentos disponibles")
def step_ver_lista_alimentos(context):
    items = context.menu_page.obtener_items_menu()
    assert len(items) > 0, "No se encontraron alimentos en el menú"
    context.menu_items = items

@then(u'cada ítem debe mostrar su título, imagen, breve descripción y precio')
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

@then('debo ver en el menú los siguientes alimentos:')
def step_verificar_lista_especifica(context):
    expected = [row[0] for row in context.table]
    titles = context.menu_page.obtener_titulos_menu()
    for name in expected:
        assert any(name.lower() == t.lower() for t in titles), \
            f"No se encontró '{name}' en el menú. Encontrados: {titles}"

