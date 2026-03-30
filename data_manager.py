def listar_arboles(arboles):
    if len(arboles) == 0:
        print("No hay árboles cargados.")
        return
        
    for i, arbol in enumerate(arboles, start=1):
        print(f"\nÁrbol {i}")
        print(f"ID: {arbol['id']}")
        print(f"Especie: {arbol['especie']}")
        print(f"Altura: {arbol['altura']} metros")
        print("-" * 20)
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
