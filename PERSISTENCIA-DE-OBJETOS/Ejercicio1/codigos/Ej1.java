//1. Sea el siguiente diagrama de clases: 
//a) Implementa el método guardarEmpleado(Empleado e) para almacenar empleados.
//b) Implementa buscaEmpleado(String n) a traves del nombre, para ver los datos del Empleado n. 
//c) Implementa mayorSalario(float sueldo), que devuelva al primer empleado con sueldo mayor al ingresado. 
import java.io.*;
import java.util.*;

class Empleado {
    private String nombre;
    private int edad;
    private double salario;

    public Empleado(String nombre, int edad, double salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public double getSalario() {
        return salario;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + ", Edad: " + edad + ", Salario: " + salario;
    }

    public String toLinea() {
        return nombre + "," + edad + "," + salario;
    }

    public static Empleado fromLinea(String linea) {
        String[] partes = linea.split(",");
        String nombre = partes[0];
        int edad = Integer.parseInt(partes[1]);
        double salario = Double.parseDouble(partes[2]);
        return new Empleado(nombre, edad, salario);
    }
}

class ArchivoEmpleado {
    private String nomA;

    public ArchivoEmpleado(String nomA) {
        this.nomA = nomA;
        File archivo = new File(nomA);
        if (!archivo.exists()) {
            crearArchivo();
        }
    }

    public void crearArchivo() {
        try {
            File archivo = new File(nomA);
            File carpeta = archivo.getParentFile();
            if (carpeta != null && !carpeta.exists()) {
                carpeta.mkdirs();
            }
            PrintWriter writer = new PrintWriter(new FileWriter(nomA));
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private List<Empleado> leerEmpleados() {
        List<Empleado> lista = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(nomA))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                lista.add(Empleado.fromLinea(linea));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return lista;
    }

    private void guardarTodos(List<Empleado> empleados) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(nomA))) {
            for (Empleado e : empleados) {
                writer.println(e.toLinea());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void guardarEmpleado(Empleado e) {
        List<Empleado> empleados = leerEmpleados();
        empleados.add(e);
        guardarTodos(empleados);
        System.out.println("Empleado guardado correctamente.");
    }

    public Empleado buscaEmpleado(String nombre) {
        List<Empleado> empleados = leerEmpleados();
        for (Empleado e : empleados) {
            if (e.getNombre().equalsIgnoreCase(nombre)) {
                return e;
            }
        }
        return null;
    }

    public Empleado mayorSalario(double sueldo) {
        List<Empleado> empleados = leerEmpleados();
        for (Empleado e : empleados) {
            if (e.getSalario() > sueldo) {
                return e;
            }
        }
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        ArchivoEmpleado archivo = new ArchivoEmpleado("empleados.txt");

        archivo.guardarEmpleado(new Empleado("Ana", 30, 3500.50));
        archivo.guardarEmpleado(new Empleado("Luis", 45, 5200.75));
        archivo.guardarEmpleado(new Empleado("Carla", 28, 4000.00));

        String nombre = "Carla";
        Empleado emp = archivo.buscaEmpleado(nombre);
        if (emp != null) {
            System.out.println("\nEmpleado encontrado: " + emp);
        } else {
            System.out.println("\nEmpleado con nombre " + nombre + " no encontrado.");
        }

        double salario_limite = 4000;
        Empleado empMayor = archivo.mayorSalario(salario_limite);
        if (empMayor != null) {
            System.out.println("\nPrimer empleado con salario mayor a " + salario_limite + ": " + empMayor);
        } else {
            System.out.println("\nNo se encontró empleado con salario mayor a " + salario_limite);
        }
    }
}
