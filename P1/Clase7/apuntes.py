recetas = {
    "Pastel de chocolate": ["harina", "azucar", "cacao", "huevos", "mantequilla"],
    "Flan": ["huevos", "leche condensada", "leche evaporada", "vainilla"],
    "Gelatina": ["grenetina", "azucar", "agua", "colorante"],
}


def buscar_postre(nombre):
    nombre_buscado = nombre.strip().lower()

    for postre in recetas:
        if postre.lower() == nombre_buscado:
            return postre

    return None


def mostrar_ingredientes(nombre):
    nombre = nombre.strip()
    postre = buscar_postre(nombre)

    if postre is None:
        print(f"El postre '{nombre}' no existe.")
        return

    ingredientes = recetas[postre]

    if not ingredientes:
        print(f"'{postre}' no tiene ingredientes registrados.")
        return

    print(f"Ingredientes de '{postre}':")

    for numero, ingrediente in enumerate(ingredientes, start=1):
        print(f"  {numero}. {ingrediente}")


def agregar_ingrediente(nombre, ingrediente):
    nombre = nombre.strip()
    ingrediente = ingrediente.strip()

    if not nombre or not ingrediente:
        print("El nombre del postre y el ingrediente no pueden estar vacios.")
        return

    postre = buscar_postre(nombre)

    if postre is None:
        postre = nombre
        recetas[postre] = []
        print(f"Postre '{postre}' creado.")

    if ingrediente.lower() in [x.lower() for x in recetas[postre]]:
        print(f"'{ingrediente}' ya estaba en '{postre}'.")
        return

    recetas[postre].append(ingrediente)
    print(f"Se agrego '{ingrediente}' a '{postre}'.")


def quitar_ingrediente(nombre, ingrediente=None):
    nombre = nombre.strip()
    postre = buscar_postre(nombre)

    if postre is None:
        print(f"El postre '{nombre}' no existe.")
        return

    if ingrediente is None:
        recetas[postre] = []
        print(f"Se eliminaron todos los ingredientes de '{postre}'.")
        return

    ingrediente = ingrediente.strip()

    for elemento in recetas[postre]:
        if elemento.lower() == ingrediente.lower():
            recetas[postre].remove(elemento)
            print(f"Se elimino '{elemento}' de '{postre}'.")
            return

    print(f"'{ingrediente}' no estaba en '{postre}'.")


def menu():
    while True:
        print("\n--- Gestor de postres ---")
        print("1. Ver ingredientes de un postre")
        print("2. Agregar ingrediente")
        print("3. Eliminar un ingrediente")
        print("4. Eliminar todos los ingredientes de un postre")
        print("5. Salir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            nombre = input("Nombre del postre: ").strip()

            if nombre:
                mostrar_ingredientes(nombre)

        elif opcion == "2":
            nombre = input("Nombre del postre: ").strip()
            ingrediente = input("Ingrediente a agregar: ").strip()

            if nombre and ingrediente:
                agregar_ingrediente(nombre, ingrediente)
            else:
                print("Debes escribir un nombre de postre e ingrediente validos.")

        elif opcion == "3":
            nombre = input("Nombre del postre: ").strip()
            ingrediente = input("Ingrediente a eliminar: ").strip()

            if nombre and ingrediente:
                quitar_ingrediente(nombre, ingrediente)
            else:
                print("Debes escribir un nombre de postre e ingrediente validos.")

        elif opcion == "4":
            nombre = input("Nombre del postre: ").strip()

            if nombre:
                quitar_ingrediente(nombre)

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opcion invalida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
