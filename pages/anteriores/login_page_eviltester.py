from playwright.sync_api import Page

class LoginPageEvilTester:
    def __init__(self, page: Page):
        self.page = page
        self.usuario = page.locator("#username")
        self.clave = page.locator("#password")
        self.boton = page.locator("#login")

    def abrir(self):
        self.page.goto("https://testpages.eviltester.com/apps/simulated-login/")

    def login(self, usuario, clave):
        self.usuario.fill(usuario)
        self.clave.fill(clave)
        self.boton.click()