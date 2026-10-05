from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.boton_añadir_mochila = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.icono_carrito = page.locator(".shopping_cart_link")

    def añadir_mochila_al_carrito(self):
        self.boton_añadir_mochila.click()

    def ir_al_carrito(self):
        self.icono_carrito.click()