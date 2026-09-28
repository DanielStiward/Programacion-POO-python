# ******************** ZONA DE FUNCIONES ***********************
from animal import Animal

class Cocodrilo(Animal):
    def moverse(self):
        print(f"{self.nombre} nada y tambien se arrastra por la orilla.")