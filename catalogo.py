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

    print("================================")
    print("BUSCANDO:", texto)

    for nombre_categoria, categoria in PREGUNTAS.items():

        print("Categoria:", nombre_categoria)

        for pregunta in categoria:

            for palabra in pregunta["keywords"]:

                if palabra.lower() in texto:

                    print("ENCONTRO:", palabra)

                    return pregunta["respuesta"]

    print("NO ENCONTRO NADA")

    return None