//3.- Sea el siguiente diagrama de clases: 
//a) Implementar el diagrama de clases. 
//b) Implementa buscarCliente(int c) a través del id. 
//c) Implementa buscarCelularCliente(int c), que devuelva los datos del cliente junto al número de celular. 
import java.io.*;
import java.util.*;

class Cliente {
    private int id;
    private String nombre;
    private int telefono;

    public Cliente(int id, String nombre, int telefono) {
        this.id = id;
        this.nombre = nombre;
        this.telefono = telefono;
    }

    public int getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    @Override
    public String toString() {
        return "ID: " + id + ", Nombre: " + nombre + ", Teléfono: " + telefono;
    }

    public String toLinea() {
        return id + "," + nombre + "," + telefono;
    }

    public static Cliente fromLinea(String linea) {
        String[] partes = linea.split(",");
        int id = Integer.parseInt(partes[0]);
        String nombre = partes[1];
        int telefono = Integer.parseInt(partes[2]);
        return new Cliente(id, nombre, telefono);
    }
}

class ArchivoCliente {
    private String nomA;

    public ArchivoCliente(String nomA) {
        this.nomA = nomA;
        File archivo = new File(nomA);
        if (!archivo.exists()) {
            crearArchivo();
        }
    }

    public void crearArchivo() {
        try (PrintWriter writer = new PrintWriter(new FileWriter(nomA))) {
            // Archivo vacío
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private List<Cliente> leerClientes() {
        List<Cliente> lista = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(nomA))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                lista.add(Cliente.fromLinea(linea));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return lista;
    }

    private void guardarTodos(List<Cliente> clientes) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(nomA))) {
            for (Cliente c : clientes) {
                writer.println(c.toLinea());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void guardarCliente(Cliente cliente) {
        List<Cliente> clientes = leerClientes();
        for (Cliente c : clientes) {
            if (c.getId() == cliente.getId()) {
                System.out.println("El cliente ya existe.");
                return;
            }
        }
        clientes.add(cliente);
        guardarTodos(clientes);
        System.out.println("Cliente guardado.");
    }

    public Cliente buscarCliente(int id) {
        List<Cliente> clientes = leerClientes();
        for (Cliente c : clientes) {
            if (c.getId() == id) {
                return c;
            }
        }
        return null;
    }

    public String buscarCelularCliente(int id) {
        Cliente cliente = buscarCliente(id);
        if (cliente != null) {
            return cliente + " (Celular: " + cliente.getTelefono() + ")";
        }
        return "Cliente no encontrado.";
    }

    public void actualizarCliente(Cliente nuevoCliente) {
        List<Cliente> clientes = leerClientes();
        for (int i = 0; i < clientes.size(); i++) {
            if (clientes.get(i).getId() == nuevoCliente.getId()) {
                clientes.set(i, nuevoCliente);
                guardarTodos(clientes);
                System.out.println("Cliente actualizado.");
                return;
            }
        }
        System.out.println("Cliente no encontrado para actualizar.");
    }

    public void eliminarCliente(int id) {
        List<Cliente> clientes = leerClientes();
        int sizeAntes = clientes.size();
        clientes.removeIf(c -> c.getId() == id);
        if (clientes.size() == sizeAntes) {
            System.out.println("Cliente no encontrado para eliminar.");
        } else {
            guardarTodos(clientes);
            System.out.println("Cliente eliminado.");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        ArchivoCliente archivo = new ArchivoCliente("clientes.txt");

        Cliente c1 = new Cliente(1, "Carlos Gómez", 123456789);
        Cliente c2 = new Cliente(2, "Lucía López", 987654321);
        Cliente c3 = new Cliente(3, "Ronald Gutierrez", 8311043);
        Cliente c4 = new Cliente(4, "Paul Mamani", 1855853);

        archivo.guardarCliente(c1);
        archivo.guardarCliente(c2);
        archivo.guardarCliente(c3);
        archivo.guardarCliente(c4);

        System.out.println(archivo.buscarCelularCliente(1));
        System.out.println(archivo.buscarCelularCliente(4));

        Cliente c1Actualizado = new Cliente(1, "Carlos Gutierrez.", 111222333);
        archivo.actualizarCliente(c1Actualizado);

        System.out.println(archivo.buscarCelularCliente(2));
        Cliente encontrado = archivo.buscarCliente(3);
        if (encontrado != null) {
            System.out.println("Encontrado: " + encontrado);
        }
    }
}
