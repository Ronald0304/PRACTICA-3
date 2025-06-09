#5: Crea una clase genérica Pila<T> 
#a) Implementa un método para apilar 
#b) Implementa un método para des apilar 
#c) Prueba la pila con diferentes tipos de datos 
#d) Muestra los datos de la pila
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def apilar(self, elemento: T):
        self.elementos.append(elemento)
        print(f"Apilado: {elemento}")

    def desapilar(self) -> T:
        if self.esta_vacia():
            print("La pila está vacía. No se puede desapilar.")
            return None
        elemento = self.elementos.pop()
        print(f"Desapilado: {elemento}")
        return elemento

    def mostrar(self):
        if self.esta_vacia():
            print("La pila está vacía.")
        else:
            print("Contenido de la pila:")
            for elemento in self.elementos:
                print(elemento)

    def esta_vacia(self) -> bool:
        return len(self.elementos) == 0
# Pila de enteros
print("-----PILA DE ENTEROS-----")
pila_enteros = Pila[int]()
pila_enteros.apilar(10)
pila_enteros.apilar(20)
pila_enteros.apilar(30)
pila_enteros.mostrar()
pila_enteros.desapilar()
pila_enteros.mostrar()

# Pila de cadenas
print("-----PILA DE CADENAS (str)-----")
pila_cadenas = Pila[str]()
pila_cadenas.apilar("Hola")
pila_cadenas.apilar("Mundo")
pila_cadenas.apilar("Python")
pila_cadenas.mostrar()
pila_cadenas.desapilar()
pila_cadenas.mostrar()

# Pila de flotantes
print("-----PILA DE NÚMEROS DECIMALES (float)-----")
pila_floats = Pila[float]()
pila_floats.apilar(3.14)
pila_floats.apilar(2.71)
pila_floats.apilar(1.618)
pila_floats.mostrar()
pila_floats.desapilar()
pila_floats.mostrar()
