
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Nombre del grafo: ");
        String nombreGrafo = scanner.nextLine();

        Grafo grafo = new Grafo(nombreGrafo);

        System.out.print("Cantidad de vertices: ");
        int cantidadVertices = scanner.nextInt();
        scanner.nextLine();

        ArrayList<Vertice> vertices = new ArrayList<>();

        for (int i = 1; i <= cantidadVertices; i++) {

            System.out.print("Nombre del vertice " + i + ": ");
            String nombre = scanner.nextLine();

            Vertice vertice = new Vertice(nombre, i);

            vertices.add(vertice);
            grafo.agregarVertice(vertice);
        }

        System.out.print("\nCantidad de aristas: ");
        int cantidadAristas = scanner.nextInt();
        scanner.nextLine();

        for (int i = 1; i <= cantidadAristas; i++) {

            System.out.println("\nArista " + i);

            System.out.print("Nombre de la arista: ");
            String nombreArista = scanner.nextLine();

            Vertice extremo1 = null;
            Vertice extremo2 = null;

            while (extremo1 == null) {

                System.out.print("Primer vertice: ");
                String nombreVertice = scanner.nextLine();

                extremo1 = buscarVertice(vertices, nombreVertice);

                if (extremo1 == null) {
                    System.out.println("Ese vertice no existe.");
                }
            }

            while (extremo2 == null) {

                System.out.print("Segundo vertice: ");
                String nombreVertice = scanner.nextLine();

                extremo2 = buscarVertice(vertices, nombreVertice);

                if (extremo2 == null) {
                    System.out.println("Ese vertice no existe.");
                }
            }

            Arista arista = new Arista(
                    nombreArista,
                    i,
                    extremo1,
                    extremo2
            );

            grafo.agregarArista(arista);
        }

        grafo.mostrarAnalisisCompleto();

        scanner.close();
    }

    public static Vertice buscarVertice(
            ArrayList<Vertice> vertices,
            String nombre) {

        for (Vertice v : vertices) {

            if (v.getNombre().equalsIgnoreCase(nombre)) {
                return v;
            }
        }

        return null;
    }
}
