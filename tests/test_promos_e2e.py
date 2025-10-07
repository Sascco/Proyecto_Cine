"""import pytest
from pages.promos_page import PromosPage


@pytest.mark.e2e
class TestPromosE2E:

    def test_ver_lista_promociones_disponibles(self, driver):
        # GIVEN: que estoy en la página Promos
        page = PromosPage(driver)
        page.abrir()
        print("\nNavegado a la página de Promos")

        # WHEN: la página carga completamente
        titulo = page.obtener_titulo_promociones()
        assert "Promociones" in titulo, f"Título esperado contiene 'Promociones', obtenido: '{titulo}'"
        print(f"Página cargada completamente. Título: '{titulo}'")

        # THEN: debo ver una lista de promociones disponibles
        promos = page.obtener_promociones()  # <- esta función debe usar PROMO_NAME como base
        assert len(promos) > 0, "No se encontraron promociones en la página"
        print(f"Se encontraron {len(promos)} promociones disponibles")

        # AND: cada promoción debe mostrar su título, descripción y precio
        print("\nVerificando que cada promoción tiene datos completos:")
        for i in range(len(promos)):
            nombre = page.obtener_nombre_promo(i)         # usa PROMO_NAME
            descripcion = page.obtener_descripcion_promo(i)  # usa PROMO_DESCRIPTION
            precio = page.obtener_precio_promo(i)         # usa PROMO_PRICE

            assert nombre.strip(), f"La promoción {i} no tiene título"
            assert descripcion.strip(), f"La promoción {i} no tiene descripción"
            assert precio.strip(), f"La promoción {i} no tiene precio"
            assert "$" in precio, f"La promoción {i} no tiene un precio válido: {precio}"

            print(f"  {i+1}. {nombre} - {precio} ")

        print(f"\nTodas las {len(promos)} promociones tienen título, descripción y precio")

        # AND: debo ver en el listado las siguientes promociones
        promociones_esperadas = [
            "Combo Pareja",
            "Miércoles 2x1",
            "Combo Kids",
            "Tarjeta Membresía",
            "Descuento Matiné",
            "Combo Familiar",
            "Precio Estudiantes",
            "Combo Amigos",
            "Palomitas Refill",
            "Bebida Grande Gratis"
        ]

        print(f"\nVerificando que las {len(promociones_esperadas)} promociones específicas están presentes:")
        promociones_no_encontradas = []

        for promo_esperada in promociones_esperadas:
            existe = page.verificar_promo_existe(promo_esperada)
            if existe:
                indice = page.obtener_indice_promo(promo_esperada)
                precio = page.obtener_precio_promo(indice)
                print(f"{promo_esperada} - {precio}")
            else:
                print(f"  ✗ {promo_esperada} - NO ENCONTRADA")
                promociones_no_encontradas.append(promo_esperada)

        assert len(promociones_no_encontradas) == 0, \
            f"Las siguientes promociones no se encontraron: {', '.join(promociones_no_encontradas)}"

        print(f"\n TODAS las promociones esperadas están presentes en la página")


@pytest.mark.regression
class TestPromosRegresion:
   Tests de regresión para la página de promociones

    def test_carga_pagina_promos(self, driver):
        page = PromosPage(driver)
        page.abrir()

        assert driver.current_url == page.url, \
            f"URL esperada: {page.url}, obtenida: {driver.current_url}"

        titulo = page.obtener_titulo_promociones()
        assert "Promociones" in titulo, f"Título esperado contiene 'Promociones', obtenido: '{titulo}'"

        print(f"Página de promociones cargada correctamente")

    def test_todas_promos_tienen_precio_valido(self, driver):
        page = PromosPage(driver)
        page.abrir()

        promos = page.obtener_promociones()
        precios_invalidos = []

        for i in range(len(promos)):
            nombre = page.obtener_nombre_promo(i)
            precio = page.obtener_precio_promo(i)

            if "$" not in precio:
                precios_invalidos.append(f"{nombre}: {precio}")

        assert len(precios_invalidos) == 0, \
            f"Las siguientes promociones tienen precios inválidos: {precios_invalidos}"

        print(f" Todas las {len(promos)} promociones tienen precios válidos")

    def test_cantidad_minima_promociones(self, driver):
        page = PromosPage(driver)
        page.abrir()

        promos = page.obtener_promociones()
        cantidad_minima = 5

        assert len(promos) >= cantidad_minima, \
            f"Se esperaban al menos {cantidad_minima} promociones, se encontraron {len(promos)}"

        print(f"✓ Hay {len(promos)} promociones disponibles (mínimo esperado: {cantidad_minima})")

    def test_obtener_todas_las_promos_completo(self, driver):
        page = PromosPage(driver)
        page.abrir()

        todas_promos = page.obtener_todas_las_promos()

        assert len(todas_promos) > 0, "No se obtuvieron promociones"

        print(f"\n✓ Información completa de {len(todas_promos)} promociones:")
        for i, promo in enumerate(todas_promos, 1):
            print(f"\n  {i}. {promo['nombre']}")
            print(f"     Precio: {promo['precio']}")
            print(f"     Descripción: {promo['descripcion'][:60]}...")

            assert promo['nombre'], f"Promoción {i} sin nombre"
            assert promo['descripcion'], f"Promoción {i} sin descripción"
            assert promo['precio'], f"Promoción {i} sin precio"


@pytest.mark.smoke
class TestPromosSmokeTests:
    def test_smoke_promos_basico(self, driver):
        page = PromosPage(driver)
        page.abrir()

        titulo = page.obtener_titulo_promociones()
        assert titulo, "No se pudo obtener el título de la página"

        promos = page.obtener_promociones()
        assert len(promos) >= 1, "No hay promociones disponibles"

        print(f"Smoke test completo: {len(promos)} promociones disponibles")
"""