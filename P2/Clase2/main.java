
public class main {

    public static void main(String[] args) {
        ArbolBinario arbol = new ArbolBinario();

        // Pruebas de inserción
        arbol.insertar(50);
        arbol.insertar(30);
        arbol.insertar(20);
        arbol.insertar(40);
        arbol.insertar(70);
        arbol.insertar(60);
        arbol.insertar(80);

        System.out.print("Recorrido Inorden del árbol: ");
        arbol.inorden();
    }
}
