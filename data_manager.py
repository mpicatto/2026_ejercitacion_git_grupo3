
inventario = []

def inicializar_datos():
    """Carga 3 diccionarios de ejemplo en la lista global inventario."""
    global inventario
    inventario = [
        {"especie": "Roble", "estado": "Saludable", "ubicacion": "Parque Central"},
        {"especie": "Pino",  "estado": "Saludable", "ubicacion": "Calle 5"},
        {"especie": "Arce",  "estado": "Enfermo",   "ubicacion": "Plaza Norte"},
    ]

def obtener_inventario():
    """Retorna una copia del inventario."""
    return list(inventario)

if __name__ == "__main__":
    inicializar_datos()
    print(obtener_inventario())