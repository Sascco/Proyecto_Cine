from behave import given, when, then
from selenium.webdriver.common.by import By
import logging
from pages.menu_alimentos_page import MenuAlimentosPage
from utils.helpers import MenuAlimentosLocators

@given("que estoy en la página Alimentos")
def step_ir_a_pagina_alimentos(context):
    context.menu_page = MenuAlimentosPage(context.driver)
    context.menu_page.abrir()

@then("debo ver una lista de alimentos disponibles")
def step_ver_lista_alimentos(context):
    nombres = context.menu_page.obtener_nombres_productos()
    assert len(nombres) > 0, "No se encontraron productos en la página"
    print(f"Productos encontrados: {nombres}")

@then("cada ítem debe mostrar su título, imagen, breve descripción y precio")
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

@then("debo ver en el menú los siguientes alimentos:")
def step_verificar_lista_alimentos(context):
    nombres_esperados = [row['nombre'] for row in context.table]
    nombres_actuales = context.menu_page.obtener_nombres_productos()
    for nombre in nombres_esperados:
        assert nombre in nombres_actuales, f"El alimento '{nombre}' no está en el menú"

