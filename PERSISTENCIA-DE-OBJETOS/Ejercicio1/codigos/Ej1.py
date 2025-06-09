#1.- Sea el siguiente diagrama de clases:
#a) Implementa el método guardarEmpleado(Empleado e) para almacenar empleados. 
#b) Implementa buscaEmpleado(String n) a traves del nombre, para ver los datos del Empleado n. 
#c) Implementa mayorSalario(float sueldo), que devuelva al primer empleado con sueldo mayor al ingresado.  
import json
import os     

class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "salario": self.salario
        }

    @staticmethod
    def from_dict(data):
        return Empleado(data['nombre'], data['edad'], data['salario'])

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}"

class ArchivoEmpleado:
    def __init__(self, nomA):
        self.nomA = nomA
        if not os.path.exists(self.nomA):
            self.crearArchivo()

    def crearArchivo(self):
        carpeta = os.path.dirname(self.nomA)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)
        with open(self.nomA, 'w') as archivo:
            json.dump([], archivo)

    def _leerEmpleados(self):
        with open(self.nomA, 'r') as archivo:
            return json.load(archivo)

    def _guardarTodos(self, lista_empleados):
        with open(self.nomA, 'w') as archivo:
            json.dump(lista_empleados, archivo, indent=4)

    def guardarEmpleado(self, e):
        empleados = self._leerEmpleados()
        empleados.append(e.to_dict())
        self._guardarTodos(empleados)
        print("Empleado guardado correctamente.")

    def buscaEmpleado(self, nombre):
        empleados = self._leerEmpleados()
        for emp in empleados:
            if emp["nombre"].lower() == nombre.lower():
                return Empleado.from_dict(emp)
        return None

    def mayorSalario(self, sueldo):
        empleados = self._leerEmpleados()
        for emp in empleados:
            if emp["salario"] > sueldo:
                return Empleado.from_dict(emp)
        return None
    
if __name__ == "__main__":
    archivo = ArchivoEmpleado("empleados.json")

    archivo.guardarEmpleado(Empleado("Ana", 30, 3500.50))
    archivo.guardarEmpleado(Empleado("Luis", 45, 5200.75))
    archivo.guardarEmpleado(Empleado("Carla", 28, 4000.00))

    nombre = "Carla"
    emp = archivo.buscaEmpleado(nombre)
    if emp:
        print(f"\nEmpleado encontrado: {emp}")
    else:
        print(f"\nEmpleado con nombre {nombre} no encontrado.")

    salario_limite = 4000
    emp_mayor = archivo.mayorSalario(salario_limite)
    if emp_mayor:
        print(f"\nPrimer empleado con salario mayor a {salario_limite}: {emp_mayor}")
    else:
        print(f"\nNo se encontró empleado con salario mayor a {salario_limite}.")
