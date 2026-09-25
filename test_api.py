import requests

def test_obtener_usuario():
    respuesta = requests.get("https://reqres.in/api/users/2")
    datos = respuesta.json()

    assert respuesta.status_code == 200
    assert datos["data"]["id"] == 2
    assert "email" in datos["data"]

def test_crear_usuario():
    datos_nuevos = {
        "name": "Jaime",
        "job": "QA Automation Engineer"
    }

    respuesta = requests.post("https://reqres.in/api/users", json=datos_nuevos)
    resultado = respuesta.json()

    assert respuesta.status_code == 201
    assert resultado["name"] == "Jaime"
    assert resultado["job"] == "QA Automation Engineer"
    assert "id" in resultado
    