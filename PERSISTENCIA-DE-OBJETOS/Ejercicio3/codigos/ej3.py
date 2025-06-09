#3.- Sea el siguiente diagrama de clases:
#a) Implementar el diagrama de clases. 
#b) Implementa buscarCliente(int c) a través del id. 
#c) Implementa buscarCelularCliente(int c), que devuelva los datos del cliente junto al número de celular. 
import json
import os

class Cliente:
    def __init__(self, id, nombre, telefono):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'telefono': self.telefono
        }

    @staticmethod
    def from_dict(data):
        return Cliente(data['id'], data['nombre'], data['telefono'])

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}"

class ArchivoCliente:
    def __init__(self, nomA):
        self.nomA = nomA
        if not os.path.exists(self.nomA):
            self.crearArchivo()

    def crearArchivo(self):
        with open(self.nomA, 'w') as archivo:
            json.dump([], archivo)

    def _leerClientes(self):
        with open(self.nomA, 'r') as archivo:
            return json.load(archivo)

    def _guardarTodos(self, lista_clientes):
        with open(self.nomA, 'w') as archivo:
            json.dump(lista_clientes, archivo, indent=4)

    def guardarCliente(self, cliente):
        clientes = self._leerClientes()
        for c in clientes:
            if c['id'] == cliente.id:
                print("El cliente ya existe.")
                return
        clientes.append(cliente.to_dict())
        self._guardarTodos(clientes)
        print("Cliente guardado.")

    def buscarCliente(self, c):
        clientes = self._leerClientes()
        for data in clientes:
            if data['id'] == c:
                return Cliente.from_dict(data)
        return None

    def buscarCelularCliente(self, c):
        cliente = self.buscarCliente(c)
        if cliente:
            return f"{cliente} (Celular: {cliente.telefono})"
        else:
            return "Cliente no encontrado."

    def actualizarCliente(self, nuevo_cliente):
        clientes = self._leerClientes()
        for i, c in enumerate(clientes):
            if c['id'] == nuevo_cliente.id:
                clientes[i] = nuevo_cliente.to_dict()
                self._guardarTodos(clientes)
                print("Cliente actualizado.")
                return
        print("Cliente no encontrado para actualizar.")

    def eliminarCliente(self, id_cliente):
        clientes = self._leerClientes()
        nuevos = [c for c in clientes if c['id'] != id_cliente]
        if len(clientes) == len(nuevos):
            print("Cliente no encontrado para eliminar.")
        else:
            self._guardarTodos(nuevos)
            print("Cliente eliminado.")

if __name__ == "__main__":
    archivo = ArchivoCliente("clientes.json")

    c1 = Cliente(1, "Carlos Gómez", 123456789)
    c2 = Cliente(2, "Lucía López", 987654321)
    c3 = Cliente(3, "Ronald Gutierrez", 8311043)
    c4 = Cliente(4, "Paul Mamani", 1855853)

    archivo.guardarCliente(c1)
    archivo.guardarCliente(c2)
    archivo.guardarCliente(c3)
    archivo.guardarCliente(c4)

    print(archivo.buscarCelularCliente(1))  
    print(archivo.buscarCelularCliente(4))

    c1_actualizado = Cliente(1, "Carlos Gutierrez.", 111222333)
    archivo.actualizarCliente(c1_actualizado)

    print(archivo.buscarCelularCliente(2))  
    print(archivo.buscarCliente(3))
