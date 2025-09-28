from utils.driver_factory import create_driver

def before_scenario(context, scenario):
    # Inicializar el driver antes de cada escenario
    context.driver = create_driver(headless=True)  # Cambia a True si quieres ocultar el navegador

def after_scenario(context, scenario):
    # Cerrar el driver después de cada escenario
    if hasattr(context, "driver"):
        context.driver.quit()