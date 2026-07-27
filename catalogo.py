import json


with open("vehiculos.json", "r", encoding="utf-8") as archivo:
    VEHICULOS = json.load(archivo)


def buscar_vehiculo(texto):

    texto = texto.lower()

    for clave, datos in VEHICULOS.items():

        if clave in texto:

            return datos

    return None