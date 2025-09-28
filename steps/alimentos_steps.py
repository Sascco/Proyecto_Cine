import os
from behave import given, when, then
from openpyxl.styles.builtins import title
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import MenuAlimentosLocators

"""
Feature: Ver menú de Alimentos
  Como usuario
  Quiero poder ver las opciones de alimentos disponibles
  Para poder elegir qué quiero comer durante la función
"""

@given('que estoy en la página Alimentos')
def step_impl(context):
    context.driver.get("https://fake-cinema.vercel.app/alimentos")

@when("la página carga completament")
def step_esperar_carga_pagina(context):
    context.menu_page_obtener_items_menu()

@then("debo ver una lista de alimentos disponibles")
def step_ver_lista_alimentos(context):
    items = context.menu_page.obtener_items_menu()
    assert len(items) > 0, "No se encontraron alimentos en el menú"
    context.menu_items = items

@then("Cada ítem debe mostrar su título, imagen, breve descripción y precio")
def step_verificar_detalles_item(context):
    items = context.menu_page.obtener_items_menu()
    for item in items:
        title = item.find_element(*MenuAlimentosLocators.MENU_ITEM_TITlE).text.strip()
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
        assert any(name.lower() == t.lower() for t in titles), f"No se encontró '{name}' en el menú. Encontrados: {titles}"
        print: titles

@when("Presiono el botón de buscar")   # Boton de busqueda no funciona - BUG - HACER REPORTE EN JIRA
def presionar_buscar(context):
    icon = context.driver.find_element(*searchlocators.search_icon)    # Click en el ícono - Esto evidenciará el bug funcional.
    icon.click()
    WebDriverWait(context.driver, 2).until(lambda d: True)      # Espera breve (no usamos sleep fijo)

# Scenario Outline: Agregar palomitas y validar totales
@given('que veo la tarjeta de "{nombre}" con precio "{precio_unitario}"')
def step_ver_tarjeta_con_precio(context, nombre, precio_unitario):
    titles = context.menu_page.obtener_titulos_menu()
    assert any(nombre.lower() in t.lower() for t in titles), f"No se encontró la tarjeta '{nombre}' en el menú"
    # verificar precio en la tarjeta correspondiente
    items = context.menu_page.obtener_items_menu()
    for item in items:
        title = item.find_element(*MenuAlimentosLocators.MENU_ITEM_TITLE).text.strip()
        if nombre.lower() in title.lower():
            price_text = item.find_element(*MenuAlimentosLocators.MENU_ITEM_PRICE).text.strip()
            parsed = context.menu_page._parse_price(price_text)
            expected = context.menu_page._parse_price(precio_unitario)
            assert parsed == expected, f"Precio esperado {expected}, encontrado {parsed}"
            return
    raise AssertionError(f"No se encontró la tarjeta '{nombre}' con precio {precio_unitario}")

@when('agrego {cantidad:d} unidades de "{nombre}" al carrito')
def step_agregar_cantidad_al_carrito(context, cantidad, nombre):
    context.menu_page.agregar_al_carrito_por_nombre(nombre, cantidad)

@when('navego al "Carrito" desde la barra superior')
def step_ir_al_carrito(context):
    context.menu_page.ir_al_carrito()

@then("debo ver en el carrito:")
def step_verificar_carrito_tabla(context):
    expected_rows = [dict(row.items()) for row in context.table]
    detalles = context.menu_page.obtener_detalle_carrito()
    # comparar cada fila esperada con lo obtenido (buscar por nombre)
    for expected in expected_rows:
        nombre_esperado = expected.get("Ítem")
        cantidad_esperada = int(expected.get("Cantidad", 0))
        precio_unit_expected = context.menu_page._parse_price(expected.get("Precio Unitario"))
        subtotal_expected = context.menu_page._parse_price(expected.get("Subtotal") or expected.get("Total Esperado"))

        match = next((d for d in detalles if d["Ítem"].lower() == nombre_esperado.lower()), None)
        assert match is not None, f"No se encontró '{nombre_esperado}' en el carrito. Items en carrito: {[d['Ítem'] for d in detalles]}"
        assert match["Cantidad"] == cantidad_esperada, f"Cantidad esperada {cantidad_esperada}, encontrada {match['Cantidad']}"
        assert abs(match["Precio Unitario"] - precio_unit_expected) < 0.01, f"Precio unitario esperado {precio_unit_expected}, encontrado {match['Precio Unitario']}"
        assert abs(match["Subtotal"] - subtotal_expected) < 0.01, f"Subtotal esperado {subtotal_expected}, encontrado {match['Subtotal']}"

@then('el "Total" general debe mostrar "{total_esperado}"')
def step_verificar_total(context, total_esperado):
    actual = context.menu_page.obtener_total_carrito()
    expected = context.menu_page._parse_price(total_esperado)
    assert abs(actual - expected) < 0.02, f"Total esperado {expected}, encontrado {actual}"

@then('el botón "Proceder al pago" debe estar habilitado')
def step_verificar_boton_proceder(context):
    assert context.menu_page.boton_proceder_pago_habilitado(), "El botón 'Proceder al pago' NO está habilitado"

# Scenario: Agregar varios productos al carrito y validar totales
@when("agrego los siguientes productos al carrito:")
def step_agregar_varios(context):
    # context.table filas con Producto, Cantidad, Precio Unitario
    productos = []
    for row in context.table:
        productos.append({
            "Producto": row.get("Producto"),
            "Cantidad": row.get("Cantidad"),
            "Precio Unitario": row.get("Precio Unitario")
        })
    context.menu_page.agregar_varios_productos(productos)
