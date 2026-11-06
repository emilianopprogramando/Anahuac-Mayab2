
tabla = [None] * 10

def insertar(numero):
    posicion = numero % 10

    while tabla[posicion] is not None:
        posicion = (posicion + 1) % 10

    tabla[posicion] = numero

def buscar(numero):
    posicion = numero % 10

    for i in range(10):
        if tabla[posicion] == numero:
            return posicion

        if tabla[posicion] is None:
            break

        posicion = (posicion + 1) % 10

    return -1


# Solicitar los valores
for i in range(6):
    numero = int(input("Ingresa un numero: "))
    insertar(numero)

# Mostrar el arreglo
print("\nTabla hash:")
for i in range(10):
    print("Posicion", i, ":", tabla[i])

# Buscar un numero
numero = int(input("\nNumero a buscar: "))
posicion = buscar(numero)

if posicion != -1:
    print("Numero encontrado en la posicion", posicion)
else:
    print("Numero no encontrado")
