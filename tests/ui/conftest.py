import re
import pytest
from playwright.sync_api import Page, expect
from pages.orange_login_page import OrangeLoginPage
from pages.orange_sidebar import MenuLateralPage
from pages.orange_pim_page import PimPage
from pages.add_employee_page import AltaEmpleado
from utils.datos_prueba import generar_id_empleado

@pytest.fixture
def contexto():
    return {}

@pytest.fixture
def empleado_creado(page: Page):
    # Datos del empleado nuevo: se generan UNA sola vez
    id_empleado = generar_id_empleado()
    usuario_nuevo = f"qa{id_empleado}"
    clave_nueva = "Pass1234"

    # Login como Admin
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