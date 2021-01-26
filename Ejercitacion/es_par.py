def es_par(numero):
    """ La funcion evalua si un numero es par o no.
    >>> es_par(5)
    False
    >>> es_par(6)
    True
    >>> es_par(-1)
    False
    >>> es_par(-8)
    True
    >>> es_par(0)
    True
    """
    devolver = True
    if numero % 2 != 0:
        devolver = False
        
    return devolver
#------------------ Bloque Principal ---------------#
import doctest
doctest.testmod()
