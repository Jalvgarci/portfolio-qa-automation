from playwright.sync_api import Page
class LeavePage:
    def __init__(self, page: Page):
        self.page=page
        self.boton_apply = page.locator(".oxd-topbar-body-nav-tab-item").filter(has_text="Apply")
        


    def clic_apply(self):
        self.boton_apply.click()