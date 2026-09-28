# ******************** ZONA DE FUNCIONES ***********************
from vehiculo import Vehiculo

class Camioneta(Vehiculo):
    def tipo_seguridad(self):
        print(f"La {self.modelo} cuenta con sensores de reversa para carga.")