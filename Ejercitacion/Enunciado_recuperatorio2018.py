"""1) Escribir una función que, dado un texto que se pasa por parámetro, devuelva el valor booleano verdadero si todas las palabras tienen 6 letras o menos, caso contrario 
devuelve falso. Las palabras están separadas solo por blancos. """
def validar_texto(texto):

    """ Casos de prueba:
    >>> validar_texto("Hola")
    True
    >>> validar_texto("banana")
    True
    >>> validar_texto("Lescano")
    False
    >>> validar_texto("arribaLaBirra")
    False"""

    devolver = False
    largo = len(texto)

    if largo <= 6:
        devolver = True
    
    return devolver
#--------- Bloque de Prueba -----------#
import doctest
doctest.testmod(verbose = True)

#print(validar_texto("NahuelAgustin"))
#print(validar_texto("H o l a"))
""" Cuidado: el enunciado dice que tiene que las palabras solo pueden estar separados por blancos"""