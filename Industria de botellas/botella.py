# ************ Clase padre *******************

class Botella:
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados

    def contener_liquidos(self):
        print(f"La botella de {self.material} contiene {self.capacidad} de liquido.")

    def facilitar_vertido(self):
        print(f"Gracias a su forma {self.forma}, facilita el vertido del liquido.")

    def cierre_hermetico(self):
        print(f"La tapa tipo {self.tapa} asegura un cierre hermtico.")

    def transporte(self):
        print("Esta botella puede transportarse con facilidad.")

    def manejo(self):
        print("Se puede manejar con una sola mano.")

    def reutilizacion(self):
        print("Esta botella puede reutilizarse.")

    def mostrar_info(self):
        print(f"--- Botella de {self.material} ---")
        print(f"Capacidad: {self.capacidad}")
        print(f"Forma: {self.forma}")
        print(f"Diseño: {self.diseno}")
        print(f"Tapa: {self.tapa}")
        print(f"Grabados: {self.grabados}")