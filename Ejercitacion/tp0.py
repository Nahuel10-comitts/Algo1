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
    cont1=0
    cont2=0
    cont3=0

    posicion = 0
    vuelto = False
    while (posicion < len(clave)) and (8<=len(clave)<=12) and (clave.isalnum() == True) and not vuelto:
        if (clave[posicion].isupper() == True):
            cont1 = 1
        elif (clave[posicion].islower() == True):
            cont2 = 1
        elif(clave[posicion].isdigit() == True):
            cont3 = 1
        if ((cont1+cont2+cont3) == 3):
            vuelto = True
        posicion += 1
    return vuelto
   
# -------------------------------- Bloque Principal -----------------------------#
import doctest
doctest.testmod()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++