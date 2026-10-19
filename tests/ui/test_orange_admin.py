import re
import pytest
from playwright.sync_api import Page, expect
from pages.orange_login_page import OrangeLoginPage
from pages.orange_sidebar import MenuLateralPage
from pages.orange_pim_page import PimPage
from pages.add_employee_page import AltaEmpleado
from utils.datos_prueba import generar_id_empleado

@pytest.mark.parametrize("usuario, clave, nombre_empleado, apellido1_empleado,apellido2_empleado", [("Admin", "admin123","Zacarias","Ronalda","Smith")])
def test_alta_empleado(page: Page, usuario, clave, nombre_empleado, apellido1_empleado, apellido2_empleado):
    login = OrangeLoginPage(page)
    login.abrir()
    login.login(usuario, clave)
    expect(page).to_have_url(re.compile("dashboard"), timeout=30000)

    menu = MenuLateralPage(page)
    menu.ir_a_pim()
    expect(page).to_have_url(re.compile("pim"), timeout=30000)

    pim = PimPage(page)
    pim.clic_add()
    expect(page).to_have_url(re.compile("addEmployee"), timeout=30000)

    crear_empleado = AltaEmpleado(page)
    crear_empleado.informar_datos_empleado(nombre_empleado, apellido1_empleado, apellido2_empleado)
    id_empleado = generar_id_empleado()
    crear_empleado.informar_id(id_empleado)
    crear_empleado.activar_creacion_usuario()
    usuario = f"qa{id_empleado}"
    clave = "Pass1234"
    crear_empleado.informar_credenciales(usuario, clave)
    crear_empleado.clicar_boton_save()
    expect(page).to_have_url(re.compile("viewPersonalDetails"), timeout=30000)

#@pytest.mark.parametrize("usuario, clave", [("Admin", "admin123")])
#def test_solicitar_vacaciones (page: Page, usuario, clave):

