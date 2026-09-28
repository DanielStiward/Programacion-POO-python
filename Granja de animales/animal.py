# ******************** ZONA DE FUNCIONES ***********************

class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color

    def moverse(self):
        print(f"{self.nombre} se mueve por su habitat: {self.habitat}.")

    def comunicacion(self):
        print(f"{self.nombre} se comunica con otros de su especie.")

    def reproduccion(self):
        print(f"{self.nombre} se reproduce siguiendo el ciclo natural de su especie.")

    def alimentarse(self):
        print(f"{self.nombre} se alimenta principalmente de {self.dieta}.")

    def adaptacion(self):
        print(f"{self.nombre} esta adaptado para vivir en {self.habitat}.")

    def instintos(self):
        print(f"{self.nombre} actua segun sus instintos naturales.")

    def descanso(self):
        print(f"{self.nombre} descansa para recuperar energia.")

    def sueno(self):
        print(f"{self.nombre} duerme segun los habitos propios de su especie.")

    def interaccion_social(self):
        print(f"{self.nombre} interactua con otros animales de su entorno.")

    def mostrar_info(self):
        print(f"--- Animal: {self.nombre} ---")
        print(f"Edad: {self.edad} - Habitat: {self.habitat} - Dieta: {self.dieta} - Tamaño: {self.tamano} - Color: {self.color}")