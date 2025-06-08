from typing import Generic, TypeVar

# Definimos un tipo genérico T
T = TypeVar('T')

# Clase genérica Caja
class Caja(Generic[T]):
    def __init__(self):
        self.contenido: T = None  # Inicializa el contenido

    def guardar(self, objeto: T):
        self.contenido = objeto

    def obtener(self) -> T:
        return self.contenido

# Programa principal
def main():
    # Caja para strings
    caja_texto = Caja[str]()
    caja_texto.guardar("Hola Mundo")

    # Caja para enteros
    caja_numero = Caja[int]()
    caja_numero.guardar(12345)

    # Mostrar contenido
    print("Contenido de caja_texto:", caja_texto.obtener())
    print("Contenido de caja_numero:", caja_numero.obtener())

# Ejecutar
if __name__ == "__main__":
    main()
