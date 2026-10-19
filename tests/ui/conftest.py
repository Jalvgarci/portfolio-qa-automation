import pytest
import re
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.saucedemo_login_page import SauceDemoLoginPage
from playwright.sync_api import Page, expect
from utils.datos_prueba import generar_id_empleado
from pages.orange_sidebar import MenuLateralPage
from pages.add_employee_page import AltaEmpleado
from pages.orange_pim_page import PimPage
from pages.orange_login_page import OrangeLoginPage

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

@pytest.fixture
def empleado_creado(page: Page):
    id_empleado = generar_id_empleado()
    usuario_nuevo = f"qa{id_empleado}"
    clave_nueva = "Pass1234"
#login como ADMIN
    login = OrangeLoginPage(page)
    login.abrir()
    login.login("Admin", "admin123")
    expect(page).to_have_url(re.compile("dashboard"), timeout=30000)

    menu = MenuLateralPage(page)
    menu.ir_a_pim()
    expect(page).to_have_url(re.compile("pim"), timeout=30000)

    pim = PimPage(page)
    pim.clic_add()
    expect(page).to_have_url(re.compile("addEmployee"), timeout=30000)

    crear_empleado = AltaEmpleado(page)
    crear_empleado.informar_datos_empleado("Zacarias", "Ronalda", "Smith")
    crear_empleado.informar_id(id_empleado)
    crear_empleado.activar_creacion_usuario()

    crear_empleado.informar_credenciales(usuario_nuevo, clave_nueva)
    crear_empleado.clicar_boton_save()
    expect(page).to_have_url(re.compile("viewPersonalDetails"), timeout=30000)
    
    return {"usuario": usuario_nuevo, "clave": clave_nueva}

@pytest.fixture
def pagina_empleado(browser):
    contexto = browser.new_context()
    yield contexto.new_page()
    contexto.close()