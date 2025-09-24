"""
Tests para la página de películas del cine
Pruebas funcionales de la cartelera y navegación básica
"""

import pytest
from pages.peliculas_page import PeliculasPage


class TestPeliculasPage:
    """Suite de tests para la página de películas"""

    def test_abrir_cartelera(self, driver):
        """Verifica que la página de cartelera se abre correctamente"""
        page = PeliculasPage(driver)
        page.abrir()

        # Verificar URL
        assert "fake-cinema" in driver.current_url
        print(f"URL actual: {driver.current_url}")

        # Verificar título de cartelera
        titulo = page.obtener_titulo_cartelera()
        assert titulo == "Cartelera", f"Título esperado: 'Cartelera', encontrado: '{titulo}'"
        print(f"Título de cartelera: {titulo}")

    def test_lista_peliculas_cargada(self, driver):
        """Verifica que la lista de películas se carga correctamente"""
        page = PeliculasPage(driver)
        page.abrir()

        # Verificar que hay películas en cartelera
        peliculas = page.obtener_peliculas()
        assert len(peliculas) > 0, "No se encontraron películas en la cartelera"
        print(f"Se encontraron {len(peliculas)} películas")

    def test_estructura_tarjeta_pelicula(self, driver, cartelera=None):
        """Verifica que cada tarjeta de película tiene la estructura correcta"""
        page = PeliculasPage(driver)
        page.abrir()

        peliculas = page.obtener_peliculas()

        for i, pelicula in enumerate(peliculas[:3]):  # Probar solo las primeras 3
            try:
                titulo = pelicula.find_element(*MovieCardLocators.MOVIE_TITLE)
                assert titulo.text.strip() != "", f"Película {i} sin título"

                duracion = pelicula.find_element(*MovieCardLocators.MOVIE_DURATION)
                assert duracion.text.strip() != "", f"Película {i} sin duración"

                print(f"Película {i}: {titulo.text} - {duracion.text}")
            except Exception as e:
                pytest.fail(f"Error en película {i}: {str(e)}")cartelera encontrado: {titulo}")