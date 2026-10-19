from playwright.sync_api import Page




class AltaEmpleado:
    def __init__(self, page: Page):
        self.page = page
        self.nombre_empleado = page.get_by_placeholder("First Name")
        self.segundo_nombre = page.get_by_placeholder("Middle Name")
        self.apellido = page.get_by_placeholder("Last Name")
        self.id_empleado = page.locator(".oxd-input-group").filter(has_text="Employee Id").locator("input")
        self.interruptor_login = page.locator(".oxd-switch-input")
        self.usuario_empleado = page.locator(".oxd-input-group").filter(has_text="Username").locator("input")
        self.empleado_pass = page.locator(".oxd-input-group").filter(has=self.page.get_by_text("Password", exact=True)).locator("input")
        self.empleado_confirmar_pass = page.locator(".oxd-input-group").filter(has=self.page.get_by_text("Confirm Password", exact=True)).locator("input")
        self.boton_alta_empleado = page.get_by_role("button", name="Save")
        
    def informar_datos_empleado (self, nombre_empleado, segundo_nombre, apellido):    
        self.nombre_empleado.fill(nombre_empleado)
        self.segundo_nombre.fill(segundo_nombre)
        self.apellido.fill(apellido)

    def informar_id(self, id_empleado):
        self.id_empleado.fill(id_empleado)
    
    
    def activar_creacion_usuario(self): #activar interruptor para creación de usuario
        self.interruptor_login.click()

    def informar_credenciales(self, usuario, clave):
        self.usuario_empleado.fill(usuario)
        self.empleado_pass.fill(clave)
        self.empleado_confirmar_pass.fill(clave)
    def clicar_boton_save (self):
        self.boton_alta_empleado.click()
        
        
        

        
