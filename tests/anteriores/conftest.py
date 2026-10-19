import pytest
from playwright.sync_api import Page
from pages.anteriores.login_page import LoginPage
from pages.anteriores.saucedemo_login_page import SauceDemoLoginPage


@pytest.fixture
def sesion_logueada(page: Page):
    login = LoginPage(page)
    login.abrir()
    login.login("tomsmith", "SuperSecretPassword!")
    return page


@pytest.fixture
def inventario_logueado(page: Page):
    login = SauceDemoLoginPage(page)
    login.abrir()
    login.login("standard_user", "secret_sauce")
    return page