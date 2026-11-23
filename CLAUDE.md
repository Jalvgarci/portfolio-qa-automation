# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Proyecto

Portfolio de automatización de pruebas en Python: Playwright (API síncrona, Chromium) + Pytest + pytest-bdd, con Page Object Model. El código, los identificadores, los comentarios, los pasos Gherkin y los mensajes de commit están en **español**; hay que mantener esa convención.

El trabajo activo es el flujo de OrangeHRM contra la demo pública `https://opensource-demo.orangehrmlive.com` (administrador `Admin` / `admin123`). Todo lo que hay en `pages/anteriores/` y `tests/anteriores/` son ejercicios anteriores archivados (the-internet.herokuapp.com, SauceDemo, API de reqres.in); no se amplían salvo que se pida.

## Comandos (Windows / PowerShell)

```powershell
py -m venv venv; venv\Scripts\activate
pip install -r requirements.txt
playwright install

pytest -v                                                     # todo lo que hay en tests/
pytest tests\ui\test_vacaciones_bdd.py -v --headed            # escenario de vacaciones de OrangeHRM, con el navegador visible
pytest tests\ui\test_orange_admin.py::test_alta_empleado -v   # un único test
pytest tests\anteriores\api -v                                # solo los tests de API
```

`pytest.ini` añade siempre `--screenshot=only-on-failure --video=retain-on-failure --html=report.html --self-contained-html` y define `pythonpath = .` (para que los imports `from pages...` / `from utils...` funcionen desde los tests). Las evidencias de los fallos van a `test-results/` y el informe a `report.html` (los dos están en `.gitignore`). No hay linter ni formatter configurado.

El CI (`.github/workflows/tests.yml`, Python 3.14, ubuntu) ejecuta `pytest -v --ignore=tests/ui --ignore=tests/anteriores/ui/ejercicios_iniciales`. **Los tests de OrangeHRM no se ejecutan en el CI**: hay que comprobarlos en local.

## Arquitectura

- **`pages/`**: una clase por pantalla o componente (`OrangeLoginPage`, `MenuLateralPage` para el menú lateral, `BarraSuperior` para la barra superior y el cierre de sesión, `PimPage`, `AltaEmpleado`, `AsignarDiasPage`, `ApplyLeavePage`, `MyLeavePage`, `ViewLeaveListPage`, ...). Los locators se definen en `__init__` y los métodos son verbos en español (`abrir`, `informar_*`, `clic_*`, `seleccionar_*`). Las filas de las tablas se localizan con `.oxd-table-row` filtrando por el apellido único del empleado (`fila_de(apellido)`). Los métodos que envían datos al servidor envuelven el clic en `page.expect_response(...)` y devuelven la respuesta, para que el test pueda comprobar `respuesta.ok`.
- **`tests/ui/features/vacaciones.feature`** + **`tests/ui/test_vacaciones_bdd.py`**: el escenario BDD principal, de principio a fin. El administrador da de alta un empleado con usuario de acceso → le asigna días de vacaciones → el empleado inicia sesión y solicita vacaciones → la solicitud aparece como "Pending Approval" en My Leave → el administrador la aprueba en View Leave List. Los pasos comparten datos a través del fixture `contexto`, un diccionario definido en `tests/ui/conftest.py`: `id_empleado`, `apellido`, `usuario`, `clave`, `tipo_ausencia`, `dias`. Los pasos que se repiten ("inicio sesión como administrador", "cierro sesión") usan `@step`.
- **`utils/datos_prueba.py`**: genera datos de prueba únicos (`generar_id_empleado`, `generar_apellido_unico`). La demo es compartida y se reinicia periódicamente, así que cada ejecución tiene que crear sus propios datos con nombres únicos en lugar de depender de registros existentes.
- `tests/ui/test_orange_admin.py`, `tests/ui/test_orange_empleado.py` y los fixtures `empleado_creado` / `pagina_empleado` son versiones anteriores, sin BDD, de partes del mismo flujo.

## Cosas a tener en cuenta

- La demo es lenta: las comprobaciones usan `expect(...)` con `timeout=30000`, y `OrangeLoginPage.abrir` usa un timeout de 60 s en el `goto`. Mejor `expect` con una expresión regular de la URL o un texto visible que pausas fijas.
- Campos de fecha: `ApplyLeavePage.informar_fechas` lee el `placeholder` del campo para construir el formato de fecha; no hay que escribir uno fijo.
## Convenciones del proyecto (aprendidas con errores reales)

### Diseño
- Un Page Object por pantalla real. Lo común a todas las pantallas (menú lateral, barra superior) va en su propio componente.
- Los datos de prueba se generan una sola vez por escenario, se guardan en `contexto` y se pasan como argumentos. Los Page Objects no generan ni fijan datos (por ejemplo, el tipo de ausencia se pasa como parámetro).
- Cada test o paso `Then` necesita una comprobación real con `expect`. Un test sin comprobación pasa en verde sin probar nada. Que algo desaparezca de pantalla no prueba que se hizo lo correcto.

### Selectores
- Preferencia: `data-test`, luego `get_by_role` / `get_by_label` / `get_by_placeholder`, y por último `#id` o `.clase`.
- No inventar selectores. Si no está verificado en el HTML real, pídeme el HTML (F12) antes de escribirlo.
- OrangeHRM: los campos se localizan con `.oxd-input-group` filtrado por su etiqueta con `get_by_text(..., exact=True)`. Los desplegables son propios: clic en `.oxd-select-text` y luego `get_by_role("option")`.
- `strict mode violation` significa que el selector encuentra varios elementos: hay que concretarlo (por ejemplo, con `exact=True`).
- Comprobar con `expect(...)`, que espera y reintenta, no con lecturas directas como `.count()`.

### pytest-bdd
- El texto del paso debe coincidir carácter a carácter con el del `.feature`.
- Cada paso se define una sola vez.
- Los pasos solo valen en el módulo que llama a `scenarios()` o en un `conftest.py`.
- `Given` y `When` para acciones; `Then` solo para comprobaciones.

### Datos de la demo OrangeHRM
- Tipos de ausencia: `CAN - Bereavement`, `CAN - FMLA`, `CAN - Matternity` (la errata es de la demo), `CAN - Personal`, `CAN - Vacation`.
- El periodo de ausencias es todo 2026. Al informar la fecha de inicio, la de fin se rellena sola.
- Solo se pueden pedir vacaciones en días laborables.

### Git
- No hacer commit ni push sin que yo lo pida.
- Commits locales frecuentes y un solo `push` al final de una tanda, porque cada `push` lanza GitHub Actions.

### Antes de dar algo por terminado
- Ejecutar el test afectado y confirmar que pasa. `ERROR at setup` significa que falló una fixture, no el test.
- No dejar `page.pause()` en el código.