from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.items_carrito = page.locator(".cart_item")
        self.boton_checkout = page.locator("#checkout")

    def numero_de_items(self):
        return self.items_carrito.count()

    def ir_a_checkout(self):
        self.boton_checkout.click()