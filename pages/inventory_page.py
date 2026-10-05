from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.icono_carrito = page.locator(".shopping_cart_link")

    def añadir_producto(self, codigo_producto):
        self.page.locator(f'[data-test="add-to-cart-{codigo_producto}"]').click()

    def ir_al_carrito(self):
        self.icono_carrito.click()