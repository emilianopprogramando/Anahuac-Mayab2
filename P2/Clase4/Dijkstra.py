
inf = float('inf')
n = 6
vertices = ['A', 'B', 'C', 'D', 'E', 'F']

mat = [[inf] * n for _ in range(n)]

aristas = [
    (0, 1, 4),
    (0, 2, 2),
    (1, 2, 1),
    (1, 3, 5),
    (2, 4, 10),
    (3, 4, 3),
    (3, 5, 2),
    (4, 5, 1)
]

for origen, destino, peso in aristas:
    mat[origen][destino] = peso
    mat[destino][origen] = peso


def dijkstra(mat, origen):
    dist = [inf] * n
    visitado = [False] * n
    pred = [-1] * n

    dist[origen] = 0

    for i in range(n):
        u = -1
        min_dist = inf

        for j in range(n):
            if not visitado[j] and dist[j] < min_dist:
                min_dist = dist[j]
                u = j

        if u == -1:
            break

        visitado[u] = True

        for j in range(n):
            if not visitado[j] and mat[u][j] < inf:
                if dist[u] + mat[u][j] < dist[j]:
                    dist[j] = dist[u] + mat[u][j]
                    pred[j] = u

    return dist, pred


def mostrar_camino(pred, destino):
    camino = []
    actual = destino

    while actual != -1:
        camino.append(vertices[actual])
        actual = pred[actual]

    camino.reverse()
    return " -> ".join(camino)


dist, pred = dijkstra(mat, 0)

print("=== Distancias minimas desde A ===")

for i in range(n):
    print(f"A -> {vertices[i]} = {dist[i]}")

print()
print("Camino optimo:", mostrar_camino(pred, 5))
print("Distancia total:", dist[5])
