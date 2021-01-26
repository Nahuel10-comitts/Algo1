#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Escribir una funcion para validar una nueva clave de acceso.
La funcion debera recibir una cadena de caracteres, que contendra la clave
candidata, que fue ingresada por el usuario; y devolvera True o False,
dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud de entre 8 y 12 caracteres inclusive
- Solo puede estar formada por letras y numeros
- Debe contener al menos una letra mayuscula, una letra minuscula y 1 numero

*******************************************************************************
Aqui coloca tu Padron:
Aqui coloca tu Apellido y Nombre:
-------------------------------------------------------------------------------
"""

def validar_clave(clave):

    """ Casos de Prueba a comprobar:

    >>> validar_clave("florencia25")
    False
    >>> validar_clave("florencia")
    False
    >>> validar_clave("ElFede3")
    False
    >>> validar_clave("23894093")
    False
    >>> validar_clave("HOLAHOLA")
    False
    >>> validar_clave("HOLA_hola2")
    False
    >>> validar_clave("ElÑoño00")
    True
    >>> validar_clave("Facundo850")
    True
    >>> validar_clave("0Florcita")
    True
    >>> validar_clave("2A3b4C5D6E7F")
    True
   
    """

    #--------- Escribi el Codigo de la Funcion a partir de aqui ---------------#
    posicion = 0
    cont_minusculas = 0
    cont_mayusculas = 0
    cont_numeros = 0
    devolver = False
    if (12 <= len(clave) <= 8 or clave.isalnum() == False): 
        devolver = False
    else:
        while (posicion < len(clave) and not devolver):
            if (clave[posicion].islower() == True):
                cont_minusculas = 1      
            elif (clave[posicion].isupper() == True):
                cont_mayusculas = 1    
            elif (clave[posicion].isdigit() == True):
                cont_numeros = 1
            if ((cont_minusculas + cont_mayusculas + cont_numeros) == 3):
                devolver = True          
            posicion += 1              
    return devolver
   
# -------------------------------- Bloque Principal -----------------------------#
# contraseña = input("clave: ")
# print(validar_clave(contraseña))
import doctest
doctest.testmod()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++