"""Escribir un programa en Python que solcite un numero por pantalla e imprima su valor
absoluto"""
numero_ingresado = int(input("Ingrese numero: "))
if numero_ingresado >= 0:
    valor_absoluto = numero_ingresado
else: #numero_ingresado < 0
    valor_absoluto = -numero_ingresado
print("El valor absoluto del numero ingresado es: ", valor_absoluto)

""" Escribir un programa en Python que solicite un numero por pantalla e imprima si el
numero es valido o no."""
numero_ingresado = int(input("Ingrese numero: "))
if (numero_ingresado % 2) != 0:
    print("El numero ingresado no es par")
else: #(numero_ingresado % 2) == 0
    print("El numero ingresado es par")
    
