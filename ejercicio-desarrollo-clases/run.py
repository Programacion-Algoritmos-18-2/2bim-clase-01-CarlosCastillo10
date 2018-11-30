"""
	Autor: Carlos Castillo
"""

from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir
from paquete_modelo.mimodelo import Alumno

m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

lista = m.obtener_informacion() # Guardamos en lista lo que retorna el metodo
lista = [x.split("|") for x in lista] # Separamos los datos delimitados por "|" 

lista = lista[1:] # Guardamos en lista todos los elementos a partir de la posicon 1

m2.archivo.write("Nombre|Promedio\n") #Escribirmos en el archivo el encabezado.

for x in lista:
    a = Alumno(x[0], x[1], x[2], x[3]) # Creamos el objeto de tipo Alumno y enviamos los parametros
    m2.agregar_informacion(a) # llamamos al metodo agregar_informacion() 
    print(a)


# Cerramos los archivos
m.cerrar_archivo()
m2.cerrar_archivo()
