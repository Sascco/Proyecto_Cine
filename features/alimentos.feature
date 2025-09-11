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
      | Palomitas   			  |
      | Hot Dog  			      |
      | Nachos  			      |
      | Pizza por rebanada	|
      | Hamburguesa Clásica	|
      | Helado Sundae		    |
      | Pretzel Jumbo  		  |
      | Sandwich de Pollo  	|
      | Dulces Surtidos  		|
      | Agua Embotellada  	|

  Scenario: Buscar alimento por nombre
    When escribo “Pretzel Jumbo” en la barra de búsqueda
    And Presiono el botón de buscar
    Then debo ver solo los alimentos que contengan “Pretzel Jumbo” en el título
#BUG- El icono (lupa) ubicado en la esquina superior derecha, no funciona.

  Scenario Outline: Agregar palomitas y validar totales en el carrito
    Given que veo la tarjeta de "Palomitas" con precio "<Precio Unitario>"
    When agrego <Cantidad> unidades de "Palomitas" al carrito
    And navego al "Carrito" desde la barra superior
    Then debo ver en el carrito:
    | Ítem         | Cantidad   | Precio Unitario   | Subtotal          |
    | Palomitas    | <Cantidad> | <Precio Unitario> | <Total Esperado>  |
    And el "Total" general debe mostrar "<Total Esperado>"
    And el botón "Proceder al pago" debe estar habilitado

    Examples:
      | Cantidad | Precio Unitario | Total Esperado |
      | 1        | 3.50            | 3.50           |
      | 2        | 3.50            | 7.00           |

  Scenario: Agregar varios productos al carrito y validar totales
    Given que estoy en la página de productos
    When agrego los siguientes productos al carrito:
      | Producto          | Cantidad | Precio Unitario |
      | Palomitas         | 2        | 3.50            |
      | Agua Embotellada  | 1        | 1.50            |
      | Nachos            | 3        | 5.00            |
    And voy al carrito desde la barra superior
    Then debo ver en el carrito los siguientes detalles:
      | Ítem                | Cantidad | Precio Unitario | Subtotal |
      | Palomitas           | 2        | 3.50            | 7.00     |
      | Agua Embotellada    | 1        | 1.50            | 1.50     |
      | Nachos              | 3        | 5.00            | 15.00    |
    Then el carrito debe mostrar el total "<23.50>"
    And permitir proceder al pago
