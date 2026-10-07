
import java.util.ArrayList;

public class Grafo {

    private String nombre;
    private ArrayList<Vertice> vertices;
    private ArrayList<Arista> aristas;
    private int gradoTotal;

    public Grafo() {
        nombre = "";
        vertices = new ArrayList<>();
        aristas = new ArrayList<>();
        gradoTotal = 0;
    }

    public Grafo(String nombre) {
        this.nombre = nombre;
        vertices = new ArrayList<>();
        aristas = new ArrayList<>();
        gradoTotal = 0;
    }

    public void agregarVertice(Vertice v) {
        vertices.add(v);
    }

    public void agregarArista(Arista a) {
        aristas.add(a);
    }

    public int calcularGrado(Vertice v) {
        int grado = 0;

        for (Arista arista : aristas) {
            if (arista.esBucle()
                    && arista.getExtremo1().getId() == v.getId()) {

                grado += 2;

            } else if (!arista.esBucle()
                    && arista.incideEn(v)) {

                grado++;
            }
        }

        v.setGrado(grado);
        v.setEsAislado(grado == 0);

        return grado;
    }

    public int calcularGradoTotal() {
        gradoTotal = 0;

        for (Vertice v : vertices) {
            gradoTotal += calcularGrado(v);
        }

        return gradoTotal;
    }

    public ArrayList<Vertice> obtenerAdyacentes(Vertice v) {
        ArrayList<Vertice> adyacentes = new ArrayList<>();

        for (Arista a : aristas) {
            if (a.incideEn(v)) {

                if (a.esBucle()) {
                    agregarVerticeSinRepetir(adyacentes, v);
                } else {

                    if (a.getExtremo1().getId() == v.getId()) {
                        agregarVerticeSinRepetir(
                                adyacentes,
                                a.getExtremo2()
                        );
                    } else {
                        agregarVerticeSinRepetir(
                                adyacentes,
                                a.getExtremo1()
                        );
                    }
                }
            }
        }

        return adyacentes;
    }

    private void agregarVerticeSinRepetir(
            ArrayList<Vertice> lista,
            Vertice nuevo) {

        boolean existe = false;

        for (Vertice v : lista) {
            if (v.getId() == nuevo.getId()) {
                existe = true;
                break;
            }
        }

        if (!existe) {
            lista.add(nuevo);
        }
    }

    public ArrayList<Arista> obtenerAristasIncidentes(Vertice v) {
        ArrayList<Arista> incidentes = new ArrayList<>();

        for (Arista a : aristas) {
            if (a.incideEn(v)) {
                incidentes.add(a);
            }
        }

        return incidentes;
    }

    public ArrayList<Arista> obtenerAristasAdyacentes(Arista a) {
        ArrayList<Arista> adyacentes = new ArrayList<>();

        for (Arista otra : aristas) {
            if (otra.getId() != a.getId()) {

                boolean comparteExtremo
                        = otra.incideEn(a.getExtremo1())
                        || otra.incideEn(a.getExtremo2());

                if (comparteExtremo) {
                    adyacentes.add(otra);
                }
            }
        }

        return adyacentes;
    }

    public ArrayList<Arista> obtenerBucles() {
        ArrayList<Arista> bucles = new ArrayList<>();

        for (Arista a : aristas) {
            if (a.esBucle()) {
                bucles.add(a);
            }
        }

        return bucles;
    }

    public ArrayList<String> obtenerParalelas() {
        ArrayList<String> paralelas = new ArrayList<>();

        for (int i = 0; i < aristas.size(); i++) {
            for (int j = i + 1; j < aristas.size(); j++) {

                Arista a1 = aristas.get(i);
                Arista a2 = aristas.get(j);

                if (a1.esParalela(a2)) {
                    paralelas.add(
                            "{"
                            + a1.getNombre()
                            + ", "
                            + a2.getNombre()
                            + "}"
                    );
                }
            }
        }

        return paralelas;
    }

    public ArrayList<Vertice> obtenerVerticesAislados() {
        ArrayList<Vertice> aislados = new ArrayList<>();

        calcularGradoTotal();

        for (Vertice v : vertices) {
            if (v.esAislado()) {
                aislados.add(v);
            }
        }

        return aislados;
    }

    public boolean verificarTeoremaSaludo() {
        int sumaGrados = calcularGradoTotal();

        return sumaGrados == 2 * aristas.size();
    }

    public boolean puedeExistirGrafo(int[] grados) {
        int suma = 0;

        for (int grado : grados) {
            if (grado < 0) {
                return false;
            }

            suma += grado;
        }

        return suma % 2 == 0;
    }

    public void mostrarTablaExtremos() {
        System.out.println();
        System.out.println("--- TABLA PUNTO EXTREMO - ARISTA ---");

        System.out.printf(
                "| %-8s | %-25s |%n",
                "Arista",
                "Punto(s) Extremo(s)"
        );

        System.out.println(
                "|----------|---------------------------|"
        );

        for (Arista a : aristas) {
            String extremos;

            if (a.esBucle()) {
                extremos = "{"
                        + a.getExtremo1().getNombre()
                        + "} [BUCLE]";
            } else {
                extremos = "{"
                        + a.getExtremo1().getNombre()
                        + ", "
                        + a.getExtremo2().getNombre()
                        + "}";
            }

            System.out.printf(
                    "| %-8s | %-25s |%n",
                    a.getNombre(),
                    extremos
            );
        }
    }

    public void mostrarAnalisisCompleto() {
        calcularGradoTotal();

        System.out.println();
        System.out.println("======================================");
        System.out.println("       ANALISIS COMPLETO DEL GRAFO");
        System.out.println("======================================");

        System.out.println(this);

        System.out.println("\nVERTICES:");

        for (Vertice v : vertices) {

            System.out.println("\n" + v);

            System.out.print("Adyacentes: ");

            ArrayList<Vertice> adyacentes = obtenerAdyacentes(v);

            if (adyacentes.isEmpty()) {
                System.out.println("Ninguno");
            } else {
                for (Vertice adyacente : adyacentes) {
                    System.out.print(adyacente.getNombre() + " ");
                }

                System.out.println();
            }

            System.out.print("Aristas incidentes: ");

            ArrayList<Arista> incidentes
                    = obtenerAristasIncidentes(v);

            if (incidentes.isEmpty()) {
                System.out.println("Ninguna");
            } else {
                for (Arista a : incidentes) {
                    System.out.print(a.getNombre() + " ");
                }

                System.out.println();
            }
        }

        System.out.println("\nBUCLES:");

        ArrayList<Arista> bucles = obtenerBucles();

        if (bucles.isEmpty()) {
            System.out.println("No existen bucles.");
        } else {
            for (Arista a : bucles) {
                System.out.println(a);
            }
        }

        System.out.println("\nARISTAS PARALELAS:");

        ArrayList<String> paralelas = obtenerParalelas();

        if (paralelas.isEmpty()) {
            System.out.println("No existen aristas paralelas.");
        } else {
            for (String par : paralelas) {
                System.out.println(par);
            }
        }

        System.out.println("\nVERTICES AISLADOS:");

        ArrayList<Vertice> aislados
                = obtenerVerticesAislados();

        if (aislados.isEmpty()) {
            System.out.println("No existen vertices aislados.");
        } else {
            for (Vertice v : aislados) {
                System.out.println(v.getNombre());
            }
        }

        System.out.println(
                "\nGrado total: "
                + calcularGradoTotal()
        );

        System.out.println(
                "2 x |E| = "
                + (2 * aristas.size())
        );

        if (verificarTeoremaSaludo()) {
            System.out.println(
                    "Se cumple el Teorema del Saludo de Mano."
            );
        } else {
            System.out.println(
                    "No se cumple el Teorema del Saludo de Mano."
            );
        }

        mostrarTablaExtremos();
    }

    @Override
    public String toString() {
        return "Grafo ["
                + nombre
                + "]: |V| = "
                + vertices.size()
                + ", |E| = "
                + aristas.size();
    }
}
