"""
Ejemplos de manejo de excepciones

"""

try:
     numero1 = int(input("\nIngrese un numero 1: "))
     numero2 = int(input("Ingrese un numero 2: "))

     operacion = numero1 / numero2
     print("El valor de la operacion es: %d" %(operacion))

except NameError as e:
    
    print("Existe un error %s" %e)

except ValueError as e:
    
    print("Existe un error (%s) %s" %(e.__class__ ,e)) 

except ZeroDivisionError as e:
	clase = e.__class__
	e = "No existe division para cero"
	print("\nExiste un error (%s) %s" %(clase ,e))

except Exception as e:
    
    print("Existe un error (%s) %s" %(e.__class__ ,e))