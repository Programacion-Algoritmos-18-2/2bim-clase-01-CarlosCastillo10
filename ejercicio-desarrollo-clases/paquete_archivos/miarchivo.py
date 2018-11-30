"""
    Autor : Carlos Castillo
"""
import codecs # Importamos codecs para leer archivos.

class MiArchivo:
 
    # Constructor    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion.csv", "r") # Guardamos en archivo el csv.

    def obtener_informacion(self):
        return self.archivo.readlines() # Leemos cada linea de archivo

    def cerrar_archivo(self):
        self.archivo.close() # Cerramos el archivo


class MiArchivoEscribir:
    
    # Constructor
    def __init__(self):
    
        self.archivo = codecs.open("data/promedios.csv", "a") # Creamos o sobre escribimos el archivo "promedios.csv"

    
    # Metodo que permite agregar informacion al archivo
    def agregar_informacion(self, p):
        # Escribimos en el archivo
        self.archivo.write("%s|%.2f\n" % (p.obtener_nombre(), p.calcular_promedio()))

    def cerrar_archivo(self):
        self.archivo.close() # Cerramos el archivo
