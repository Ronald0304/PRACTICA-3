#3. Crea una clase genérica Catalogo<T> que almacene productos o libros. 
#a) Agrega métodos para agregar y buscar elemento 
#b) Prueba el catálogo con libros 
#c) Prueba el catálogo con productos 
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Catalogo(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def agregar(self, elemento: T):
        self.elementos.append(elemento)

    def buscar(self, elemento: T) -> bool:
        return elemento in self.elementos

    def mostrar_todo(self):
        for elem in self.elementos:
            print(elem)
class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def __eq__(self, other):
        return isinstance(other, Libro) and self.titulo == other.titulo and self.autor == other.autor

    def __hash__(self):
        return hash((self.titulo, self.autor))

    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor}"
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __eq__(self, other):
        return isinstance(other, Producto) and self.nombre == other.nombre and self.precio == other.precio

    def __hash__(self):
        return hash((self.nombre, self.precio))

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: Bs {self.precio}"

catalogo_libros = Catalogo[Libro]()
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("1984", "George Orwell")
catalogo_libros.agregar(libro1)
catalogo_libros.agregar(libro2)
print("Catálogo de libros:")
catalogo_libros.mostrar_todo()
print("¿Está el libro '1984'? ", catalogo_libros.buscar(Libro("1984", "George Orwell")))

catalogo_productos = Catalogo[Producto]()
prod1 = Producto("Laptop", 3999.99)
prod2 = Producto("Mouse", 40)
catalogo_productos.agregar(prod1)
catalogo_productos.agregar(prod2)
print("\nCatálogo de productos:")
catalogo_productos.mostrar_todo()
print("¿Está el producto 'Mouse'? ", catalogo_productos.buscar(Producto("Mouse", 40)))

