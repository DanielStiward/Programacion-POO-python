# ******************** ZONA DE FUNCIONES ***********************

class Vehiculo:
    def __init__(self, modelo, color, motor, num_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.num_puertas = num_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    def arranque(self):
        print(f"El {self.modelo} ha encendido su motor {self.motor}.")

    def apagado(self):
        print(f"El {self.modelo} se ha apagado.")

    def aceleracion_frenado(self):
        print(f"El {self.modelo} acelera y frena con normalidad.")

    def sistema_direccion(self):
        print(f"El {self.modelo} responde correctamente a la direccion.")

    def climatizacion(self):
        print(f"El {self.modelo} tiene climatizacion activada.")

    def luces(self):
        print(f"El {self.modelo} enciende sus luces.")

    def sistema_ventanas(self):
        print(f"El {self.modelo} tiene {self.num_puertas} puertas con ventanas electricas.")

    def sistema_espejo(self):
        print(f"El {self.modelo} ajusta sus espejos correctamente.")

    def mostrar_info(self):
        print(f"--- Vehículo: {self.modelo} ---")
        print(f"Color: {self.color} - Motor: {self.motor} - Puertas: {self.num_puertas} - Pasajeros: {self.capacidad_pasajeros} - Combustible: {self.tipo_combustible}")