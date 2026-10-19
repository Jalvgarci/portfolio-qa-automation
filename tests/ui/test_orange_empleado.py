import re
from playwright.sync_api import expect
from pages.orange_login_page import OrangeLoginPage

def test_solicitud_vacaciones(pagina_empleado, empleado_creado):
    login = OrangeLoginPage(pagina_empleado)
    login.abrir()
    login.login(empleado_creado["usuario"], empleado_creado["clave"])
    expect(pagina_empleado).to_have_url(re.compile("dashboard"), timeout=30000)