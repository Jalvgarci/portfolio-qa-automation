import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def sesion_logueada(page: Page):
    login = LoginPage(page)
    login.abrir()
    login.login("tomsmith", "SuperSecretPassword!")
    return page