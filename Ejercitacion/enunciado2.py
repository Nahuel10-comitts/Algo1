"""Escribir una funcion para validar una nueva clave de acceso.
La funcion debera recibir una cadena de caracteres, que contendra la clave
candidata, ingresada por el usuario; y devolvera True o False, dependiendo de
si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud de entre 6 y 10 caracteres inclusive
- Solo puede estar formada por vocales (no acentuadas) y digitos pares
- Debe estar formada por una combinacion cualquiera de:
    vocales mayusculas y digitos pares, o
    vocales minusculas y digitos pares, o
    vocales minusculas y mayusculas, o
    vocales minusculas, mayusculas y digitos pares"""



def validar_acceso(clave):
    """Claves a Validar:

    >>> validar_acceso("2Aeioue8")
    True
    >>> validar_acceso("Juananan")
    False
    """
    contmayusculas = 0
    contminusculas = 0
    contpares = 0
    
    posicion = 0
    devolver = False
    
    while (posicion < len(clave)) and (6 <= len(clave) <= 10) and (clave[posicion] in "AEIOUaeiou02468") and not devolver:
        if (clave[posicion] in "AEIOU"):
            contmayusculas += 1
        elif(clave[posicion] in "aeiou"):
            contminusculas += 1
        elif(int(clave[posicion]) %2 == 0):
            contpares += 1
        if ((contmayusculas+contminusculas+contpares) == len(clave)):
            devolver = True
        posicion += 1
        
    return devolver
    
import doctest
doctest.testmod()
