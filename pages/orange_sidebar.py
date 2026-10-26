from playwright.sync_api import Page

class MenuLateralPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_pim = page.get_by_role("link", name="PIM")
        self.menu_leave = page.get_by_role("link", name="Leave", exact=True)

    def ir_a_pim(self):
        self.menu_pim.click()

    def ir_a_leave(self):
        self.menu_leave.click()
