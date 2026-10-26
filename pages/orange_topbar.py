
from playwright.sync_api import Page

class BarraSuperior:
    def __init__(self, page: Page):
        self.page = page
        self.menu_usuario = page.locator(".oxd-userdropdown-tab")
        self.opcion_logout = page.get_by_role("menuitem", name="Logout")

    def cerrar_sesion(self):
        self.menu_usuario.click()
        self.opcion_logout.click()