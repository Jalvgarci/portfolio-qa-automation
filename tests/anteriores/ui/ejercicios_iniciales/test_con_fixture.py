from playwright.sync_api import Page, expect

def test_area_segura_visible(sesion_logueada: Page):
    expect(sesion_logueada.locator("#flash")).to_contain_text("You logged into a secure area!", timeout=10000)

def test_boton_logout_existe(sesion_logueada: Page):
    expect(sesion_logueada.locator("a.button")).to_contain_text("Logout", timeout=10000)