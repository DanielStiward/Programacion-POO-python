#********** codigo principal **********
from botella_plastico import BotellaPlastico
from botella_vidrio import BotellaVidrio

botella1 = BotellaPlastico("plastico", "3050 ml", "cilindrica", "moderno", "rosca", "logo de marca")
botella2 = BotellaVidrio("vidrio", "750 ml", "alargada", "clasico", "corcho", "grabado artesanal")

print("BOTELLA DE PLASTICO")
botella1.mostrar_info()
botella1.contener_liquidos()
botella1.facilitar_vertido()
botella1.cierre_hermetico()
botella1.compatibilidad_temperatura()
botella1.transparencia()

print("\nBOTELLA DE VIDRIO")
botella2.mostrar_info()
botella2.contener_liquidos()
botella2.facilitar_vertido()
botella2.cierre_hermetico()
botella2.compatibilidad_temperatura()
botella2.transparencia()






