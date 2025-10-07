
# Automatización de Pruebas Funcionales Cinema Website

Este proyecto implementa la automatización de pruebas para un sitio web de cine: https://fake-cinema.vercel.app/ . Se cubren flujos clave de usuario relacionados con:

- Películas: visualización, filtrado, búsqueda y detalles.

- Promociones: listado y validación de promociones activas.

- Menú de Alimentos: navegación por categorías y verificación de precios.

La automatización está organizada con tres capas:

 - Features: describen en lenguaje claro qué debe ocurrir.

 - Pages: encapsulan cómo interactuar con la interfaz del sitio.

- Tests: ejecutan comprobaciones end-to-end y de componentes.

 - Utils: brindan soporte común para navegador, drivers y utilidades.


## Caracteristicas del Proyecto

- Pruebas legibles y alineadas al comportamiento esperado.

- Separación clara entre intención (Features) e implementación (Pages).

- Ejecución con Pytest y soporte para CI con GitHub Actions.

- Configuración de entorno mediante .env para controlar navegador y tiempos de espera.

- Utilidades centralizadas para iniciar y controlar el navegador de forma coherente.


## Alcance de la Automatización

Casos de prueba cubiertos

- Películas
    - Visualizar catálogo
    - Filtrar y buscar títulos
    - Acceder a detalles de una película

- Promociones
    - Listar promociones disponibles
    - Validar información clave de cada promoción

- Menú de Alimentos
    -  Navegar por categorías
    - Verificar precios y descripciones
## Estructura del Proyecto

    Proyecto_Cine/
    │── features/
    │   ├── peliculas.feature        # Escenarios de catálogo y detalle de películas
    │   ├── promos.feature           # Escenarios de promociones
    │   ├── alimentos.feature        # Escenarios de menú de alimentos
    │   ├── steps/
    │   │   ├── peliculas_steps.py   # Implementación de pasos de películas
    │   │   ├── promos_steps.py      # Implementación de pasos de promociones
    │   │   ├── alimentos_steps.py   # Implementación de pasos de alimentos
    │   │   └── common_steps.py      # Pasos comunes reutilizables
    │   └── environment.py           # Preparación y limpieza del contexto de pruebas
    │
    │── pages/
    │   ├── base_page.py             # Comportamientos base de interacción con la web
    │   ├── peliculas_page.py        # Acciones y localizadores de la sección de películas
    │   ├── promos_page.py           # Acciones y localizadores de promociones
    │   └── menu_alimentos_page.py   # Acciones y localizadores del menú de alimentos
    │
    │── tests/
    │       ├── test_cine_e2e.py         # Flujo end-to-end de usuario
    │       ├── test_peliculas_page.py   # Pruebas de la página de       películas
    │   └── test_imports.py          # Verificación básica de importaciones
    │
    │── utils/
    │   ├── browser.py               # Configuración centralizada del navegador
    │   ├── driver_factory.py        # Creación de drivers según configuración
    │   └── helpers.py               # Funciones auxiliares reutilizables
    │
    │── conftest.py                  # Configuración global de  Pytest y fixtures
    │── pytest.ini                   # Configuración de Pytest
    │── .env                         # Variables de entorno para la ejecución
    │── requirements.txt             # Dependencias del proyecto
    │── .github/workflows/           # CI con GitHub Actions
    └── README.md
## Descripción

Películas (features/peliculas.feature)
- Qué valida: al entrar a la home se listan películas; cada tarjeta muestra título, clasificación, duración y enlace “Ver detalle”. Al hacer clic, la página de detalle muestra información de cines/funciones. Se constata que el botón de búsqueda no filtra actualmente.


Alimentos (features/alimentos.feature)
- Qué valida: cada tarjeta de alimento muestra título, imagen, descripción y precio; se verifica una lista mínima esperada de productos. Se documenta el estado actual del “botón de buscar” sin efecto.


Promociones (features/promos.feature)
- Qué valida: la página de promociones carga correctamente, se listan tarjetas y cada una tiene título, descripción y precio; se verifica la presencia de promociones específicas.

## Installation

Instalación
Prerrequisitos

Python 3.8 o superior
Google Chrome
Git
Pasos

Clonar y entrar al proyecto:
-       git clone https://github.com/Sascco/Proyecto_Cine
-       cd Proyecto_Cine

(Recomendado) Crear y activar entorno virtual:
Windows: python -m venv venv && venv\Scripts\activate
macOS/Linux: python -m venv venv && source venv/bin/activate

Instalar dependencias:
-       pip install -r requirements.txt

Verificar herramientas:
-       pytest~=8.4.2
-       selenium~=4.34.2
-       webdriver-manager~=4.0.2
-       pytest-html~=4.1.0
-       pytest-cov~=5.0.0
-       behave~=1.2.6
-       allure-behave~=2.9.0

Variables de entorno

-       HEADLESS=true|false
Controla si el navegador corre sin interfaz. Recomendado true para ejecución en CI.

Ejecución

-       Pytest

Ejecutar toda la suite:
-       pytest -v
Por marcadores:
-       pytest -m e2e -v
-       pytest -m regression -v
-       pytest -m smoke -v
Reporte HTML:
-       pytest --html=reports/pytest-report.html --self-contained-html

Behave

Todos los features:
-       behave
Feature específico:
-       behave features/peliculas.feature
Salida legible:
behave -f pretty
Cobertura

-       pytest --cov=. --cov-report=html:reports/coverage --cov-report=term-missing
## License

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Authors

Ali Valentin Tovar Morales
QA Automation Tester
-Buenos Aires, Argentina
-ali.v.tovar@gmail.com
[LinkedIn](https://www.linkedin.com/in/ali-v-tovar/)

Roberto Gamboa López
QA Automation Tester
-Chiapas, México
-robertogamboa.9006@gmail.com
[LinkedIn](https://www.linkedin.com/in/robertogamboa07/)

Sergio Solano
QA Automation Tester
-Villavicencio, Colombia
-sergiosolanoc@gmail.com
[LinkedIn](https://www.linkedin.com/in/sergiosc-qa-tester/)

