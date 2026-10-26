from playwright.sync_api import Page


class MyLeavePage:
    def __init__(self, page: Page):
        self.page = page
        self.pestana_my_leave = page.get_by_text("My Leave", exact=True)

    def abrir(self):
        self.pestana_my_leave.click()

    def fila_de(self, apellido):
        return self.page.locator(".oxd-table-row").filter(has_text=apellido)