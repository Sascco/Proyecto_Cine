import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.promos_pages import PromosPage

scenarios('../promos.feature')

@given('que estoy en la página Promos', target_fixture='promos_page')
def navegar_a_promos(driver):
    """Navega a la página de promociones"""
    page = PromosPage(driver)
    page.abrir()
    return page

@when('la página carga completamente')
def pagina_carga_completamente(promos_page):
    """Espera a que la página cargue completamente"""
    # Verificar que el título está visible
    titulo = promos_page.obtener_titulo_promociones()
    assert titulo, "La página no cargó correctamente"
    print(f"✓ Página cargada. Título: {titulo}")

@then('debo ver una lista de promociones disponibles')
def verificar_lista_promociones(promos_page):
    """Verifica que hay promociones en la página"""
    promos = promos_page.obtener_promociones()
    assert len(promos) > 0, "No se encontraron promociones en la página"
    print(f"✓ Se encontraron {len(promos)} promociones")


@then('cada promoción debe mostrar su título, descripción y precio')
def verificar_datos_completos_promociones(promos_page):
    """Verifica que cada promoción tiene título, descripción y precio"""
    promos = promos_page.obtener_promociones()

    for i in range(len(promos)):
        nombre = promos_page.obtener_nombre_promo(i)
        descripcion = promos_page.obtener_descripcion_promo(i)
        precio = promos_page.obtener_precio_promo(i)

        assert nombre.strip(), f"La promoción {i} no tiene título"
        assert descripcion.strip(), f"La promoción {i} no tiene descripción"
        assert precio.strip(), f"La promoción {i} no tiene precio"
        assert "$" in precio, f"La promoción {i} no tiene un precio válido: {precio}"

    print(f"Todas las {len(promos)} promociones tienen datos completos")


@then(parsers.parse('debo ver en el listado las siguientes promociones:\n{table}'))
def verificar_promociones_especificas(promos_page, table):
    """Verifica que las promociones específicas están presentes"""
    # Parsear la tabla de datos
    lineas = [linea.strip() for linea in table.split('\n') if linea.strip()]

    # Saltar la primera línea (header: | nombre |)
    promociones_esperadas = []
    for linea in lineas[1:]:  # Empezar desde la segunda línea
        # Extraer el nombre entre los pipes |
        if '|' in linea:
            nombre = linea.split('|')[1].strip()
            if nombre and nombre != 'nombre':  # Ignorar el header si aparece
                promociones_esperadas.append(nombre)

    print(f"\n Verificando {len(promociones_esperadas)} promociones específicas:")

    # Verificar cada promoción esperada
    promociones_no_encontradas = []
    for promo_esperada in promociones_esperadas:
        existe = promos_page.verificar_promo_existe(promo_esperada)
        if existe:
            print(f"   {promo_esperada} - Encontrada")
        else:
            print(f"   {promo_esperada} - NO encontrada")
            promociones_no_encontradas.append(promo_esperada)

    # Assertion final
    assert len(promociones_no_encontradas) == 0, \
        f"Las siguientes promociones no se encontraron: {', '.join(promociones_no_encontradas)}"

    print(f"\n Todas las promociones esperadas están presentes")