import random
import time
import string
from datetime import date, timedelta


def generar_id_empleado():
    return time.strftime("%d%H%M%S") + str(random.randint(10, 99))

def generar_apellido_unico():
    return "Test" + "".join(random.choices(string.ascii_lowercase, k=6))

def siguiente_dia_laborable(desde=None):
    fecha = desde or date.today()
    while fecha.weekday() >= 5:      # 5 = sábado, 6 = domingo
        fecha += timedelta(days=1)
    return fecha

def dia_laborable_futuro(desde=None):
    hoy = desde or date.today()
    return siguiente_dia_laborable(hoy + timedelta(days=1))
