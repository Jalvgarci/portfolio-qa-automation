from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.nombre = page.locator("#first-name")
        self.apellido = page.locator("#last-name")
        self.codigo_postal = page.locator("#postal-code")
        self.boton_continuar = page.locator("#continue")
        self.boton_finalizar = page.locator("#finish")
        self.mensaje_confirmacion = page.locator(".complete-header")
        self.mensaje_error = page.locator(".error-message-container")

    def rellenar_datos_envio(self, nombre, apellido, codigo_postal):
        self.nombre.fill(nombre)
        self.apellido.fill(apellido)
        self.codigo_postal.fill(codigo_postal)
        self.boton_continuar.click()

    def finalizar_compra(self):
        self.boton_finalizar.click()