from playwright.sync_api import Page


class AsignarDiasPage:
    def __init__(self, page: Page):
        self.page = page
        self.pestana_entitlements = page.locator(".oxd-topbar-body-nav-tab-item").filter(has_text="Entitlements")
        self.opcion_add = page.get_by_role("menuitem", name="Add Entitlements")
        self.empleado = page.get_by_placeholder("Type for hints...")
        self.sugerencias = page.locator(".oxd-autocomplete-dropdown")
        self.tipo_ausencia = self._grupo("Leave Type").locator(".oxd-select-text")
        self.dias = self._grupo("Entitlement").locator("input")
        self.boton_save = page.get_by_role("button", name="Save")
        self.boton_confirm = page.get_by_role("button", name="Confirm")

    def _grupo(self, etiqueta):
        return self.page.locator(".oxd-input-group").filter(
            has=self.page.get_by_text(etiqueta, exact=True)
        )

    def abrir_formulario(self):
        self.pestana_entitlements.click()
        self.opcion_add.click()

    def seleccionar_empleado(self, apellido):
        self.empleado.fill(apellido)
        self.sugerencias.get_by_text(apellido).click()

    def seleccionar_tipo(self, tipo):
        self.tipo_ausencia.click()
        self.page.get_by_role("option", name=tipo, exact=True).click()

    def asignar_dias(self, dias):
        self.dias.fill(str(dias))
        self.boton_save.click()
        self.boton_confirm.click()