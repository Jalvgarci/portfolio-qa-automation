from playwright.sync_api import Page, expect

def test_titulo_pagina(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    assert page.title() == "The Internet"
    


def test_marcar_checkbox(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox = page.locator("#checkboxes input").nth(0)
    checkbox.check()
    expect(checkbox).to_be_checked()

