import random
import time
import string


def generar_id_empleado():
    return time.strftime("%d%H%M%S") + str(random.randint(10, 99))

def generar_apellido_unico():
    return "Test" + "".join(random.choices(string.ascii_lowercase, k=6))

   