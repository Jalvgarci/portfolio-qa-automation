from playwright.sync_api import Page, expect
from pages.saucedemo_login_page import SauceDemoLoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_añadir_producto_y_ver_carrito(page: Page):
    login = SauceDemoLoginPage(page)
    login.abrir()
    login.login("standard_user", "secret_sauce")

    inventario = InventoryPage(page)
    inventario.añadir_mochila_al_carrito()
    inventario.ir_al_carrito()

    carrito = CartPage(page)
    expect(carrito.items_carrito).to_have_count(1)