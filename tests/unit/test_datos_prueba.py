from datetime import date

import pytest

from utils.datos_prueba import siguiente_dia_laborable


@pytest.mark.parametrize(
    "desde, esperado",
    [
        (date(2026, 11, 23), date(2026, 11, 23)),  # lunes -> el mismo lunes
        (date(2026, 11, 27), date(2026, 11, 27)),  # viernes -> el mismo viernes
        (date(2026, 11, 28), date(2026, 11, 30)),  # sábado -> lunes
        (date(2026, 11, 29), date(2026, 11, 30)),  # domingo -> lunes
        (date(2027, 1, 2), date(2027, 1, 4)),      # sábado -> lunes, cambiando de año
    ],
    ids=[
        "lunes_mismo_dia",
        "viernes_mismo_dia",
        "sabado_pasa_a_lunes",
        "domingo_pasa_a_lunes",
        "cambio_de_anio",
    ],
)
def test_siguiente_dia_laborable(desde, esperado):
    assert siguiente_dia_laborable(desde) == esperado
