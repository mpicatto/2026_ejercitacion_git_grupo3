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