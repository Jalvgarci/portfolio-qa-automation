import random
import time


def generar_id_empleado():
    return time.strftime("%d%H%M%S") + str(random.randint(10, 99))

   