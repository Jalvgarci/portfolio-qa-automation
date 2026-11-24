from playwright.sync_api import Page

class ViewLeaveListPage:
    def __init__(self, page: Page):
        self.page = page


    def fila_de(self, apellido):
        return self.page.locator(".oxd-table-row").filter(has_text=apellido)

    def clic_aprobar(self, fila):
        with self.page.expect_response(
            lambda r: "leave-requests/" in r.url and r.request.method == "PUT",
            timeout=30000,
        ) as info:
            fila.get_by_role("button", name="Approve").click()
        return info.value