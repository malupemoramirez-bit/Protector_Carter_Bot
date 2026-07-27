from catalogo import buscar_vehiculo

def responder(texto):

    texto = texto.lower()
    vehiculo = buscar_vehiculo(texto)

    if vehiculo:
        return (
            f"¡Perfecto! Tenemos Protector Carter para {vehiculo['nombre']}.\n\n"
            f"💰 Precio con instalación en Barranquilla: ${vehiculo['precio_barranquilla']:,} COP.\n"
            f"🚚 Precio con envío a ciudades capitales: ${vehiculo['precio_capital']:,} COP.\n"
            f"📦 Precio con envío a municipios: ${vehiculo['precio_municipio']:,} COP.\n\n"
            "En un momento te compartiré las fotografías de esta referencia.\n\n"
            "¿En qué ciudad te encuentras? Así te indico la opción de instalación o envío disponible."
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