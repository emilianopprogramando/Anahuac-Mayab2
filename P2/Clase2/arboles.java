
class Nodo {

    int clave;
    Nodo izquierdo, derecho;

    public Nodo(int elemento) {
        clave = elemento;
        izquierdo = derecho = null;
    }
}

// Clase ArbolBinario
class ArbolBinario {

    Nodo raiz;

    public ArbolBinario() {
        raiz = null;
    }

    // INSERCIÓN
    public void insertar(int clave) {
        raiz = insertarRec(raiz, clave);
    }

    private Nodo insertarRec(Nodo raiz, int clave) {
        if (raiz == null) {
            raiz = new Nodo(clave);
            return raiz;
        }

        if (clave < raiz.clave) {
            raiz.izquierdo = insertarRec(raiz.izquierdo, clave);
        } else if (clave > raiz.clave) {
            raiz.derecho = insertarRec(raiz.derecho, clave);
        }

        return raiz;
    }

    // RECORRIDO INORDEN (Para mostrar los elementos ordenados)
    public void inorden() {
        inordenRec(raiz);
        System.out.println();
    }

    private void inordenRec(Nodo raiz) {
        if (raiz != null) {
            inordenRec(raiz.izquierdo);
            System.out.print(raiz.clave + " ");
            inordenRec(raiz.derecho);
        }
    }
}
