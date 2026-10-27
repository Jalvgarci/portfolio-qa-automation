from playwright.sync_api import Page

class ViewLeaveListPage:
    def __init__(self, page: Page):
        self.page = page


    def fila_de(self, apellido):
        return self.page.locator(".oxd-table-row").filter(has_text=apellido)

    def clic_aprobar(self, fila):
        fila.get_by_role("button", name="Approve").click()