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

def validar(clave):
    """Casos a validar:
    >>> validar("AE64ui28")
    True
    >>> validar("Iu24aE8")
    True
    >>> validar("hsgye23")
    False
    >>> validar("Nw37loq379Nah1")
    False
    """
    vocales_mayus = 0
    vocales_minus = 0
    digitos_pares = 0
    posicion = 0
    devolver = False
    largo = len(clave)
    
    if 6 <= largo <= 10:
        
        while posicion < largo and clave[posicion] in "AEIOUaeiou02468" and not devolver:
            
            if clave[posicion].isupper():
                vocales_mayus += 1
            
            elif clave[posicion].islower():
                vocales_minus += 1
            
            elif int(clave[posicion]) % 2 == 0:
                digitos_pares += 1
            
            if (vocales_mayus + vocales_minus + digitos_pares) == largo:
                devolver = True
            
            posicion += 1
    
    else:
         devolver = False
    
    return devolver

import doctest
doctest.testmod()

#def main():
#    cadena = input("Ingrese clave a validar: ")
#    print(validar(cadena))

#main()