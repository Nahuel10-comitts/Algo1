# Escribir un programa en Python que pida el ingreso por pantalla e imprima si es bisiesto
# o no.
# Un año es bisiesto si es divisible por 4, pero no por 100, a menos que tambien sea
# divisible por 400.
año = int(input("Ingrese año: "))
bisiesto = False
if ((año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0)):
#     if ((año % 100 != 0)or (año % 400 == 0)):
    bisiesto = True
if bisiesto:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
    
    