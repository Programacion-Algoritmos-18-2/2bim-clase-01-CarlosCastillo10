"""
    creación de clases
"""

from .paqute_archivos.miarchivo import *
print("Hola")

class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod):
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo
    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    
    def __str__(self):
        """
        """
        return "%s\n%15s\n%20d\n%30d\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n" % (self.nombre, self.apellido,\
                self.edad, self.codigo)
