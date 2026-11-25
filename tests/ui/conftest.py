import datetime
import html
import re
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect
from pages.orange_login_page import OrangeLoginPage
from pages.orange_sidebar import MenuLateralPage
from pages.orange_pim_page import PimPage
from pages.add_employee_page import AltaEmpleado
from utils.datos_prueba import generar_id_empleado

RAIZ = Path(__file__).resolve().parents[2]
FICHERO_DATOS = RAIZ / "datos_ultima_ejecucion.txt"
_datos_por_test = {}


def pytest_bdd_before_scenario(request, feature, scenario):
    # Guardamos el texto del .feature y el momento de inicio.
    request.node._nombre_escenario = scenario.name
    request.node._inicio_escenario = datetime.datetime.now()


@pytest.fixture
def contexto(request):
    datos = {}
    yield datos

    # Regla acordada: si no se genero ningun dato, no tocamos el fichero anterior.
    if not datos:
        return

    nombre = getattr(request.node, "_nombre_escenario", request.node.name)
    inicio = getattr(request.node, "_inicio_escenario", datetime.datetime.now())

    lineas = [
        f"Ejecucion: {inicio.strftime('%d/%m/%Y %H:%M:%S')}",
        f"Escenario: {nombre}",
        "",
    ]
    lineas += [f"{clave}: {valor}" for clave, valor in sorted(datos.items())]
    contenido = "\n".join(lineas) + "\n"

    FICHERO_DATOS.write_text(contenido, encoding="utf-8")
    _datos_por_test[request.node.nodeid] = contenido


def pytest_html_results_table_html(report, data):
    # pytest-html pasa 3 veces por el mismo test (setup, call, teardown).
    # Solo queremos una copia del bloque.
    if report.when != "call":
        return

    contenido = _datos_por_test.get(report.nodeid)
    if not contenido:
        return

    data.append(
        "<div><b>Datos de la ultima ejecucion</b><pre>"
        + html.escape(contenido)
        + "</pre></div>"
    )


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