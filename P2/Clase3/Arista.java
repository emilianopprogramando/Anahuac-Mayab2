
public class Arista {

    private String nombre;
    private int id;
    private Vertice extremo1;
    private Vertice extremo2;
    private boolean esBucle;

    public Arista() {
        nombre = "";
        id = 0;
        extremo1 = null;
        extremo2 = null;
        esBucle = false;
    }

    public Arista(String nombre, int id, Vertice extremo1, Vertice extremo2) {
        this.nombre = nombre;
        this.id = id;
        this.extremo1 = extremo1;
        this.extremo2 = extremo2;

        if (extremo1 != null && extremo2 != null) {
            esBucle = extremo1.getId() == extremo2.getId();
        } else {
            esBucle = false;
        }
    }

    public String getNombre() {
        return nombre;
    }

    public int getId() {
        return id;
    }

    public Vertice getExtremo1() {
        return extremo1;
    }

    public Vertice getExtremo2() {
        return extremo2;
    }

    public boolean esBucle() {
        return esBucle;
    }

    public boolean esParalela(Arista otra) {
        if (otra == null || this.id == otra.id) {
            return false;
        }

        boolean mismoOrden
                = extremo1.getId() == otra.extremo1.getId()
                && extremo2.getId() == otra.extremo2.getId();

        boolean ordenContrario
                = extremo1.getId() == otra.extremo2.getId()
                && extremo2.getId() == otra.extremo1.getId();

        return mismoOrden || ordenContrario;
    }

    public boolean incideEn(Vertice v) {
        if (v == null) {
            return false;
        }

        return extremo1.getId() == v.getId()
                || extremo2.getId() == v.getId();
    }

    @Override
    public String toString() {
        if (esBucle) {
            return nombre + ": {" + extremo1.getNombre() + "} [BUCLE]";
        }

        return nombre + ": {"
                + extremo1.getNombre()
                + ", "
                + extremo2.getNombre()
                + "}";
    }
}
