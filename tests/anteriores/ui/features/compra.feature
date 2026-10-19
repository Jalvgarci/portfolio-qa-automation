Feature: Compra en SauceDemo
  Como usuario de la tienda
  Quiero comprar un producto
  Para completar un pedido

  Scenario: Comprar la mochila con éxito
    Given que inicio sesión en SauceDemo
    When añado la mochila al carrito
    And voy al carrito y continúo a checkout
    And relleno los datos de envío
    Then veo el mensaje de confirmación de compra

  Scenario: Ordenar listado y comprar varios productos
    Given que inicio sesión en SauceDemo
    When ordeno el listado por precio ascendente
    And añado camiseta
    And añado chaqueta
    And voy al carrito y continúo a checkout
    And relleno los datos de envío
    Then veo el mensaje de confirmación de compra

  Scenario: comprobar navegación y validaciones
    Given que inicio sesión en SauceDemo
    When abro el menú
    And despliego menú Dinamic Catalog
    And voy al menú Dinamic Catalog/Lazy Load
    And compruebo que estoy en la página
