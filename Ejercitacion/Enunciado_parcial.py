"""EJERCICIO 1:

Escribir una funcion que reciba una cadena de caracteres alfanumericos y devuelva la cantidad de 
caracteres alfabeticos (letras) que hay en la cadena.

Debe validar que lo recibido sea una cadena formada solo por numeros y/o letras, si no lo fuera, la funcion 
debe devolver -1.

Debera comprobar el correcto funcionamiento, mediante los siguientes casos de prueba usando la libreria 
doctest.

Para "Algoritmos", debe devolver 10
Para "Ejercicio1", debe devolver 9
Para "z", debe devolver 1
Para "Algoritmos 1", debe devolver -1
Para "", debe devolver -1
Para "+*ab", debe devolver -1
Para "2por1", debe devolver 3
Para "01101011110", debe devolver 0"""

def validar_cadena(cadena):

    """ Casos de prueba:
    >>> validar_cadena("Algoritmos")
    10
    >>> validar_cadena("Ejercicio1")
    9
    >>> validar_cadena("z")
    1
    >>> validar_cadena("")
    -1
    >>> validar_cadena("+*ab")
    -1
    >>> validar_cadena("2por1")
    3
    >>> validar_cadena("01101011110")
    0
    """

    posicion = 0
    devolver = 0
    largo = len(cadena)
    
    if not cadena.isalnum():
        devolver = -1
    
    else:
        
        while posicion < largo:
            
            if cadena[posicion].isalpha():
                devolver += 1

            posicion += 1
        
    return devolver

#-------------- Bloque Principal -------------#

import doctest
doctest.testmod(verbose = True)

# print(validar_cadena(""))
# print(validar_cadena("Algoritmos"))
# print(validar_cadena("2por1"))
