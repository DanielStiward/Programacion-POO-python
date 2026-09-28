# ******************** ZONA DE FUNCIONES ***********************
from vehiculo import Vehiculo

class Camion(Vehiculo):
    def tipo_seguridad(self):
        print(f"El {self.modelo} cuenta con frenos de aire y camara de punto ciego.")