def capital_final(m, x, n):

    # Caso base
    if n == 0:
        return m
    # Caso recursivo
    return capital_final(m, x, n - 1) * (1 + x / 100)


if __name__ == "__main__":
    print("=== Inversión de capital ===\n")

    capital_inicial = 1000
    tasa_interes = 5  
    anios = 3

    resultado = capital_final(capital_inicial, tasa_interes, anios)
    print(f"Capital inicial: {capital_inicial}")
    print(f"Tasa de interés anual: {tasa_interes}%")
    print(f"Años: {anios}")
    print(f"Capital final: {resultado:.2f}\n")

    print("=== Verificación año por año ===")
    capital = capital_inicial
    print(f"Año 0: {capital:.2f}")
    for anio in range(1, anios + 1):
        capital *= (1 + tasa_interes / 100)
        print(f"Año {anio}: {capital:.2f}")

    print("\n=== Prueba interactiva ===")
    try:
        m = float(input("Ingrese el capital inicial (m): "))
        x = float(input("Ingrese la tasa de interés anual (%): "))
        n = int(input("Ingrese el número de años (n): "))

        resultado = capital_final(m, x, n)
        print(f"\nEl capital luego de {n} años será: {resultado:.2f}")
    except ValueError:
        print("Error: debe ingresar valores numéricos válidos.")