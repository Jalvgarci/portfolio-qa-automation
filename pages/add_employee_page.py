from playwright.sync_api import Page
from utils.datos_prueba import generar_id_empleado



class AltaEmpleado:
    def __init__(self, page: Page):
        self.page = page
        self.nombre_empleado = page.get_by_placeholder("First Name")
        self.apellido1_empleado = page.get_by_placeholder("Middle Name")
        self.apellido2_empleado = page.get_by_placeholder("Last Name")
        self.id_empleado = page.locator(".oxd-input-group").filter(has_text="Employee Id").locator("input")
        self.interruptor_login = page.locator(".oxd-switch-input")
        self.usuario_empleado = page.locator(".oxd-input-group").filter(has_text="Username").locator("input")
        self.empleado_pass = page.locator(".oxd-input-group").filter(has=self.page.get_by_text("Password", exact=True)).locator("input")
        self.empleado_confirmar_pass = page.locator(".oxd-input-group").filter(has=self.page.get_by_text("Confirm Password", exact=True)).locator("input")
        self.boton_alta_empleado = page.get_by_role("button", name="Save")
        
    def informar_datos_empleado (self, nombre_empleado, apellido1_empleado, apellido2_empleado):    
        self.nombre_empleado.fill(nombre_empleado)
        self.apellido1_empleado.fill(apellido1_empleado)
        self.apellido2_empleado.fill(apellido2_empleado)

    def informar_id(self, id_empleado):
        self.id_empleado.fill(id_empleado)
    
    
    def activar_creacion_usuario(self): #activar interruptor para creación de usuario
        self.interruptor_login.click()

    def informar_credenciales(self, usuario, clave):
        #usuario_nuevo = f"qa{id_empleado}"
        self.usuario_empleado.fill(usuario)
        self.empleado_pass.fill(clave)
        self.empleado_confirmar_pass.fill(clave)
    def clicar_boton_save (self):
        self.boton_alta_empleado.click()
        
        
        

        
