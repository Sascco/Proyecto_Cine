from behave import given, when, then
from utils.browser import BrowserManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL_CINE, SearchLocators, MovieCardLocators, NavigationLocators

# Selector base para tarjetas (si tienes uno más específico, úsalo aquí)
CARDS_CSS = "div.p-4.text-white"

# Palabras clave y patrones que indican que el detalle cargó correctamente
DETALLE_KEYWORDS = ["Cines", "Horarios", "Filtros"]
SHOWTIME_LINK_SELECTOR = "a[href*='/book']"  # Enlaces de horarios como /movies/<slug>/book


# PASOS BÁSICOS


@given("que estoy en la página principal")
def abrir_pagina_principal(context):
    context.browser = BrowserManager()
    context.driver = context.browser.get_driver()
    context.driver.get(URL_CINE)
    context.wait = WebDriverWait(context.driver, 10)

@when("ingreso a la página principal")
def ingresar_pagina_principal(context):
    # Ya estamos en la página desde el Given
    pass


# LISTADO DE PELÍCULAS


@then("debo ver una lista de películas disponibles")
def verificar_lista_peliculas(context):
    context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, CARDS_CSS)))
    peliculas = context.driver.find_elements(By.CSS_SELECTOR, CARDS_CSS)
    assert len(peliculas) > 0, "No se encontraron películas en cartelera"
    context.peliculas = peliculas                           # Guardamos para el paso siguiente

@then("cada tarjeta de película debe mostrar:")
def verificar_informacion_pelicula(context):
    for card in context.peliculas:
        titulo = card.find_element(*MovieCardLocators.MOVIE_TITLE)
        assert titulo.text.strip() != "", "Falta el título"

        # Clasificación
        clasificacion = card.find_element(*MovieCardLocators.MOVIE_RATING)
        assert clasificacion.is_displayed(), "Falta la clasificación"

        # Duración
        duracion = card.find_element(*MovieCardLocators.MOVIE_DURATION)
        assert duracion.text.strip() != "", "Falta la duración"

        # Enlace "Ver detalle"
        enlace_detalle = card.find_element(*MovieCardLocators.MOVIE_DETAIL_LINK)
        assert enlace_detalle.is_displayed(), "No se muestra el enlace 'Ver detalle'"

        # Etiqueta "Estreno" (si aplica, no forzamos que esté en todas)
        try:
            estreno = card.find_element(*MovieCardLocators.MOVIE_PREMIERE_LABEL)
            assert estreno.is_displayed(), "La etiqueta 'Estreno' está oculta"
        except Exception:
            # Si no aplica, no fallamos
            pass


# DETALLE DE PELÍCULA


@given('que la tarjeta de "{titulo}" está visible en la cartelera')
def tarjeta_visible(context, titulo):
    context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, CARDS_CSS)))
    cards = context.driver.find_elements(By.CSS_SELECTOR, CARDS_CSS)
    encontrada = any(titulo in c.text for c in cards)
    assert encontrada, f"No se encontró la tarjeta de {titulo}"

@when('hago clic en "Ver detalle" en la tarjeta de "{titulo}"')
def clic_en_ver_detalle(context, titulo):
    context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, CARDS_CSS)))
    cards = context.driver.find_elements(By.CSS_SELECTOR, CARDS_CSS)
    for c in cards:
        if titulo in c.text:
            link = c.find_element(*MovieCardLocators.MOVIE_DETAIL_LINK)
            link.click()
            break
    # Espera a que el título aparezca en el HTML de detalle
    context.wait.until(lambda d: titulo.lower() in d.page_source.lower())

@then('debo ser llevado a la página de detalle de "{titulo}", en la cual debe aparecer el cine y las fechas de las funciones')
def verificar_detalle_pelicula(context, titulo):
    # Confirmamos que cargó el detalle correspondiente
    assert titulo.lower() in context.driver.page_source.lower(), f"No se cargó la página de detalle de {titulo}"

    # Espera a que aparezca “Cines” o un enlace de horario (/book)
    try:
        context.wait.until(
            lambda d: ("cines" in d.page_source.lower())
            or len(d.find_elements(By.CSS_SELECTOR, SHOWTIME_LINK_SELECTOR)) > 0
        )
    except Exception:
        raise AssertionError(
            "No se muestran elementos de cine/funciones en la página de detalle.\n"
            f"URL actual: {context.driver.current_url}\n"
            f"Busqué alguna de estas señales: {', '.join(DETALLE_KEYWORDS)} o enlaces {SHOWTIME_LINK_SELECTOR}"
        )
