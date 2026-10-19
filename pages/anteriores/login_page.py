from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.usuario = page.locator("#username")
        self.clave = page.locator("#password")
        self.boton = page.locator("button[type='submit']")
        self.mensaje = page.locator("#flash")

    def abrir(self):
        self.page.goto("https://the-internet.herokuapp.com/login", timeout=60000)

    def login(self, usuario, clave):
        self.usuario.fill(usuario)
        self.clave.fill(clave)
        self.boton.click()