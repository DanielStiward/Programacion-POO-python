# ******************** ZONA DE FUNCIONES ***********************
from caballo import Caballo
from cocodrilo import Cocodrilo
from pato import Pato

def probar_animales():
    caballo1 = Caballo("Arthur", "5 años", "pradera", "pasto y heno", "grande", "blanco y negro")
    cocodrilo1 = Cocodrilo("Lagartijo", "10 años", "rio", "peces y carne", "grande", "verde oscuro")
    pato1 = Pato("Issai", "2 años", "estanque", "insectos y plantas acuaticas", "pequeño", "blanco")

    print(" CABALLO ")
    caballo1.mostrar_info()
    caballo1.moverse()
    caballo1.comunicacion()
    caballo1.alimentarse()
    caballo1.adaptacion()
    caballo1.instintos()
    caballo1.descanso()
    caballo1.sueno()
    caballo1.interaccion_social()
    caballo1.reproduccion()

    print("\n COCODRILO ")
    cocodrilo1.mostrar_info()
    cocodrilo1.moverse()
    cocodrilo1.comunicacion()
    cocodrilo1.alimentarse()
    cocodrilo1.adaptacion()
    cocodrilo1.instintos()
    cocodrilo1.descanso()
    cocodrilo1.sueno()
    cocodrilo1.interaccion_social()
    cocodrilo1.reproduccion()

    print("\n PATO ")
    pato1.mostrar_info()
    pato1.moverse()
    pato1.comunicacion()
    pato1.alimentarse()
    pato1.adaptacion()
    pato1.instintos()
    pato1.descanso()
    pato1.sueno()
    pato1.interaccion_social()
    pato1.reproduccion()


# ******************** ZONA DE CODIGO PRINCIPAL ****************

print("************ REINO ANIMAL ************")
probar_animales()   