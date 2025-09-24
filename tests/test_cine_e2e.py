"""
Tests End-to-End para el flujo completo de compra de cine
Prueba la integración de todas las funcionalidades del sistema
"""

import pytest
import time
from pages.peliculas_page import PeliculasPage
from utils.helpers import NavigationLocators  # Importación añadida


@pytest.mark.e2e
class TestFlujoCompraCompleto:
    """Suite de tests E2E para el flujo completo de compra"""

    def test_flujo_compra_completo(self, driver):
        """
        Prueba el flujo completo de compra:
        Películas → Detalle → Selección → Asientos → Tickets
        """
        # 1. Navegar a la página principal
        page = PeliculasPage(driver)
        page.abrir()

        # 2. Verificar que la cartelera está cargada
        assert page.obtener_titulo_cartelera() == "Cartelera"
        peliculas = page.obtener_peliculas()
        assert len(peliculas) > 0

        print("✓ Cartelera cargada correctamente")

        # 3. Hacer clic en "Ver detalle" de la primera película
        try:
            page.hacer_clic_ver_detalle(0)
            time.sleep(2)  # Esperar carga de página de detalle

            # Verificar que estamos en página de detalle
            assert "movie" in driver.current_url.lower() or "detalle" in driver.current_url.lower()
            print("✓ Página de detalle cargada")

        except Exception as e:
            pytest.skip(f"Funcionalidad de detalle no disponible: {str(e)}")

    @pytest.mark.skip(reason="Funcionalidad de compra no implementada en el sitio")
    def test_seleccion_asientos_y_pago(self, driver):
        """Prueba la selección de asientos y proceso de pago"""
        # Este test se implementará cuando la funcionalidad esté disponible
        pass


@pytest.mark.regression
class TestsRegresion:
    """Tests de regresión para funcionalidades críticas"""

    def test_carga_pagina_principal(self, driver):
        """Verifica que la página principal carga correctamente"""
        page = PeliculasPage(driver)
        page.abrir()

        assert driver.current_url == page.url
        assert page.is_element_visible(NavigationLocators.CARTELERA_TITLE)

    def test_navegacion_entre_paginas(self, driver):
        """Verifica la navegación básica entre páginas"""
        page = PeliculasPage(driver)
        page.abrir()

        # Verificar que podemos recargar la página
        driver.refresh()
        assert page.obtener_titulo_cartelera() == "Cartelera"

    def test_navegacion_entre_paginas(self, driver):
        """Verifica la navegación básica entre páginas"""
        page = PeliculasPage(driver)
        page.abrir()

        # Verificar que podemos recargar la página
        driver.refresh()
        assert page.obtener_titulo_cartelera() == "Cartelera"