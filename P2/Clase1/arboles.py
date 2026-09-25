class Nodo:
    def __init__(self):
        self.info = 0
        self.izq = None
        self.der = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, info):
        nuevo = Nodo()
        nuevo.info = info
        nuevo.izq = None
        nuevo.der = None

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz
        anterior = None

        while actual is not None:
            anterior = actual

            if info < actual.info:
                actual = actual.izq
            elif info > actual.info:
                actual = actual.der
            else:
                return

        if info < anterior.info:
            anterior.izq = nuevo
        else:
            anterior.der = nuevo