"""
Ejemplos de manejo de excepciones

"""

try:
    edad = int(input("Ingrese su edad por favor: "))
    print("Su edad es: %d" %(edad))

except NameError as e:
    
    print("Existe un error %s" %e)

except ValueError as e:
    
    print("Existe un error (%s) %s" %(e.__class__ ,e))

#except Exception as e:
    
    #print("Existe un error (%s) %s" %(e.__class__ ,e))