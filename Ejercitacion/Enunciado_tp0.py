"""Escribir una funcion para validar una nueva clave de acceso.
La funcion debera recibir una cadena de caracteres, que contendra la clave
candidata, que fue ingresada por el usuario; y devolvera True o False,
dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud de entre 8 y 12 caracteres inclusive
- Solo puede estar formada por letras y numeros
- Debe contener al menos una letra mayuscula, una letra minuscula y 1 numero"""
def validar(clave):
    """ Casos de Prueba a comprobar:

    >>> validar("florencia25")
    False
    >>> validar("florencia")
    False
    >>> validar("ElFede3")
    False
    >>> validar("23894093")
    False
    >>> validar("HOLAHOLA")
    False
    >>> validar("HOLA_hola2")
    False
    >>> validar("ElÑoño00")
    True
    >>> validar("Facundo850")
    True
    >>> validar("0Florcita")
    True
    >>> validar("2A3b4C5D6E7F")
    True
   
    """
    posicion = 0 
    cant_mayus = 0
    cant_minus = 0
    cant_num = 0
    devolver = False
    largo = len(clave)
    
    if  (8 <= largo <= 12 and clave.isalnum()):
        while (posicion < largo and not devolver):
        
            if clave[posicion].isupper():
                cant_mayus = 1
        
            elif clave[posicion].islower():
                cant_minus = 1
        
            else: #clave[posicion].isdigit():
                cant_num = 1
        
            if ((cant_mayus + cant_minus + cant_num) == 3):
                devolver = True
        
            posicion += 1
    
    return devolver 
#----------------------------------------------------------#
#cadena = input("Ingrese texto a validar: ")
#print(validar(cadena))
import doctest
doctest.testmod()
