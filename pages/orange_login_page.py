from playwright.sync_api import Page

class OrangeLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.usuario = page.locator('[placeholder="Username"]')
        self.clave = page.locator('[placeholder="Password"]')
        self.boton = page.get_by_role("button", name="Login")
        #self.mensaje = page.locator("#flash")

    def abrir(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=60000)

    def login(self, usuario, clave):
        self.usuario.fill(usuario)
        self.clave.fill(clave)
        self.boton.click()