nombre_archivo = input("Ingresa un nombre de archivo: ")

archivo = open(nombre_archivo)

lista = []

for linea in archivo:
    palabras = linea.split()

    for palabra in palabras:
        if palabra not in lista:
            lista.append(palabra)

lista.sort()

print(lista)