import json

# ==========================
# CATALOGO DE VEHICULOS
# ==========================

with open("vehiculos.json", "r", encoding="utf-8") as archivo:
    VEHICULOS = json.load(archivo)

# ==========================
# PREGUNTAS FRECUENTES
# ==========================

with open("preguntas.json", "r", encoding="utf-8") as archivo:
    PREGUNTAS = json.load(archivo)


def buscar_vehiculo(texto):

    texto = texto.lower()

    for clave, datos in VEHICULOS.items():

        if clave.lower() in texto:
            return datos

    return None


def buscar_pregunta(texto):

    texto = texto.lower()

    for categoria in PREGUNTAS.values():

        for pregunta in categoria:

            for palabra in pregunta["keywords"]:

                if palabra.lower() in texto:

                    return pregunta["respuesta"]

    return None