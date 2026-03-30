from data_manager import listar_arboles

arboles = []

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar árbol")
    print("2. Ver árbol")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Elegí una opción: ")
    
    if opcion == "1":
        print("Función agregar árbol (todavía no hecha)")

    elif opcion == "2":
        listar_arboles(arboles)

    elif opcion == "3":
        print("Saliendo...")

    else:
        print("Opción invalida")

arboles = []

def registrar_arbol():
    especie = input("Especie del árbol: ")
    ubicacion = input("Ubicación: ")
    altura = input("Altura aproximada (m): ")

    arbol = {
        "especie": especie,
        "ubicacion": ubicacion,
        "altura": altura
    }

    arboles.append(arbol)
    print(" Árbol registrado correctamente\n")


def listar_arboles():
    if not arboles:
        print("No hay árboles registrados\n")
        return

    print("\n Lista de árboles:")
    for i, a in enumerate(arboles, 1):
        print(f"{i}. Especie: {a['especie']} | Ubicación: {a['ubicacion']} | Altura: {a['altura']} m")
    print()


def menu():
    while True:
        print("=== Eco-Tracker Las Varillas ===")
        print("1. Registrar árbol")
        print("2. Listar árboles")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_arbol()
        elif opcion == "2":
            listar_arboles()
        elif opcion == "3":
            print(" Saliendo...")
            break
        else:
            print("❌ Opción inválida\n")


if __name__ == "__main__":
    menu()
