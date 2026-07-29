import json
from catalogo import buscar_vehiculo

# ===============================
# CARGAR PREGUNTAS
# ===============================

with open("preguntas.json", "r", encoding="utf-8") as archivo:
    PREGUNTAS = json.load(archivo)


# ===============================
# BUSCAR PREGUNTA
# ===============================

def buscar_pregunta(texto):

    texto = texto.lower()

    for categoria in PREGUNTAS.values():

        for item in categoria:

            for palabra in item["keywords"]:

                if palabra.lower() in texto:
                    return item["respuesta"]

    return None


# ===============================
# RESPONDER
# ===============================

def responder(texto):

    texto = texto.lower()

    # ===============================
    # 1. BUSCAR VEHÍCULO
    # ===============================

    vehiculo = buscar_vehiculo(texto)

    if vehiculo:

        mensaje = (
            f"✅ ¡Perfecto! Tenemos Protector Carter para {vehiculo['nombre']}.\n\n"

            f"💰 Precio con instalación en Barranquilla: ${vehiculo['precio_barranquilla']:,} COP.\n"
            f"🚚 Precio con envío a ciudades capitales: ${vehiculo['precio_capital']:,} COP.\n"
            f"📦 Precio con envío a municipios: ${vehiculo['precio_municipio']:,} COP.\n\n"

            "📸 A continuación te compartiré fotografías de esta referencia.\n\n"

            "🔨 Cada Protector Carter se fabrica específicamente para el vehículo solicitado, garantizando un ajuste perfecto.\n\n"

            "Actualmente contamos con más de 300 referencias, por lo que fabricamos cada pedido una vez confirmado.\n\n"

            "💳 Para iniciar la fabricación solicitamos un anticipo del 50%.\n\n"

            "✅ El 50% restante se cancela al momento de la instalación en Barranquilla o antes del despacho de la guía para envíos nacionales.\n\n"

            "📍 ¿En qué ciudad te encuentras?"
        )

        return mensaje, vehiculo["imagenes"]

    # ===============================
    # 2. BUSCAR PREGUNTA
    # ===============================

    respuesta = buscar_pregunta(texto)

    if respuesta:
        return respuesta, None

    # ===============================
    # 3. SALUDOS
    # ===============================

    if any(saludo in texto for saludo in [

        "hola",
        "hola!",
        "holaaa",
        "buenas",
        "buen día",
        "buen dia",
        "buenos días",
        "buenos dias",
        "buenas tardes",
        "buenas noches",
        "hello",
        "hi",
        "hey",
        "qué tal",
        "que tal",
        "saludos"

    ]):

        return (

            "👋 ¡Bienvenido a Protector Carter!\n\n"
            "Somos fabricantes de Protectores Carter desde el año 2019.\n\n"
            "🚗 Indícanos la marca, línea y modelo de tu vehículo para enviarte la cotización."

        ), None

    # ===============================
    # 4. PRECIO
    # ===============================

    if "precio" in texto:

        return (

            "Con gusto.\n\n"
            "Indícanos la marca, línea y modelo de tu vehículo para enviarte la cotización."

        ), None

    # ===============================
    # 5. GRACIAS
    # ===============================

    if "gracias" in texto:

        return (

            "Con mucho gusto. Estamos atentos para ayudarte."

        ), None

    # ===============================
    # 6. RESPUESTA GENERAL
    # ===============================

    return (

        "Con gusto te ayudamos.\n\n"
        "🚗 Indícanos la marca, línea y modelo de tu vehículo."

    ), None