from botella import Botella

class BotellaPlastico(Botella):
    def compatibilidad_temperatura(self):
        print("No se recomienda usarla con bebidas muy calientes porque se deforma.")

    def transparencia(self):
        print("Es transparente y deja ver parcialmente el contenido.")