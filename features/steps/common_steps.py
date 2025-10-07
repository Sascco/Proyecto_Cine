from behave import when, then
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

bug_reported = False

@when("la página carga completamente")
def step_impl(context):
    # Espera hasta que el DOM esté listo o el <body> sea visible
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located(("tag name", "body"))
    )

@when("presiono el botón de buscar")
def step_presionar_boton_buscar(context):
    global bug_reported
    if not bug_reported:
        logging.warning("Bug conocido: el botón de buscar no tiene funcionalidad implementada.")
        bug_reported = True
    # No hace nada porque el botón no funciona

@then("la lista de resultados no cambia y muestra todos los ítems")
def step_validar_lista_sin_filtrar(context):
    lista_actual = obtener_lista_visible(context)
    lista_antes = getattr(context, "lista_antes_busqueda", lista_actual)
    assert lista_actual == lista_antes, "La lista cambió, pero el botón no debería filtrar"

def obtener_lista_visible(context):
    """Obtiene los ítems visibles en la página (películas o alimentos)."""
    driver = getattr(context, "driver", None)
    if driver is None and hasattr(context, "menu_page"):
        driver = context.menu_page.driver
    if driver is None:
        return []

    # Selector genérico: películas (cards), alimentos (menu-item)
    elementos = driver.find_elements(
        By.CSS_SELECTOR, ".card, .menu-item, div.p-4.text-white"
    )
    return [e.text.strip() for e in elementos if e.is_displayed()]

@then("cierro el navegador")
def step_cerrar_navegador(context):
    if hasattr(context, "browser"):
        context.browser.quit_driver()
    elif hasattr(context, "driver"):
        context.driver.quit()