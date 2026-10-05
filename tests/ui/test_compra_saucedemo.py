import pytest
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("producto, cantidad_esperada", [
    ("sauce-labs-backpack", 1),
    ("sauce-labs-bike-light", 1),
])
def test_añadir_producto_al_carrito(inventario_logueado: Page, producto, cantidad_esperada):
    inventario = InventoryPage(inventario_logueado)
    inventario.añadir_producto(producto)
    inventario.ir_al_carrito()

    carrito = CartPage(inventario_logueado)
    expect(carrito.items_carrito).to_have_count(cantidad_esperada)

def test_checkout_sin_datos_muestra_error(inventario_logueado: Page):
    inventario = InventoryPage(inventario_logueado)
    inventario.añadir_producto("sauce-labs-backpack")
    inventario.ir_al_carrito()

    carrito = CartPage(inventario_logueado)
    carrito.ir_a_checkout()

    checkout = CheckoutPage(inventario_logueado)
    checkout.boton_continuar.click()

    expect(checkout.mensaje_error).to_contain_text("First Name is required")
def test_compra_completa(inventario_logueado: Page):

    inventario = InventoryPage(inventario_logueado)
    inventario.añadir_producto("sauce-labs-backpack")
    inventario.ir_al_carrito()

    carrito = CartPage(inventario_logueado)
    expect(carrito.items_carrito).to_have_count(1)
    carrito.ir_a_checkout()

    checkout = CheckoutPage(inventario_logueado)
    checkout.rellenar_datos_envio("Jaime", "García", "28000")
    checkout.finalizar_compra()

    expect(checkout.mensaje_confirmacion).to_contain_text("Thank you for your order!")