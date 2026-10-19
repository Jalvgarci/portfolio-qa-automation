from playwright.sync_api import Page
class PimPage:
    def __init__(self, page: Page):
        self.page=page
        self.boton_add = page.get_by_role("button", name="Add")


    def clic_add(self):
        self.boton_add.click()