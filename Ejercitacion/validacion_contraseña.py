'''Escribir una funcion para validar una nueva clave de acceso.
La funcion debera recibir una cadena de caracteres, que contendra la clave
candidata, que fue ingresada por el usuario; y devolvera True o False,
dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud total de entre 8 y 12 caracteres
- Estar formada por mayor cantidad de caracteres alfabeticos que caracteres
  numericos, y no puede contener ningun otro caracter.
- No puede comenzar con un caracter numerico, ni los 3 ultimos ser alfabeticos.
- La suma de los caracteres numericos no puede ser mayor a 35.
'''

def validacion_clave(clave):
     devolver = True
     posicion = 0
     contador = 0
     cont_caracteres = 0
     cont_numeros = 0
     if (8 <= len(clave) <= 12 and clave[0].isnumeric() == True and clave[-3: ].isalpha() == True):
        while (posicion < len(clave) and clave.isalnum() == True and contador <= 35 and devolver):
             if (clave[posicion].isalpha() == True):
                 cont_caracteres +=  1
             elif(clave[posicion].isnumeric() == True):
                 cont_numeros += 1
         if((cont_caracteres + cont_numeros == len(clave)) and (cont_caracteres > cont_numeros)):
             devolver = True
 
         posicion += 1
    
     else:
        devolver = False
     
   return devolver

# def validar_acceso(clave):
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

# import doctest
# doctest.testmod()
#--------------------------------------------------  Bloque Principal -----------------------------------------#
print(validar_acceso("0nah2el9"))
