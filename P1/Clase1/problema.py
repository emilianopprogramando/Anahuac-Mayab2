import numpy as np

# Declaración del arreglo de asientos
asientos = np.array([1, 1, 0, 1, 0, 0, 1, 1, 1, 0])

# Buscar el primer asiento vacío
for i in range(10):
    if asientos[i] == 0:
        print("El primer asiento vacío es el número:", i + 1)
        break