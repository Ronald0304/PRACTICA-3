#5.- Sea el siguiente diagrama de clases:  
#a) Crear, leer y mostrar un Archivo de Farmacias  
#b) Mostrar los medicamentos para la tos, de la Sucursal numero X  
#c) Mostrar el número de sucursal y su dirección que tienen el medicamento “Golpex”
import json
import os

class Medicamento:
    def __init__(self, nombre, codMedicamento, tipo, precio):
        self.nombre = nombre
        self.codMedicamento = codMedicamento
        self.tipo = tipo 
        self.precio = precio

    def leer(self):
        return self.nombre, self.codMedicamento, self.tipo, self.precio

    def mostrar(self):
        return f"Medicamento: {self.nombre}, Código: {self.codMedicamento}, Tipo: {self.tipo}, Precio: {self.precio:.2f}"

    def getTipo(self):
        return self.tipo

    def getPrecio(self):
        return self.precio

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Medicamento(data["nombre"], data["codMedicamento"], data["tipo"], data["precio"])


class Farmacia:
    def __init__(self, nombreFarmacia, direccion, sucursal, medicamentos):
        self.nombreFarmacia = nombreFarmacia
        self.direccion = direccion
        self.sucursal = sucursal
        self.med = medicamentos  

    def getDireccion(self):
        return self.direccion

    def getSucursal(self):
        return self.sucursal

    def mostrarMedicamentos(self):
        return [m.mostrar() for m in self.med]

    def buscaMedicamento(self, nombre):
        return any(m.nombre.lower() == nombre.lower() for m in self.med)

    def medicamentosPorTipo(self, tipo):
        return [m for m in self.med if m.getTipo().lower() == tipo.lower()]

    def medicamentosMenorPrecio(self):
        if not self.med:
            return []
        min_precio = min(m.getPrecio() for m in self.med)
        return [m for m in self.med if m.getPrecio() == min_precio]

    def to_dict(self):
        return {
            "nombreFarmacia": self.nombreFarmacia,
            "direccion": self.direccion,
            "sucursal": self.sucursal,
            "med": [m.to_dict() for m in self.med]
        }

    @staticmethod
    def from_dict(data):
        meds = [Medicamento.from_dict(m) for m in data["med"]]
        return Farmacia(data["nombreFarmacia"], data["direccion"], data["sucursal"], meds)


class ArchFarmacia:
    def __init__(self, na):
        self.na = na
        if not os.path.exists(self.na):
            self.crearArchivo()

    def crearArchivo(self):
        with open(self.na, 'w') as f:
            json.dump([], f)

    def _leerArchivo(self):
        with open(self.na, 'r') as f:
            return json.load(f)

    def _guardarArchivo(self, datos):
        with open(self.na, 'w') as f:
            json.dump(datos, f, indent=4)

    def adicionar(self, farmacia):
        data = self._leerArchivo()
        data.append(farmacia.to_dict())
        self._guardarArchivo(data)

    def listar(self):
        data = self._leerArchivo()
        for f in data:
            farmacia = Farmacia.from_dict(f)
            print(f"\nSucursal {farmacia.getSucursal()} - {farmacia.getDireccion()}")
            for m in farmacia.med:
                print("  ", m.mostrar())

    def mostrarMedicamentosResfrio(self):
        data = self._leerArchivo()
        for f in data:
            farmacia = Farmacia.from_dict(f)
            resfrio = farmacia.medicamentosPorTipo("resfrio")
            if resfrio:
                print(f"\nFarmacia: {farmacia.nombreFarmacia} (Sucursal {farmacia.getSucursal()})")
                for m in resfrio:
                    print("  ", m.mostrar())

    def mostrarMedicamentosMenorTos(self):
        data = self._leerArchivo()
        for f in data:
            farmacia = Farmacia.from_dict(f)
            tos_meds = farmacia.medicamentosPorTipo("tos")
            if tos_meds:
                menor_precio = min(m.getPrecio() for m in tos_meds)
                menor_meds = [m for m in tos_meds if m.getPrecio() == menor_precio]
                print(f"\nSucursal {farmacia.getSucursal()} (Medicamentos para la tos más baratos):")
                for m in menor_meds:
                    print("  ", m.mostrar())

    def mostrarFarmaciasConMedicamento(self, nombre_medicamento):
        data = self._leerArchivo()
        for f in data:
            farmacia = Farmacia.from_dict(f)
            if farmacia.buscaMedicamento(nombre_medicamento):
                print(f"Sucursal {farmacia.getSucursal()} - Dirección: {farmacia.getDireccion()}")

if __name__ == "__main__":
    arch = ArchFarmacia("farmacias.json")

    m1 = Medicamento("Golpex", 101, "tos", 15.5)
    m2 = Medicamento("Panadol", 102, "resfrio", 12.0)
    m3 = Medicamento("Mentisan", 103, "tos", 8.5)
    m4 = Medicamento("FluPlus", 104, "resfrio", 10.5)

    f1 = Farmacia("MiSalud", "Av. Arce #123", 1, [m1, m2])
    f2 = Farmacia("Farmavida", "Calle 10, Zona Sur", 2, [m3, m4])
    f3 = Farmacia("SaludTotal", "Av. Blanco Galindo #456", 3, [m1, m3])

    arch.adicionar(f1)
    arch.adicionar(f2)
    arch.adicionar(f3)

    print("\n--- Lista de todas las farmacias ---")
    arch.listar()

    print("\n--- Medicamentos para resfrío ---")
    arch.mostrarMedicamentosResfrio()

    print("\n--- Medicamentos para la tos más baratos por sucursal ---")
    arch.mostrarMedicamentosMenorTos()

    print("\n--- Farmacias con el medicamento 'Golpex' ---")
    arch.mostrarFarmaciasConMedicamento("Golpex")
