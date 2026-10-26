from playwright.sync_api import Page

class DetalleEmpleado:
    def __init__(self, page: Page):
        self.page = page
        self.id_empleado = page.locator(".oxd-input-group").filter(has_text="Employee Id").locator("input")