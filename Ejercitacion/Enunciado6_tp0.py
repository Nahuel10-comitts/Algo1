"""Escribir una función para validar una nueva clave de acceso.
La función deberá recibir una cadena de caracteres, que contendrá la clave candidata, que fue ingresada por el usuario; y devolverá True o False, dependiendo de si cumple con 
las condiciones establecidas.

La clave debe:
- Tener una longitud total de entre 8 y 12 caracteres
- Estar formada por mayor cantidad de caracteres alfabéticos que caracteres numéricos, y no puede contener ningún otro carácter.
- No puede comenzar con un carácter numérico, ni los 3 últimos ser alfabéticos.
- La suma de los caracteres numéricos no puede ser mayor a 35."""

def validar_clave(clave):

    """casos a validar:

    >>> validar_clave("juanpe234")
    True
    >>> validar_clave("2juanpe234")
    False

    """
    cant_caracteres = 0
    cant_num = 0
    posicion = 0
    devolver = False
    largo = len(clave)
    #numeros = "0123456789"
    
    if (8 <= largo <= 12) and (clave.isalnum()) and (not clave[0].isdigit()) and (not clave[-3:].isalpha()):
       
        while (posicion < largo):
            
            if clave.isalpha():
                cant_caracteres += 1
            
            else: #clave.isdigit():
                cant_num += 1
            
            posicion += 1
        
        if (cant_caracteres + cant_num == largo) and (cant_caracteres > cant_num):
            devolver = True
    
    else: 
        devolver = False

    return devolver

#--------------------------------------------------#

import doctest
doctest.testmod()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# def validar_acceso(clave):
#     
#     """casos a validar:
# 
#     >>> validar_acceso("juanpe234")
#     True
#     >>> validar_acceso("2juanpe234")
#     False
#     
#     """
#     
#     contcar = 0
#     contnum = 0
#     contador = 0
#     
#     posicion = 0
#     devolver = False
#     
#     if (clave[0].isnumeric() == True) or (clave[-3:].isalpha() == True):
#             devolver = False
#     else:
#         while (posicion < len(clave)) and (8 <= len(clave) <= 12) and (clave.isalnum() == True) and (contador <= 35) and not devolver:
#             if (clave[posicion].isalpha() == True):
#                 contcar += 1
#             elif (clave[posicion].isnumeric() == True):
#                 contnum += 1
#             posicion += 1
#         if (contcar+contnum == len(clave)) and (contcar>contnum):
#             devolver = True
#             
#     return devolver
# 
# import doctest
# doctest.testmod()
# print(validar_acceso("juanpe234"))