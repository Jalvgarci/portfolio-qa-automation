from playwright.sync_api import Page

class MenuLateralPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_pim = page.get_by_role("link", name="PIM")

    def ir_a_pim(self):
        self.menu_pim.click()