# 🎬 Sistema de Testing Automatizado para Cine

Este proyecto contiene pruebas automatizadas para el sistema de cine "Fake Cinema" implementado en `https://fake-cinema.vercel.app/`.

## 🏗️ Estructura del Proyecto

proyecto-cine/
├── features/ # Pruebas BDD con Behave
│ ├── peliculas.feature # Escenarios Gherkin
│ └── environment.py # Configuración Behave
├── pages/ # Page Objects
│ ├── init.py
│ ├── base_page.py # Clase base para páginas
│ └── peliculas_page.py # Página de cartelera
├── utils/ # Utilidades y helpers
│ ├── init.py
│ ├── browser.py # Gestión del navegador
│ └── helpers.py # Localizadores y configs
├── tests/ # Tests con pytest
│ ├── test_peliculas_page.py # Tests de página principal
│ └── test_cine_e2e.py # Tests E2E completos
├── reports/ # Reportes generados
├── screenshots/ # Capturas de error
├── requirements.txt # Dependencias
├── pytest.ini # Configuración pytest
└── README.md # Este archivo


## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- Google Chrome
- Git

### 1. Clonar y configurar el proyecto
```bash
  git clone <repositorio>
  cd proyecto-cine
```
2. Crear entorno virtual (recomendado)
```bash
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
```
3. Instalar dependencias
```bash
  pip install -r requirements.txt
```
4. Verificar instalación
```bash
  python --version
  pytest --version
  behave --version
```
🧪 Ejecución de Pruebas
```bash
  pytest -v
```

Ejecutar tests específicos
```bash
  # Solo tests E2E
  pytest -m e2e -v

  # Solo tests de regresión
  pytest -m regression -v

  # Tests con reporte HTML
  pytest --html=reports/report.html
```
Ejecutar pruebas BDD con Behave

```bash
  # Todos los features
  behave

  # Feature específico
  behave features/peliculas.feature

  # Con formato detallado
  behave -f pretty
```

Ejecutar con cobertura
```bash
  pytest --cov=. --cov-report=html
```