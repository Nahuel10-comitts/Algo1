""" Escribir una función para validar una nueva clave de acceso. La función deberá recibir una cadena de caracteres, que contendra la clavecandidata, que fue ingresada por el 
usuario; y devolvera True o False, dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud total de entre 4 y 10 caracteres alfabeticos, inclusive.
- Estar formada por mayor cantidad de letras minusculas que mayusculas.
- El ultimo caracter, debe ser una letra minuscula.
- La clave puede tener como maximo 2 caracteres que sean vocales."""

def validar(clave):
    """ Casos de Prueba:
    >>> validar("florencia25")
    False
    >>> validar("eAEIOui")
    False
    >>> validar("97532")
    False
    >>> validar("1AE5b2")
    False
    >>> validar("dia")
    False
    >>> validar("dias")
    True
    >>> validar("LuneS")
    False
    >>> validar("Lunes")
    True
    >>> validar("aBcdeio")
    False
    >>> validar("aBcdenm")
    True
    >>> validar("MartES")
    False
    >>> validar("tarta")
    True
    >>> validar("Nahuel")
    False
    >>> validar("PiZzas")
    True
    """
    devolver = False
    vocales = "aeiou"
    posicion = 0
    largo = len(clave)
    cant_mayus = 0
    cant_minus = 0
    cant_vocales = 0

    if 4 <= largo <= 10 and clave.isalpha() and clave[-1].islower():
        
        while posicion < largo:
            
            if clave[posicion].isupper():
                cant_mayus += 1
            
            else: #clave[posicion].islower():
                cant_minus += 1
            
            if clave[posicion].lower() in vocales:
                cant_vocales += 1
            
            posicion += 1

        if cant_minus > cant_mayus and cant_vocales <= 2:
            devolver = True
            
    else:
        devolver = False
    
    return devolver 
#----------------------------#
import doctest
doctest.testmod()
# cadena = input("Ingrese cadena a validar: ")
# print(validar(cadena))
