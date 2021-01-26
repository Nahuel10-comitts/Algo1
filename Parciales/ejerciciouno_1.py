"""Escribir una función para validar una nueva clave de acceso.
La función deber recibir una cadena de caracteres, que contendrá la clave candidata, que fue ingresada por el usuario; y devolverá True o False, dependiendo
de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud total de entre 4 y 10 caracteres alfabéticos, inclusive.
- Estar formada por mayor cantidad de letras minúsculas que mayúsculas.
- El último caracter, debe ser una letra minúscula.
- La clave puede tener como máximo 2 caracteres que sean vocales.

Incluí en el programa, como comentario inicial, el enunciado que te ha tocado, seleccionando y pegando todo el texto.

Nombra a tu archivo de la siguiente forma: padrón_Apellido_ej1.py  reemplazando padrón por tu padrón y Apellido, por tu apellido."""

def validar_acceso(clave):
    """ Casos a validar:

    >>> validar_acceso("Andreskblr")
    True
    >>> validar_acceso("Kungamr")
    True
    >>> validar_acceso("AbCd")
    True
    >>> validar_acceso("Andreskubler1234")
    False
    >>> validar_acceso("ANDRESkub")
    False
    >>> validar_acceso("ANDRESKUb")
    False
    """
    #--------- Escribi el Codigo de la Funcion a partir de aqui ---------------#
    
    posicion = 0
    cantvocales = 0
    cantmin = 0
    vuelto = True
    while (posicion < len(clave)) and (4 <= len(clave) <= 10) and vuelto:
        if (clave[-1].islower == False) or (clave[posicion].isalpha == False) or (cantvocales > 2) :
            vuelto = False
        elif (clave[posicion].islower == True):
            cantmin += 1
        elif (clave[posicion].lower() in "aeiou") :
            cantvocales += 1
        
        posicion += 1
    if (cantmin < (len(clave)/2)):
        vuelto = False
    
    return vuelto
# -------------------------------- Bloque Principal -----------------------------#
import doctest
doctest.testmod()