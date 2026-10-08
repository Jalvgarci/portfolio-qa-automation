from playwright.sync_api import Page

class DynamicCatalogPage:
    def __init__(self, page: Page):
        self.page = page
        self.titulo_secundario = page.locator(".header_secondary_container")
