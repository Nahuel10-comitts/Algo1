"""Escribir una funcion para validar una nueva clave de acceso.
La función debera recibir una cadena de caracteres, que contendra la clave
candidata, ingresada por el usuario; y devolvera True o False, dependiendo de
si cumple con las condiciones establecidas.

La clave debe:
- Tener como minimo entre 4 y 8 digitos numericos
- Los digitos adyacentes no pueden ser iguales
- La clave no puede formar una secuencia ordenada creciente o decreciente"""

def validar(clave):
    """ Casos a validar:
    >>> validar("dca3210")
    False
    >>> validar("157g32ja")
    True
    >>> validar("19gjfa2")
    False
    >>> validar("amigo3298")
    True
    >>> validar("amigo3347")
    False
    >>> validar("1579amz")
    False
    """
    ordenada_creciente = True
    ordenada_decreciente = True
    digitos = 0
    indice = 0
    posicion = 0
    devolver = True
    largo = len(clave) - 1
    
    while indice < largo and devolver:
        
        if clave[indice] == clave[indice + 1]:

            if clave[indice].isdigit() and clave[indice].isdigit():

                devolver = False

        indice += 1

    if devolver:
        
        for numeros in clave:
            
            if numeros.isdigit():
                digitos += 1
        
        if digitos < 4 or digitos > 8:
            devolver = False
    
    while posicion < largo and (ordenada_creciente or ordenada_decreciente) and devolver:
        
        if clave[posicion] > clave[posicion + 1] and ordenada_creciente:
            ordenada_decreciente = False
        
        elif clave[posicion] < clave[posicion + 1] and ordenada_decreciente:
            ordenada_creciente = False
        
        else:
            ordenada_creciente = False
            ordenada_decreciente = False
        
        posicion += 1
    
    if ordenada_creciente or ordenada_decreciente:
        devolver = False

    return devolver
#------------------------------#
# cadena = input("Ingrese clave a validar: ")
# print(validar("amigo347"))
import doctest
doctest.testmod()
        
