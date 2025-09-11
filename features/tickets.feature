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
