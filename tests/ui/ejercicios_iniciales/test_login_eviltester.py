import pytest
from playwright.sync_api import Page, expect
from pages.login_page_eviltester import LoginPageEvilTester

@pytest.mark.parametrize("usuario, clave, es_correcto", [
    ("Admin", "AdminPass", True),
    ("Admin", "clave_mala", False),
    ("usuario_falso", "AdminPass", False),
])
def test_login_eviltester(page: Page, usuario, clave, es_correcto):
    login = LoginPageEvilTester(page)
    login.abrir()
    login.login(usuario, clave)

    if es_correcto:
        expect(page).to_have_url("https://testpages.eviltester.com/apps/simulated-login/adminview/")
        expect(page.get_by_text("You are Admin")).to_be_visible()
    else:
        expect(page.get_by_text("Login Details Incorrect")).to_be_visible()