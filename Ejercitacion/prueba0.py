"""Escribir una función para validar una nueva clave de acceso.
La función deberá recibir una cadena de caracteres, que contendra la clave
candidata, que fue ingresada por el usuario; y devolvera True o False,
dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud total de entre 4 y 10 caracteres alfabeticos, inclusive.
- Estar formada por mayor cantidad de letras minusculas que mayusculas.
- El ultimo caracter, debe ser una letra minuscula.
- La clave puede tener como maximo 2 caracteres que sean vocales.
"""

def validar_contraseña(clave):
    devolver = True
    posicion = 0
    cont_minusculas = 0
    cont_vocales = 0
    vocales = "aeiou"
    if (len(clave) < 4 or len(clave) > 10 or clave[-1].islower() == False):
        devolver = False
    else:
        while (posicion < len(clave) and devolver):
            if ((clave[posicion].isalpha() == False) or cont_vocales > 2):
                devolver = False
            elif (clave[posicion].islower() == True):
                cont_minusculas += 1
            if (clave[posicion].lower() in vocales):
                cont_vocales += 1
            
            posicion += 1
        
        if (cont_minusculas < len(clave) // 2):
            devolver = False
        
    return devolver
#----------------------------------------------------------------------------------------------#
contraseña = input("Ingresar clave: ")
print(validar_contraseña(contraseña))



