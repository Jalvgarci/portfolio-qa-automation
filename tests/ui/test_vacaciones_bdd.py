import re
from pytest_bdd import scenarios, step, when, then
from playwright.sync_api import Page, expect
from pages.orange_login_page import OrangeLoginPage
from pages.orange_sidebar import MenuLateralPage
from pages.orange_pim_page import PimPage
from pages.orange_leave_page import LeavePage
from pages.orange_apply_leave_page import ApplyLeavePage
from pages.orange_my_leave_page import MyLeavePage
from pages.add_employee_page import AltaEmpleado
from pages.orange_detalle_empleado import DetalleEmpleado
from pages.orange_topbar import BarraSuperior
from utils.datos_prueba import generar_id_empleado
from pages.orange_leave_entitlements_page import AsignarDiasPage
from pages.orange_view_leave_list_page import ViewLeaveListPage
from utils.datos_prueba import generar_id_empleado, generar_apellido_unico

scenarios("features/vacaciones.feature")

ADMIN_USUARIO = "Admin"
ADMIN_CLAVE = "admin123"


@step("inicio sesión como administrador")
def login_admin(page: Page):
    login = OrangeLoginPage(page)
    login.abrir()
    login.login(ADMIN_USUARIO, ADMIN_CLAVE)
    expect(page).not_to_have_url(re.compile("auth/"), timeout=30000)


@when("doy de alta un empleado nuevo con usuario de acceso")
def alta_empleado(page: Page, contexto):
    id_empleado = generar_id_empleado()
    contexto["id_empleado"] = id_empleado
    contexto["apellido"] = generar_apellido_unico()
    contexto["usuario"] = f"qa{id_empleado}"
    contexto["clave"] = "Pass1234"

    MenuLateralPage(page).ir_a_pim()
    expect(page).to_have_url(re.compile("pim"), timeout=30000)
    PimPage(page).clic_add()
    expect(page).to_have_url(re.compile("addEmployee"), timeout=30000)

    alta = AltaEmpleado(page)
    alta.informar_datos_empleado("Zacarias", "Ronalda", contexto["apellido"])
    alta.informar_id(id_empleado)
    alta.activar_creacion_usuario()
    alta.informar_credenciales(contexto["usuario"], contexto["clave"])
    alta.clicar_boton_save()
    expect(page).to_have_url(re.compile("viewPersonalDetails"), timeout=30000)


@then("el empleado figura dado de alta")
def comprobar_alta(page: Page, contexto):
    detalle = DetalleEmpleado(page)
    expect(detalle.id_empleado).to_have_value(contexto["id_empleado"], timeout=30000)

@when("asigno días de vacaciones al empleado nuevo")
def asignar_dias(page: Page, contexto):
    contexto["tipo_ausencia"] = "CAN - Personal"   # el que uses de verdad
    contexto["dias"] = 30

    MenuLateralPage(page).ir_a_leave()
    asignacion = AsignarDiasPage(page)
    asignacion.abrir_formulario()
    asignacion.seleccionar_empleado(contexto["apellido"])
    expect(page.get_by_text("Invalid", exact=True)).to_have_count(0)
    asignacion.seleccionar_tipo(contexto["tipo_ausencia"])
    asignacion.asignar_dias(contexto["dias"])
    

@then("los días de vacaciones figuran asignados")
def comprobar_dias(page: Page, contexto):
    expect(page).to_have_url(re.compile("viewLeaveEntitlements"), timeout=30000)
    expect(page.get_by_text("(1) Record Found")).to_be_visible(timeout=30000)
    expect(page.get_by_text(f"Total {contexto['dias']}.00 Day(s)")).to_be_visible()


@step("cierro sesión")
def cerrar_sesion(page: Page):
    BarraSuperior(page).cerrar_sesion()
    expect(page).to_have_url(re.compile("auth/login"), timeout=30000)

@step("inicio sesión como empleado")
def login_empleado(page: Page, contexto):
    login = OrangeLoginPage(page)
    login.abrir()
    login.login(contexto["usuario"], contexto["clave"])
    expect(page).not_to_have_url(re.compile("auth/"), timeout=30000)

@when("el empleado solicita vacaciones")
def solicitar_vacaciones(page: Page):
    MenuLateralPage(page).ir_a_leave()
    expect(page).to_have_url(re.compile("leave"), timeout=30000)
    LeavePage(page).clic_apply()
    expect(page).to_have_url(re.compile("applyLeave"), timeout=30000)
    solicitud = ApplyLeavePage(page)
    solicitud.seleccionar_leave_type()
    solicitud.informar_fechas()
    expect(solicitud.fecha_fin).to_have_value(solicitud.fecha_hoy, timeout=30000)
    respuesta = solicitud.solicitar()
    assert respuesta.ok, f"La solicitud falló: {respuesta.status} {respuesta.url}"
    
@then("la solicitud figura pendiente de aprobación")
def comprobar_solicitud(page: Page, contexto):
    mis_ausencias = MyLeavePage(page)
    mis_ausencias.abrir()
    fila = mis_ausencias.fila_de(contexto["apellido"])
    expect(fila).to_contain_text(contexto["tipo_ausencia"], timeout=30000)
    expect(fila).to_contain_text("Pending Approval")

@step("cierro sesión")
def cerrar_sesion(page: Page):
    BarraSuperior(page).cerrar_sesion()
    expect(page).to_have_url(re.compile("auth/login"), timeout=30000)

@step("inicio sesión como administrador")
def login_admin(page: Page):
    login = OrangeLoginPage(page)
    login.abrir()
    login.login(ADMIN_USUARIO, ADMIN_CLAVE)
    expect(page).to_have_url(re.compile("dashboard"), timeout=30000)

@when("apruebo la solicitud de vacaciones del empleado")
def aprobar_solicitud(page: Page, contexto):
    MenuLateralPage(page).ir_a_leave()
    expect(page).to_have_url(re.compile("leave"), timeout=30000)
    listado_vacaciones= ViewLeaveListPage(page)
    fila = listado_vacaciones.fila_de(contexto["apellido"])
    expect(fila).to_contain_text(contexto["tipo_ausencia"], timeout=30000)
    expect(fila).to_contain_text("Pending Approval")
    listado_vacaciones.clic_aprobar(fila)

@then("la solicitud ya no figura como pendiente")
def comprobar_aprobacion(page: Page, contexto):
    listado_vacaciones = ViewLeaveListPage(page)
    fila = listado_vacaciones.fila_de(contexto["apellido"])
    expect(fila).to_have_count(0, timeout=30000)



