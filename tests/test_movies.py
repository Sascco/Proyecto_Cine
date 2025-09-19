
import pytest
from pages.peliculas_page import PeliculasPage

def test_abrir_cartelera(driver):
    page = PeliculasPage(driver)
    page.abrir()

    assert "fake-cinema" in driver.current_url
    print(f"Estas en la pagina: {driver.current_url}")

    titulo = page.obtener_titulo_cartelera()
    assert titulo == "Cartelera", f"Título esperado: 'Cartelera', pero se encontró: '{titulo}'"
    print(f"Título de cartelera encontrado: {titulo}")

