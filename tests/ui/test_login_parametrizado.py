import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("usuario, clave, mensaje", [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("tomsmith", "clave_mala", "Your password is invalid!"),
    ("usuario_falso", "SuperSecretPassword!", "Your username is invalid!"),
    ("", "", "Your username is invalid!"),
    ("tomsmith", "", "Your password is invalid!"),

])
def test_login_varios_casos(page: Page, usuario, clave, mensaje):
    page.goto("https://the-internet.herokuapp.com/login", timeout=60000)
    page.locator("#username").fill(usuario)
    page.locator("#password").fill(clave)
    page.locator("button[type='submit']").click()
    expect(page.locator("#flash")).to_contain_text(mensaje, timeout=10000)