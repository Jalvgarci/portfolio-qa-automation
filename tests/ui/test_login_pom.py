import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@pytest.mark.parametrize("usuario, clave, mensaje", [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("tomsmith", "clave_mala", "Your password is invalid!"),
    ("usuario_falso", "SuperSecretPassword!", "Your username is invalid!"),
])
def test_login_con_pom(page: Page, usuario, clave, mensaje):
    login = LoginPage(page)
    login.abrir()
    login.login(usuario, clave)
    expect(login.mensaje).to_contain_text(mensaje, timeout=10000)