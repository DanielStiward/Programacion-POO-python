# ******************** ZONA DE FUNCIONES ***********************
from carro import Carro
from camioneta import Camioneta
from camion import Camion

def probar_vehiculos():
    carro1 = Carro("BMW Z4", "negro", "V6 turbo", 2, 2, "gasolina")
    camioneta1 = Camioneta("Camioneta de carga", "blanco", "diesel 1.5", 4, 3, "diesel")
    camion1 = Camion("Camion de volteo", "blanco", "diesel turbo", 2, 2, "diesel")

    print(" CARRO ")
    carro1.mostrar_info()
    carro1.arranque()
    carro1.aceleracion_frenado()
    carro1.sistema_direccion()
    carro1.climatizacion()
    carro1.tipo_seguridad()
    carro1.luces()
    carro1.sistema_ventanas()
    carro1.sistema_espejo()
    carro1.apagado()

    print("\n CAMIONETA ")
    camioneta1.mostrar_info()
    camioneta1.arranque()
    camioneta1.aceleracion_frenado()
    camioneta1.sistema_direccion()
    camioneta1.tipo_seguridad()
    camioneta1.luces()
    camioneta1.sistema_espejo()
    camioneta1.apagado()

    print("\n CAMION ")
    camion1.mostrar_info()
    camion1.arranque()
    camion1.aceleracion_frenado()
    camion1.sistema_direccion()
    camion1.tipo_seguridad()
    camion1.luces()
    camion1.sistema_espejo()
    camion1.apagado()


# ******************** ZONA DE CODIGO PRINCIPAL ****************

print("************ INDUSTRIA DE VEHICULOS ************")
probar_vehiculos()