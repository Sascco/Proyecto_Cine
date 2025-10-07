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
      | nombre                  |
      | Combo Pareja       	    |
      | Miércoles 2x1        	|
      | Combo Kids           	|
      | Tarjeta Membresía	    |
      | Descuento Matiné 	    |
      | Combo Familiar     	    |
      | Precio Estudiantes	    |
      | Palomitas Refill		|
      | Bebida Grande Gratis    |
