Feature: Ver menú de Alimentos
  Como usuario
  Quiero poder ver las opciones de alimentos disponibles
  Para poder elegir qué quiero comer durante la función

  Background:
    Given que estoy en la página Alimentos

  Scenario: Ver menú disponible
    When la página carga completamente
    Then debo ver una lista de alimentos disponibles
    And cada ítem debe mostrar su título, imagen, breve descripción y precio
    And debo ver en el menú los siguientes alimentos:
      | nombre              |
      | Palomitas   		|
      | Hot Dog  		|
      | Nachos  		|
      | Pizza por rebanada	|
      | Hamburguesa Clásica	|
      | Helado Sundae		|
      | Pretzel Jumbo  		|
      | Sandwich de Pollo  	|
      | Dulces Surtidos  	|
      | Agua Embotellada  	|

  Scenario: Presionar el botón de buscar sin funcionalidad
    When presiono el botón de buscar
    Then la lista de resultados no cambia y muestra todos los ítems

