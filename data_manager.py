inventario = []

def agregar_arbol(especie, estado, ubicacion):
    nuevo_arbol = {
    "especie": especie,
    "estado": estado,
    "ubicacion": ubicacion
    }

    inventario.append(nuevo_arbol)

agregar_arbol("Roble", "Saludable", "Plaza central")
agregar_arbol("Pino", "Seco", "Parque norte")

print(inventario)