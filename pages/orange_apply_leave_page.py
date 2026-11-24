from playwright.sync_api import Page
class ApplyLeavePage:
    def __init__(self, page: Page):
        self.page = page
        self.desplegar_leave_type = page.locator(".oxd-grid-item").filter(has_text="Leave Type").locator(".oxd-select-text-input")
        self.leave_type = page.locator(".oxd-select-option").filter(has_text="CAN - Personal")
        self.fecha_inicio = page.locator(".oxd-grid-item").filter(has_text="From Date").locator("input")
        self.fecha_fin = page.locator(".oxd-grid-item").filter(has_text="To Date").locator("input")
        self.boton_apply = page.locator(".oxd-form-actions").filter(has_text="Apply").locator("button")

    def seleccionar_leave_type(self):
        self.desplegar_leave_type.click()
        self.leave_type.click()

    def informar_fechas(self, fecha):
        formato_pantalla = self.fecha_inicio.get_attribute("placeholder")
        formato_python = (
            formato_pantalla
            .replace("yyyy", "%Y")
            .replace("mm", "%m")
            .replace("dd", "%d")
        )
        texto_fecha = fecha.strftime(formato_python)
        self.fecha_inicio.fill(texto_fecha)
        self.fecha_inicio.press("Tab")
        return texto_fecha

    def solicitar(self):
        with self.page.expect_response(
            lambda r: "leave-requests" in r.url and r.request.method == "POST",
            timeout=30000,
        ) as info:
            self.boton_apply.click()
        return info.value