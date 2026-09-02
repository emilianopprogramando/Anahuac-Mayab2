def suma_cuadrados(n):

    # Caso base
    if n == 0:
        return 0
    # Caso recursivo
    return (n * n) + suma_cuadrados(n - 1)


def suma_cuadrados_contador(n, contador=None):

    if contador is None:
        contador = [0] 
    contador[0] += 1

    if n == 0:
        print(f"Total de llamadas realizadas: {contador[0]}")
        return 0

    return (n * n) + suma_cuadrados_contador(n - 1, contador)


def validar_entrada(n):

    if not isinstance(n, int):
        raise TypeError("La entrada debe ser un número entero.")
    if n <= 0 or n > 50:
        raise ValueError("La entrada debe ser un entero positivo <= 50.")
    return True


if __name__ == "__main__":
    
    print("=== Sumatoria de los n primeros números cuadrados ===\n")

    print(f"suma_cuadrados(3) = {suma_cuadrados(3)}   (esperado: 14)")
    print(f"suma_cuadrados(5) = {suma_cuadrados(5)}   (esperado: 55)\n")

    print("=== Conteo de iteraciones ===")
    suma_cuadrados_contador(3)
    suma_cuadrados_contador(5)

    print("\n=== Prueba interactiva ===")
    try:
        n = int(input("Ingrese un número entero positivo (<= 50): "))
        validar_entrada(n)
        print(f"La suma de los primeros {n} números al cuadrado es: {suma_cuadrados(n)}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")