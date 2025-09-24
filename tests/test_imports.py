#!/usr/bin/env python3
"""
Script para verificar que todas las importaciones funcionan correctamente
"""

try:
    # Importar desde utils
    from utils.helpers import NavigationLocators, MovieCardLocators, SearchLocators

    print("✅ Importación desde utils.helpers: CORRECTA")

    # Importar desde pages
    from pages.peliculas_page import PeliculasPage

    print("✅ Importación desde pages.peliculas_page: CORRECTA")

    # Importar desde tests
    from tests.test_cine_e2e import TestFlujoCompraCompleto, TestsRegresion

    print("✅ Importación desde tests.test_cine_e2e: CORRECTA")

    # Verificar que NavigationLocators tiene los atributos esperados
    assert hasattr(NavigationLocators, 'CARTELERA_TITLE')
    assert hasattr(NavigationLocators, 'PAGE_HEADER')
    print("✅ NavigationLocators tiene los atributos esperados")

    print("\n🎉 ¡TODAS LAS IMPORTACIONES FUNCIONAN CORRECTAMENTE!")

except ImportError as e:
    print(f"❌ Error de importación: {e}")
except AttributeError as e:
    print(f"❌ Error de atributo: {e}")
except Exception as e:
    print(f"❌ Error inesperado: {e}")