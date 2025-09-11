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


##
