//3. Crea una clase genérica Catalogo<T> que almacene productos o libros. 
//a) Agrega métodos para agregar y buscar elemento 
//b) Prueba el catálogo con libros 
//c) Prueba el catálogo con productos
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

class Catalogo<T> {
    private List<T> elementos = new ArrayList<>();

    public void agregar(T elemento) {
        elementos.add(elemento);
    }

    public boolean buscar(T elemento) {
        return elementos.contains(elemento);
    }

    public void mostrarTodo() {
        for (T elem : elementos) {
            System.out.println(elem);
        }
    }
}

class Libro {
    private String titulo;
    private String autor;

    public Libro(String titulo, String autor) {
        this.titulo = titulo;
        this.autor = autor;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Libro)) return false;
        Libro l = (Libro) obj;
        return titulo.equals(l.titulo) && autor.equals(l.autor);
    }

    @Override
    public int hashCode() {
        return Objects.hash(titulo, autor);
    }

    @Override
    public String toString() {
        return "Libro: " + titulo + " - Autor: " + autor;
    }
}

class Producto {
    private String nombre;
    private double precio;

    public Producto(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Producto)) return false;
        Producto p = (Producto) obj;
        return nombre.equals(p.nombre) && precio == p.precio;
    }

    @Override
    public int hashCode() {
        return Objects.hash(nombre, precio);
    }

    @Override
    public String toString() {
        return "Producto: " + nombre + " - Precio: Bs " + precio;
    }
}
public class Main {
    public static void main(String[] args) {
        Catalogo<Libro> catalogoLibros = new Catalogo<>();
        catalogoLibros.agregar(new Libro("Cien años de soledad", "Gabriel García Márquez"));
        catalogoLibros.agregar(new Libro("1984", "George Orwell"));

        System.out.println("Catálogo de libros:");
        catalogoLibros.mostrarTodo();
        System.out.println("¿Está el libro '1984'? " +
                catalogoLibros.buscar(new Libro("1984", "George Orwell")));

        Catalogo<Producto> catalogoProductos = new Catalogo<>();
        catalogoProductos.agregar(new Producto("Laptop", 3999.99));
        catalogoProductos.agregar(new Producto("Mouse", 40));

        System.out.println("\nCatálogo de productos:");
        catalogoProductos.mostrarTodo();
        System.out.println("¿Está el producto 'Mouse'? " +
                catalogoProductos.buscar(new Producto("Mouse", 40)));
    }
}
