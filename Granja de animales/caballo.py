# ******************** ZONA DE FUNCIONES ***********************
from animal import Animal

class Caballo(Animal):
    def moverse(self):
        print(f"{self.nombre} corre y galopa por la pradera.")  