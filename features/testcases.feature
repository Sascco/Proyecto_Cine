Feature: Compra de boletos de cine
  Como usuario
  Quiero poder comprar boletos de cine en línea
  Para poder elegir película, asiento y pagar de manera sencilla

  Background:
    Given que la película "Superman" está en cartelera

  Scenario: Seleccionar película en cartelera
    When el usuario selecciona como fecha el día siguiente a la fecha actual
    And el usuario selecciona la función en su idioma de preferencia "Español" o "Subtitulada"
    Then la película queda seleccionada con fecha y función definidas

  Scenario: Seleccionar asientos
    Given que el usuario ya seleccionó la película "Superman" con fecha y función
    When el usuario selecciona las sillas de acuerdo a su preferencia
    Then las sillas quedan registradas en la selección

  Scenario: Confirmar detalles de la compra
    Given que el usuario ya seleccionó la película, función y sillas
    When el usuario revisa y confirma la información de la compra
   	| Película 	| Cine		    | Fecha 		      | Hora 		| Sillas |
	  | Superman	| The Shoppes	| Sabado 23 Ago 	| 6:00 PM	| 3	     |
    And el usuario indica el tipo y cantidad de boletos
      	| Niños         		| 1 |
      	| Adultos 	       	| 1 |
      	| Adultos Mayores	  | 1 |
    Then el sistema muestra el resumen con un total de 3 boletos

  Scenario: Intento de seleccionar asiento ocupado
    Given que el usuario ya seleccionó la película “ Superman” con fecha y función
    And el asiento A5 está ocupado
    When el usuario intenta seleccionar el asiento “A5”
    Then el sistema no permite seleccionar el asiento “A5”
    And el sistema muestra una X en la casilla del asiento ocupado

  Scenario: Intento de seleccionar asiento para persona con movilidad reducida - Silla de ruedas-
    Given que la película "Superman" está seleccionada con fecha y función
    And el asiento marcado como "Silla de ruedas" al final de la fila "D" está disponible
    When el usuario intenta seleccionar el asiento "Silla de ruedas"
    Then debo ver que el asiento "Silla de ruedas" queda seleccionado
    And debo ver el indicador de asiento ocupado (por ejemplo, "X" o estado "ocupado") en la casilla del asiento

  Scenario: Proceder al pago
    Given que el usuario confirmó los detalles de la compra con 3 boletos
    When el usuario hace clic en "Proceder al Pago"
    And diligencia el formulario con datos válidos
    Then el sistema muestra el mensaje "¡Pago completado!"
    And el sistema muestra el valor total de la compra

  Scenario: Pago rechazado por tarjeta inválida
    Given que el usuario confirmó los detalles de la compra con 3 boletos por un total de "$240.00"
    When el usuario completa el formulario con una tarjeta de crédito con número inválido
    And confirma el pago
    Then el sistema debe mostrar el mensaje "Pago rechazado: tarjeta inválida"
    And el estado de la compra debe permanecer como "no pagado"
#BUG - La pagina acepta el pago con cualquier tarjeta, el unico requerimiento de todo el formulario es que el correo electronico tenga un @.


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

Feature: Ver y seleccionar PROMOS
  Como usuario
  Quiero poder visualizar y seleccionar promociones disponibles
  Para aprovechar descuentos y combos especiales en mis compras

  Background:
    Given que estoy en la página Promos

  Scenario: Ver lista de promociones disponibles
    When la página carga completamente
    Then debo ver una lista de promociones disponibles
    And cada promoción debe mostrar su título, descripción y precio
    And debo ver en el listado las siguientes promociones:
      | Combo Pareja       	|
      | Miércoles 2x1        	|
      | Combo Kids           	|
      | Tarjeta Membresía	|
      | Descuento Matiné 	|
      | Combo Familiar     	|
      | Precio Estudiantes	|
      | Palomitas Refill		|
      | Bebida Grande Gratis	|

  Scenario Outline: Ver detalle y agregar promoción al carrito
    When selecciono "<Promoción>"
    Then debo ver la información detallada:
      | título      | <Promoción>    |
      | descripción | <Descripción>  |
      | precio      | <Precio>       |
    And debo ver un botón "Agregar al carrito"
    When hago clic en el botón "Agregar al carrito"
    Then el carrito debe mostrar el ítem "<Promoción>" con precio "<Precio>"
    And el botón "Proceder al pago" debe estar habilitado

 Examples:
    | Promoción           | Descripción                                                                                       | Precio |
    | Combo Pareja        | Disfruta de nuestra promoción para parejas con dos boletos, una palomitas grande y dos refrescos  | $20.00 |
    | Miércoles 2x1       | Todos los miércoles obtén dos entradas por el precio de una para cualquier función disponible     | $7.50  |
    | Combo Kids          | Entrada infantil con un combo pequeño de palomitas y jugo natural para los más pequeños           | $8.00  |
    | Combo Familiar      | Cuatro entradas, palomitas extragrandes y bebidas para todos por un precio reducido               | $25.00 |
    | Precio Estudiantes  | Presentando tu credencial obtienes un descuento especial en cualquier función de lunes a viernes  | $6.00  |
    | Combo Amigos        | Tres boletos junto a un balde de palomitas y tres refrescos medianos a un costo accesible         | $25.00 |
    | Palomitas Refill    | Compra tu balde de palomitas y rellénalo las veces que quieras durante la misma función           | $6.50  |
    | Bebida Grande Gratis| En la compra de cualquier combo grande recibe una bebida extra completamente gratis               | $0.00  |



