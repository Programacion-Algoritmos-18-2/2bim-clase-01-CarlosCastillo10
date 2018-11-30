"""
    Autor: Carlos Castillo
"""

class Alumno(object):

    # Constructor
    def __init__(self, n, n1, n2, n3):
       
        self.agregar_nombre(n)
        self.agregar_nota1(float(n1))
        self.agregar_nota2(float(n2))
        self.agregar_nota3(float(n3))

    # Metodos de agregar
    def agregar_nombre(self, n):

        self.nombre = n

    def agregar_nota1(self, n1):
        
        self.nota1 = float(n1)
    
    def agregar_nota2(self, n2):

        self.nota2 = float(n2)

    def agregar_nota3(self, n3):
        
        self.nota3 = float(n3)

    # Metodos de obtener
    def obtener_nombre(self):
        
        return self.nombre
   
    def obtener_nota1(self):
        
        return self.nota1
    
    def obtener_nota2(self):
        
        return self.nota2

    def obtener_nota3(self):
        
        return self.nota3

    # Metodo que calcula el promedio de cada alumno
    def calcular_promedio(self):
        promedio =  (self.obtener_nota1() + self.obtener_nota2() + self.obtener_nota3()) / 3
        return promedio 
    
    # Sobre escribimos el metodo str
    def __str__(self):

        return ("\nAlumno: %s\n %15s %.2f\n %15s %.2f\n %15s %.2f\n %17s %.2f" %(self.obtener_nombre(),"Nota 1:",self.obtener_nota1(),
            "Nota 2:",self.obtener_nota2(),"Nota 3:",self.obtener_nota3(),"Promedio:",self.calcular_promedio()))
