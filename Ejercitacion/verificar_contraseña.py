"""Escribir una función para validar una nueva clave de acceso.
La función deberá recibir una cadena de caracteres, que contendrá la clave candidata, ingresada por
el usuario; y devolverá True o False, dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud de entre 6 y 10 caracteres inclusive
- Solo puede estar formada por vocales (no acentuadas) y dígitos pares
- Debe estar formada por una combinación cualquiera de:
    Vocales mayúsculas y dígitos pares, o
    Vocales minúsculas y dígitos pares, o
    Vocales minúsculas y mayúsculas, o
    Vocales minúsculas, mayúsculas y dígitos pares
"""

def verificar_contraseña(clave):
    posicion = 0
    cant_mayusculas = 0
    cant_minusculas = 0
    cant_digitos_pares = 0
    devolver = False
    if (6 <= len(clave) <= 10):
        while (posicion < len(clave) and clave[posicion] in "AEIOUaeiou02468" and not devolver):
            if (clave[posicion] in "AEIOU"):
                cant_mayusculas += 1
            elif (clave[posicion] in "aeiou"):
                cant_minusculas += 1
            elif (int(clave[posicion]) % 2 == 0):
                cant_digitos_pares += 1
            if ((cant_mayusculas + cant_minusculas + cant_digitos_pares) == len(clave)):
                devolver = True
             
            posicion += 1
    else:
        devolver = False
        
    return devolver
#----------------------------------------- Bloque Principal -------------------------------------------#
contraseña = input("Ingresar clave: ")
print(verificar_contraseña(contraseña))
        
