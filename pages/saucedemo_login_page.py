from playwright.sync_api import Page

class SauceDemoLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.usuario = page.locator("#user-name")
        self.clave = page.locator("#password")
        self.boton = page.locator("#login-button")

    def abrir(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, usuario, clave):
        self.usuario.fill(usuario)
        self.clave.fill(clave)
        self.boton.click()
