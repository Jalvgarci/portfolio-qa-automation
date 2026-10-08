from playwright.sync_api import Page
class MenuComponent:
    def __init__(self, page):
        self.page = page
        self.icono_menu = page.locator(".bm-burger-button")
        self.boton_dinamic_catalog = page.locator('[data-test="dynamic-catalog-sidebar-link"]')
        self.boton_lazy_load = page.locator('[data-test="dynamic-catalog-lazy-load-link"]')

    def abrir(self):
        self.icono_menu.click()

    def desplegar_menu_principal (self):
        self.icono_menu.click()
    
    def desplegar_dinamic_catalog (self):
        self.boton_dinamic_catalog.click()
    
    def ir_a_dinamic_catalog(self):
        self.boton_dinamic_catalog.click()

    def ir_a_lazy_load(self):
        self.boton_lazy_load.click()