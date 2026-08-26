class NodoLista:
    def __init__(self, objeto, nodo=None):
        self.datos = objeto
        self.siguienteNodo = nodo

    def obtenerObject(self):
        return self.datos

    def obtenerSiguiente(self):
        return self.siguienteNodo


# Definición de la clase Lista Circular
class Lista:
    def __init__(self, nombreLista="lista"):
        self.nombre = nombreLista
        self.primerNodo = None
        self.ultimoNodo = None

    def insertarAlFrente(self, elementoInsertar):
        nuevoNodo = NodoLista(elementoInsertar)

        if self.estaVacia():
            self.primerNodo = self.ultimoNodo = nuevoNodo

            # El último apunta al primero
            self.ultimoNodo.siguienteNodo = self.primerNodo
        else:
            nuevoNodo.siguienteNodo = self.primerNodo
            self.primerNodo = nuevoNodo

            # El último siempre apunta al primero
            self.ultimoNodo.siguienteNodo = self.primerNodo

    def insertarAlFinal(self, elementoInsertar):
        nuevoNodo = NodoLista(elementoInsertar)

        if self.estaVacia():
            self.primerNodo = self.ultimoNodo = nuevoNodo
            self.ultimoNodo.siguienteNodo = self.primerNodo
        else:
            nuevoNodo.siguienteNodo = self.primerNodo
            self.ultimoNodo.siguienteNodo = nuevoNodo
            self.ultimoNodo = nuevoNodo

    def eliminarDelFrente(self):
        if self.estaVacia():
            raise ExcepcionListaVacia(self.nombre)

        elementoEliminado = self.primerNodo.datos

        if self.primerNodo == self.ultimoNodo:
            self.primerNodo = self.ultimoNodo = None
        else:
            self.primerNodo = self.primerNodo.siguienteNodo

            # El último apunta al nuevo primero
            self.ultimoNodo.siguienteNodo = self.primerNodo

        return elementoEliminado

    def eliminarDelFinal(self):
        if self.estaVacia():
            raise ExcepcionListaVacia(self.nombre)

        elementoEliminado = self.ultimoNodo.datos

        if self.primerNodo == self.ultimoNodo:
            self.primerNodo = self.ultimoNodo = None
        else:
            actual = self.primerNodo

            # Buscar el nodo anterior al último
            while actual.siguienteNodo != self.ultimoNodo:
                actual = actual.siguienteNodo

            self.ultimoNodo = actual

            # El último apunta nuevamente al primero
            self.ultimoNodo.siguienteNodo = self.primerNodo

        return elementoEliminado

    def estaVacia(self):
        return self.primerNodo is None

    def imprimir(self):
        if self.estaVacia():
            print(f"{self.nombre} vacia")
            return

        print(f"La {self.nombre} es:", end=" ")

        actual = self.primerNodo

        # Usamos do-while simulado para evitar ciclo infinito
        while True:
            print(actual.datos, end=" ")
            actual = actual.siguienteNodo

            if actual == self.primerNodo:
                break

        print("\n")


# Definición de la excepción ExcepcionListaVacia
class ExcepcionListaVacia(Exception):
    def __init__(self, nombre="Lista"):
        super().__init__(f"{nombre} esta vacia")


# Clase para probar la Lista
class PruebaLista:
    @staticmethod
    def main():
        lista = Lista()

        lista.insertarAlFrente(-1)
        lista.imprimir()

        lista.insertarAlFrente(0)
        lista.imprimir()

        lista.insertarAlFinal(1)
        lista.imprimir()

        lista.insertarAlFinal(5)
        lista.imprimir()

        try:
            objetoEliminado = lista.eliminarDelFrente()
            print(f"{objetoEliminado} eliminado")
            lista.imprimir()

            objetoEliminado = lista.eliminarDelFrente()
            print(f"{objetoEliminado} eliminado")
            lista.imprimir()

            objetoEliminado = lista.eliminarDelFinal()
            print(f"{objetoEliminado} eliminado")
            lista.imprimir()

            objetoEliminado = lista.eliminarDelFinal()
            print(f"{objetoEliminado} eliminado")
            lista.imprimir()

        except ExcepcionListaVacia as excepcionListaVacia:
            print(excepcionListaVacia)


# Llamada al método main
if __name__ == "__main__":
    PruebaLista.main()