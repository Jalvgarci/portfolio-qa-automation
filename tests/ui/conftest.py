import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.saucedemo_login_page import SauceDemoLoginPage

@pytest.fixture
def sesion_logueada(page: Page):
    login = LoginPage(page)
    login.abrir()
    login.login("tomsmith", "SuperSecretPassword!")
    return page
#login web saucedemo
@pytest.fixture
def inventario_logueado(page: Page):
    login = SauceDemoLoginPage(page)
    login.abrir()
    login.login("standard_user", "secret_sauce")
    return page