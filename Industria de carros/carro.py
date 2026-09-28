# ******************** ZONA DE FUNCIONES ***********************
from vehiculo import Vehiculo

class Carro(Vehiculo):
    def tipo_seguridad(self):
        print(f"El {self.modelo} cuenta con airbags y frenos ABS.")