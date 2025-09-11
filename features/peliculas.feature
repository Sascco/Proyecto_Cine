Feature: Ver películas disponibles
  Como usuario
  Quiero poder ver las películas disponibles
  Para poder elegir qué quiero ver

  Background:
    Given que estoy en la página principal

  Scenario: Ver lista de películas al cargar la página
    When ingreso a la página principal
    Then debo ver una lista de películas disponibles
    And cada tarjeta de película debe mostrar:
      | título | clasificación | duración | etiqueta "Estreno" si aplica | enlace "Ver detalle" |

  Scenario: Ver detalle al hacer clic en una película
    Given que la tarjeta de "Superman" está visible en la cartelera
    When hago clic en "Ver detalle" en la tarjeta de "Superman"
    Then debo ser llevado a la página de detalle de "Superman", en la cual debe aparecer el cine y las fechas de las funciones

  Scenario: Buscar película por título
    When escribo "Avengers" en la barra de búsqueda
    And presiono el botón de buscar
    Then debo ver solo películas que contengan "Avengers" en el título
#BUG- El icono (lupa) ubicado en la esquina superior derecha, no funciona.

