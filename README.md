# QA Automation Portfolio
[![Tests](https://github.com/Jalvgarci/portfolio-qa-automation/actions/workflows/tests.yml/badge.svg)](https://github.com/Jalvgarci/portfolio-qa-automation/actions/workflows/tests.yml)
🇪🇸 [Español](#-español) · 🇬🇧 [English](#-english)

---

## 🇪🇸 Español

### Sobre el proyecto

Portfolio de automatización de pruebas construido como parte de mi transición desde el testing funcional ( 20 años de experiencia en análisis, diseño de planes de prueba y gestión de incidencias) hacia la automatización de pruebas de UI y API.

Las pruebas se ejecutan contra aplicaciones públicas pensadas para practicar testing:

- [the-internet.herokuapp.com](https://the-internet.herokuapp.com) para pruebas de interfaz de usuario.
- [reqres.in](https://reqres.in) para pruebas de API REST.

### Tecnologías

| Herramienta | Uso |
|---|---|
| Python 3 | Lenguaje de los tests |
| Playwright | Automatización de navegador (Chromium) |
| Pytest | Ejecución y organización de los tests |
| Requests | Pruebas de API REST |
| Git / GitHub | Control de versiones |

### Qué cubre

- **Pruebas de UI** con Playwright: verificación de contenido, casillas de verificación, desplegables, formularios y autenticación básica HTTP.
- **Pruebas parametrizadas**: un mismo test de login ejecutado con varios juegos de datos (credenciales válidas, contraseña incorrecta, usuario inexistente, campos vacíos).
- **Page Object Model**: los selectores viven en una clase por página (`pages/`), no repartidos por los tests.
- **Pruebas de API**: peticiones GET y POST, validación de códigos de estado (200, 201) y caso negativo (404).
- **Evidencias automáticas**: captura de pantalla y vídeo cuando un test falla.

### Estructura

```
├── pages/                  # Page Objects
│   └── login_page.py
├── tests/
│   ├── ui/                 # Tests con navegador
│   └── api/                # Tests de API
├── pytest.ini              # Configuración de Pytest
└── README.md
```

### Cómo ejecutarlo

Requisitos: Python 3 y Git. Comandos para Windows (PowerShell):

```powershell
git clone https://github.com/Jalvgarci/portfolio-qa-automation.git
cd portfolio-qa-automation

py -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
playwright install

pytest -v
```

Opciones útiles:

```powershell
pytest tests\api -v          # solo tests de API
pytest tests\ui -v --headed  # tests de UI viendo el navegador
```

Cuando un test falla, la captura y el vídeo se guardan en la carpeta `test-results/`.

### Próximos pasos

- Pruebas de rendimiento con Apache JMeter.
- Integración continua con GitHub Actions.
- Más Page Objects y fixtures compartidos.

### Contacto

- LinkedIn: [tu enlace aquí]

---

## 🇬🇧 English

### About the project

Test automation portfolio built as part of my move from functional testing (20+ years of experience in analysis, test plan design and defect reporting) into UI and API test automation.

Tests run against public applications designed for testing practice:

- [the-internet.herokuapp.com](https://the-internet.herokuapp.com) for UI tests.
- [reqres.in](https://reqres.in) for REST API tests.

### Tech stack

| Tool | Purpose |
|---|---|
| Python 3 | Test language |
| Playwright | Browser automation (Chromium) |
| Pytest | Test runner and organization |
| Requests | REST API testing |
| Git / GitHub | Version control |

### What it covers

- **UI tests** with Playwright: content checks, checkboxes, dropdowns, forms and HTTP basic authentication.
- **Parametrized tests**: one login test run against several data sets (valid credentials, wrong password, unknown user, empty fields).
- **Page Object Model**: selectors live in one class per page (`pages/`) instead of being scattered across tests.
- **API tests**: GET and POST requests, status code validation (200, 201) and a negative case (404).
- **Automatic evidence**: screenshot and video captured when a test fails.

### Structure

```
├── pages/                  # Page Objects
│   └── login_page.py
├── tests/
│   ├── ui/                 # Browser tests
│   └── api/                # API tests
├── pytest.ini              # Pytest configuration
└── README.md
```

### How to run it

Requirements: Python 3 and Git. Commands for Windows (PowerShell):

```powershell
git clone https://github.com/Jalvgarci/portfolio-qa-automation.git
cd portfolio-qa-automation

py -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
playwright install

pytest -v
```

Useful options:

```powershell
pytest tests\api -v          # API tests only
pytest tests\ui -v --headed  # UI tests with a visible browser
```

When a test fails, the screenshot and video are saved in the `test-results/` folder.

### Roadmap

- Performance testing with Apache JMeter.
- Continuous integration with GitHub Actions.
- More Page Objects and shared fixtures.

### Contact

- LinkedIn: [your link here]
