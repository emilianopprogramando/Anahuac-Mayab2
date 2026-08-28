nombre_archivo = input("Ingresa un nombre de archivo: ")

archivo = open(nombre_archivo)

contador = 0

for linea in archivo:
    palabras = linea.split()

    if len(palabras) > 0 and palabras[0] == "From":
        print(palabras[1])
        contador = contador + 1

print("Hay", contador, "líneas en el archivo con la palabra From al inicio")