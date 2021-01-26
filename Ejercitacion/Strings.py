"""Ejercicio 1
Escribir una función que reciba una cadena de caracteres.
La función deberá evaluar si la cadena recibida representa
un número binario, y en ese caso devolver True, de lo
contrario, deberá devolver False."""
# def validar(string):
#     numeros_binarios = "01"
#     devolver = False
#     if numeros_binarios in string:
#         devolver = True
#     else:
#         devolver = False
#     return devolver
""" Una solucion es esta o mejor aun usando while"""
# def es_binario(cadena):
#     posicion = 0
#     numeros_binarios = "01"
#     largo = len(cadena)
#     while (posicion < largo and cadena[posicion] in numeros_binarios):
#         posicion += 1
#     return (posicion == largo)
# #--------------------- Bloque Principal --------------------#
# caracter = input("Ingrese numero binario: ")
# print("Es binario" if es_binario(caracter) else "No es binario")
#---------------------------------------------------------------------#
"""Escribir una función que reciba una cadena de caracteres que representa una
dirección de mail. La función deberá devolver True ó False, en función de
haber evaluado que dicha dirección está bien formada.
Se debe controla que: 
a. Que no contenga blancos
b. Que sólo se utilicen letras y/o números para la parte del nombre,delante de
la @
c.Que haya exactamente una arroba
d. Que los nombres de dominio sean: fi.uba.ar ó gmail.com"""

# def validar_mail(mail):
#     """La funcion valida una direccion de mail y devuelve True o False
#     >>> validar_mail("nlescano@fi.uba.ar")
#     True
#     >>> validar_mail("lescanoagustin10nahuel@gmail.com")
#     True
#     >>> validar_mail(" ")
#     False
#     >>> validar_mail("hsywy6@@.com2")
#     False
#     """
#     #------Funcion--------#
#     if (" " in mail):
#         devolver = False
#     elif (not mail[:mail.index("@")].isalnum()):
#         devolver = False
#     elif (mail.count("@") != 1):
#         devolver = False
#     elif (mail[mail.index("@"):] != "@fi.uba.ar") and (mail[mail.index("@"):] != "@gmail.com"):
#         devolver = False
#     else:
#         devolver = True
#     return devolver
# #---------------------- Bloque Principal ------------------#
# email = input("Ingresa tu direccion de mail: ")
# print(validar_mail(email))
# import doctest
# doctest.testmod()
"""Escribir una función que reciba una cadena de caracteres a validar, y un
segundo parámetro, que contenga una cadena con los caracteres válidos.
La función debe devolver True, si la cadena a validar, está formada sólo
por caracteres válidos; en caso contrario, deberá devolver False."""
# def validar_cadena(cadena_a_validar, caracteres_validos):
#     posicion = 0
#     largo = len(cadena_a_validar)
#     while (posicion < largo and cadena_a_validar[posicion] in caracteres_validos):
#         posicion += 1
#     return (posicion == largo > 0)
# #------------------------- Bloque Principal -------------------------------#
# cadena = input("Ingrese cadena a validar: ")
# print("Es valido" if validar_cadena(cadena, "hohohlads") else "Es invalido")
""" Escribir una función que reciba una palabra ó frase, y devuelva True,
si es un palíndromo, ó False en caso contrario. 
Asumir que la cadena a recibir, sólo estará formada por caracteres alfabéticos
y espacios en blanco.
Un palíndromo es una palabra o frase que es igual si se lee de izquierda a
derecha que de derecha a izquierda. 
Ejemplos:   Ana, ala, Neuquén, Oro, seres, radar
                        Arriba la birra
                        Amar da drama
                        Luz azul
                        La ruta natural
 """
# def palindromo(caracter):
#     """ La funcion verifica que el caracter ingresado sea palindromo y devuelve
#         True o False
#     >>> palindromo("Ana")
#     True
#     >>> palindromo("Neuquen")
#     True
#     >>> palindromo("Nahuel")
#     False
#     >>> palindromo("Algoritmos")
#     False
#     """
#     #----------- Funcion ------------------#
#     caracter = caracter.lower()
#     caracter2 = caracter.replace(" ", "")
#     devolver = False
#     if caracter[ : : -1] == caracter2:
#         devolver = True
#     else:
#         devolver = False
#     return devolver
# #-------------------- Test ------------------#
# import doctest
# doctest.testmod()
# string = input("Ingrese una cadena de caracteres: ")
# print(palindromo(string))
"""Escribir un programa que solicite el ingreso de palabras ó frases, y a
medida que se ingresan informar si se trata de un palíndromo.
Validar que la palabra ó frase ingresada, sólo este formada por caracteres
alfabéticos y por espacios en blanco.
El ingreso de las palabras ó frases, terminará cuando el usuario de enter, sin
ingresar nada.
La solución debe ser estructurada en funciones, que sigan los lineamientos de
la programación estructurada."""

nombre = input("ingresar nombre, con ENTER sale: ")
while nombre != "":
    edad = int(input("Ingrese edad: "))
    if edad >= 18:
        print("Sos mayor de edad, podes ir preso")
    else:
        print("Sos menor de edad, anda a dormir ya es tarde")
    





