from playwright.sync_api import Page, expect

def test_titulo_pagina(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    assert page.title() == "The Internet"
    


def test_marcar_checkbox(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox = page.locator("#checkboxes input").nth(0)
    checkbox.check()
    expect(checkbox).to_be_checked()

def test_login_formulario(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    expect(page.locator(".flash.success")).to_be_visible()