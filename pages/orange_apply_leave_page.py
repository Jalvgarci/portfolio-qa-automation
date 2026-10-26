from playwright.sync_api import Page
from datetime import date
class ApplyLeavePage:
    def __init__(self, page: Page):
        self.page = page
        self.desplegar_leave_type = page.locator(".oxd-select-text-input").filter(has_text="-- Select --")
        self.leave_type = page.locator(".oxd-select-option").filter(has_text="CAN - Personal")
        #self.fecha_inicio = page.get_by_placeholder("yyyy-dd-mm")
        self.fecha_inicio = page.locator(".oxd-grid-item").filter(has_text="From Date").locator("input")
        self.fecha_fin = page.locator(".oxd-grid-item").filter(has_text="To Date").locator("input")
        self.fecha_hoy = date.today().strftime("%Y-%d-%m")
        #self.boton_apply = page.locator(".oxd-button").filter(has_text="Apply")
        #self.boton_apply = page.get_by_role("button", name="Apply")
        self.boton_apply = page.locator(".oxd-form-actions").filter(has_text="Apply").locator("button")

    def seleccionar_leave_type(self):
        self.desplegar_leave_type.click()
        self.leave_type.click()
        

    def informar_fechas (self):
        self.fecha_inicio.fill(self.fecha_hoy)
        self.fecha_inicio.press("Tab")



    def solicitar(self):
        with self.page.expect_response(
            lambda r: "leave-requests" in r.url and r.request.method == "POST",
            timeout=30000,
        ) as info:
            self.boton_apply.click()
        return info.value
    
        
        

