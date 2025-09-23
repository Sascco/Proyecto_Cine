"""
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from utils.browser import BrowserManager
from selenium.webdriver.common.by import By
from utils.helpers import searchlocators, URL_CINE, moviecardlocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Pasos básicos:
@given("que estoy en la página principal")
def abrir_pagina_principal(context):
    context.browser = BrowserManager()                      # Manejador del browser
    context.driver = context.browser.get_driver()           # Se guarda el driver real
    context.driver.get(URL_CINE)                            # Navegar a la URL                       # la dirección que necesitamos usar
    context.wait = WebDriverWait(context.driver, 5)  # Espera explicita reutilizable


@when("ingreso a la página principal")
def ingresar_pagina_principal(context):                     # Ya estamos en la página desde el Background
    pass

# VERIFICACIONES DE PELÍCULAS

@then("debo ver una lista de películas disponibles")
def verificar_lista_peliculas(context):
    peliculas = context.driver.find_elements(By.CSS_SELECTOR, "div.p-4.text-white")
    assert len(peliculas) > 0, "No se encontraron películas en cartelera"
    context.peliculas = peliculas  # guardamos para pasos siguientes


@then("cada tarjeta de película debe mostrar:")
def verificar_información_pelicula(context):
    for card in context.peliculas:
        titulo = card.find_element(*moviecardlocators.movie_title_in_card)
        assert titulo.text != "", "Falta el título"

        clasificacion = card.find_element(*moviecardlocators.movie_rating_relative)
        assert clasificacion.is_displayed(), "Falta la clasificación"

        duracion = card.find_element(*moviecardlocators.movie_duration_relative)
        assert duracion.text != "", "Falta la duración"

        enlace_detalle = card.find_element(*moviecardlocators.movie_detail_link_relative)
        assert enlace_detalle.is_displayed(), "No se muestra el enlace 'Ver detalle'"


# ESCENARIO: DETALLE DE PELÍCULA


@given('que la tarjeta de "{titulo}" está visible en la cartelera')
def tarjeta_visible(context, titulo):
    context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.p-4.text-white")))
    cards = context.driver.find_elements(By.CSS_SELECTOR, "div.p-4.text-white")
    encontrada = any(titulo in c.text for c in cards)
    assert encontrada, f"No se encontró la tarjeta de {titulo}"


@when('hago clic en "Ver detalle" en la tarjeta de "{titulo}"')
def clic_en_ver_detalle(context, titulo):
    context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.p-4.text-white")))
    cards = context.driver.find_elements(By.CSS_SELECTOR, "div.p-4.text-white")
    for c in cards:
        if titulo in c.text:
            link = c.find_element(*moviecardlocators.movie_detail_link_relative)
            link.click()
            break
    time.sleep(2)  # cambiar a implicit wait ###############################################################

@then('debo ser llevado a la página de detalle de "{titulo}", en la cual debe aparecer el cine y las fechas de las funciones')
def verificar_detalle_pelicula(context, titulo):
    page_text = context.driver.page_source
    assert titulo in page_text, f"No se cargó la página de detalle de {titulo}"
    assert "Cine" in page_text or "Funciones" in page_text, "No se muestran cine/funciones en la página"


# ESCENARIO: BÚSQUEDA DE PELÍCULA


@when('escribo "{titulo}" en la barra de búsqueda')
def escribir_busqueda(context, titulo):
    search_box = context.driver.find_element(*searchlocators.search_input)
    search_box.clear()
    search_box.send_keys(titulo)


@when("presiono el botón de buscar")
def presionar_buscar(context):
    boton = context.driver.find_element(*searchlocators.search_button)
    boton.click()
    context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.p-4.text-white")))



@then('debo ver solo películas que contengan "{titulo}" en el título')
def verificar_resultados_busqueda(context, titulo):
    resultados = context.driver.find_elements(By.CSS_SELECTOR, "div.p-4.text-white")
    assert len(resultados) > 0, f"No se encontraron resultados para {titulo}"
    for r in resultados:
        assert titulo in r.text, f"Se encontró una película que no contiene {titulo}"

@then("cierro el navegador")
def cerrar_navegador(context):
    context.browser.quit_driver()
"""
from behave import given, when, then
from utils.browser import BrowserManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import searchlocators, URL_CINE, moviecardlocators

# Pasos básicos:
@given("que estoy en la página principal")
def abrir_pagina_principal(context):
    context.browser = BrowserManager()                      # Manejador del browser
    context.driver = context.browser.get_driver()           # Driver real
    context.driver.get(URL_CINE)                            # Navegar a la URL del cine
    context.wait = WebDriverWait(context.driver, 10)        # Espera explícita reutilizable

@when("ingreso a la página principal")
def ingresar_pagina_principal(context):
    # Ya estamos en la página desde el Given
    pass


# VERIFICACIONES DE PELÍCULAS

@then("debo ver una lista de películas disponibles")
def verificar_lista_peliculas(context):
    # Espera a que aparezca al menos una tarjeta de película
    context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.p-4.text-white")))
    peliculas = context.driver.find_elements(By.CSS_SELECTOR, "div.p-4.text-white")
    assert len(peliculas) > 0, "No se encontraron películas en cartelera"
    context.peliculas = peliculas  # se guarda para el siguiente paso

@then("cada tarjeta de película debe mostrar:")
def verificar_informacion_pelicula(context):
    for card in context.peliculas:
        titulo = card.find_element(*moviecardlocators.movie_title_in_card)
        assert titulo.text.strip() != "", "Falta el título"

        clasificacion = card.find_element(*moviecardlocators.movie_rating_relative)
        assert clasificacion.is_displayed(), "Falta la clasificación"

        duracion = card.find_element(*moviecardlocators.movie_duration_relative)
        assert duracion.text.strip() != "", "Falta la duración"

        enlace_detalle = card.find_element(*moviecardlocators.movie_detail_link_relative)
        assert enlace_detalle.is_displayed(), "No se muestra el enlace 'Ver detalle'"


# ESCENARIO: DETALLE DE PELÍCULA

@given('que la tarjeta de "{titulo}" está visible en la cartelera')
def tarjeta_visible(context, titulo):
    context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.p-4.text-white")))
    cards = context.driver.find_elements(By.CSS_SELECTOR, "div.p-4.text-white")
    encontrada = any(titulo in c.text for c in cards)
    assert encontrada, f"No se encontró la tarjeta de {titulo}"

@when('hago clic en "Ver detalle" en la tarjeta de "{titulo}"')
def clic_en_ver_detalle(context, titulo):
    context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.p-4.text-white")))
    cards = context.driver.find_elements(By.CSS_SELECTOR, "div.p-4.text-white")
    for c in cards:
        if titulo in c.text:
            link = c.find_element(*moviecardlocators.movie_detail_link_relative)
            link.click()
            break
    # Espera a que el contenido de detalle cargue (al menos que el título aparezca en el HTML)
    context.wait.until(lambda d: titulo.lower() in d.page_source.lower())

@then('debo ser llevado a la página de detalle de "{titulo}", en la cual debe aparecer el cine y las fechas de las funciones')
def verificar_detalle_pelicula(context, titulo):
    page_text = context.driver.page_source
    assert titulo in page_text, f"No se cargó la página de detalle de {titulo}"
    assert ("Cine" in page_text) or ("Funciones" in page_text), "No se muestran cine/funciones en la página"


# ESCENARIO: BÚSQUEDA DE PELÍCULA
# Nota: El botón de buscar actualmente NO funciona (icono sin acción).
# Este escenario fallará funcionalmente si no se filtran resultados, lo cual es esperado
# para evidenciar el bug. Técnicamente, los steps están correctos.

@when('escribo "{titulo}" en la barra de búsqueda')
def escribir_busqueda(context, titulo):
    search_box = context.driver.find_element(*searchlocators.search_input)
    search_box.clear()
    search_box.send_keys(titulo)

@when("presiono el botón de buscar")
def presionar_buscar(context):
    boton = context.driver.find_element(*searchlocators.search_button)
    boton.click()
    # Se mantiene una espera corta a resultados, aunque el botón no ejecute acción
    context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.p-4.text-white")))

@then('debo ver solo películas que contengan "{titulo}" en el título')
def verificar_resultados_busqueda(context, titulo):
    resultados = context.driver.find_elements(By.CSS_SELECTOR, "div.p-4.text-white")
    assert len(resultados) > 0, f"No se encontraron resultados para {titulo}"
    for r in resultados:
        assert titulo in r.text, f"Se encontró una película que no contiene {titulo}"

@then("cierro el navegador")
def cerrar_navegador(context):
    context.browser.quit_driver()