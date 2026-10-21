temperaturas = [
    35, 35, 37, 36, 34, 35, 36, 34, 34, 34,
    35, 35, 34, 35, 34, 34, 34, 34, 34, 34,
    35, 34, 35, 34, 34, 35, 35, 34, 34, 33
]

registros = []
for dia in range(1, 31):
    registros.append([temperaturas[dia - 1], str(dia) + " sep"])


def bubble_sort(datos, ascendente):
    n = len(datos)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if ascendente:
                intercambiar = datos[j][0] > datos[j + 1][0]
            else:
                intercambiar = datos[j][0] < datos[j + 1][0]

            if intercambiar:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]


ascendente = registros.copy()
descendente = registros.copy()

bubble_sort(ascendente, True)
bubble_sort(descendente, False)

print("TEMPERATURAS EN ORDEN ASCENDENTE")
for temperatura, fecha in ascendente:
    print(f"{temperatura:.1f} °C, {fecha}")

print("\nTEMPERATURAS EN ORDEN DESCENDENTE")
for temperatura, fecha in descendente:
    print(f"{temperatura:.1f} °C, {fecha}")