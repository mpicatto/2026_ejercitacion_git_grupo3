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