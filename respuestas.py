from catalogo import buscar_vehiculo

def responder(texto):

    texto = texto.lower()
    vehiculo = buscar_vehiculo(texto)

    if vehiculo:
        return (
            f"Perfecto. Tenemos Protector Carter para {vehiculo['nombre']}.\n\n"
            f"{vehiculo['pregunta']}"
        )
    if "hola" in texto:
        return "Hola 👋 Bienvenido a Protector Carter. ¿Qué vehículo deseas proteger?"

    if "hilux" in texto:
        return (
            "Perfecto. Tenemos protector para Toyota Hilux.\n\n"
            "Te mostraré las fotografías de la referencia disponible."
        )

    if "precio" in texto:
        return (
            "Con gusto.\n"
            "Indícanos la marca, línea y modelo de tu vehículo para enviarte la cotización."
        )

    if "envio" in texto:
        return (
            "Sí. Despachamos a toda Colombia."
        )

    if "gracias" in texto:
        return (
            "Con mucho gusto. Estamos atentos."
        )

    return (
        "Con gusto te ayudamos.\n\n"
        "¿Cuál es la marca y modelo de tu vehículo?"
    )