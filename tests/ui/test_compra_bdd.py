from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect
from pages.saucedemo_login_page import SauceDemoLoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.menu_component import MenuComponent
from pages.dynamic_catalog_page import DynamicCatalogPage

scenarios("features/compra.feature")

@given("que inicio sesión en SauceDemo")
def iniciar_sesion(page: Page):
    login = SauceDemoLoginPage(page)
    login.abrir()
    login.login("standard_user", "secret_sauce")

@when("añado la mochila al carrito")
def añadir_mochila(page: Page):
    InventoryPage(page).añadir_producto("sauce-labs-backpack")

@when("voy al carrito y continúo a checkout")
def ir_a_checkout(page: Page):
    InventoryPage(page).ir_al_carrito()
    CartPage(page).ir_a_checkout()

@when("relleno los datos de envío")
def rellenar_envio(page: Page):
    CheckoutPage(page).rellenar_datos_envio("Jaime", "García", "28000")
    CheckoutPage(page).finalizar_compra()

@then("veo el mensaje de confirmación de compra")
def comprobar_confirmacion(page: Page):
    expect(CheckoutPage(page).mensaje_confirmacion).to_contain_text("Thank you for your order!")


@when("ordeno el listado por precio ascendente")
def ordenar_listado(page: Page):
    InventoryPage(page).ordenar_listado("lohi")

@when("añado camiseta")
def añadir_camiseta(page: Page):
    InventoryPage(page).añadir_producto("sauce-labs-bolt-t-shirt")

@when("añado chaqueta")
def chaqueta(page: Page):
    InventoryPage(page).añadir_producto("sauce-labs-fleece-jacket")    


@when ("abro el menú")
def abrir_menú (page: Page):
   MenuComponent(page).desplegar_menu_principal()

@when ("despliego menú Dinamic Catalog")
def desplegar_menu_dinamic (page: Page):
    MenuComponent(page).desplegar_dinamic_catalog()

@when ("voy al menú Dinamic Catalog/Lazy Load")
def navegar_menu_lazy_load (page: Page):
    MenuComponent(page).ir_a_lazy_load()

@when ("compruebo que estoy en la página")
def comprobar_titulo_pagina (page:Page):
    expect(DynamicCatalogPage(page).titulo_secundario).to_contain_text("Dynamic Catalog - Lazy Load")

