#1. Crea una clase genérica Caja<T> para guardar algún tipo de objeto 
#a) Agrega métodos guardar() y obtener() 
#b) Crea dos instancias de la caja y almacena 2 datos de diferente tipo 
#c) Muestra el contenido de las cajas 
from typing import Generic, TypeVar

T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self.contenido: T = None 

    def guardar(self, objeto: T):
        self.contenido = objeto

    def obtener(self) -> T:
        return self.contenido

caja_texto = Caja[str]()
caja_texto.guardar("Hola Mundo")

caja_numero = Caja[int]()
caja_numero.guardar(12345)

print("Contenido de caja de texto:", caja_texto.obtener())
print("Contenido de caja de numero:", caja_numero.obtener())
