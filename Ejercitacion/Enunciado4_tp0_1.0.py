"""Escribir una función para validar una nueva clave de acceso.
La función debe recibir una cadena de caracteres, que contendrá la clave candidata, que fue ingresada por el usuario; y devolverá True o False, dependiendo de si cumple con las 
condiciones establecidas.

La clave debe:
- Tener una longitud total de entre 4 y 10 caracteres
- Estar formada por igual cantidad de caracteres numéricos y caracteres alfabéticos, y no puede contener ningún otro carácter.
- Los caracteres alfabéticos y numéricos deben estar intercalados, no puede haber dos letras consecutivas, ni dos dígitos numéricos consecutivos."""

def validar_clave(clave):
    
    """ Casos de Prueba:
 
    >>> validar_clave("asd")
    False
    >>> validar_clave("hola")
    False
    >>> validar_clave("a1a1d")
    False
    >>> validar_clave("aa5j")
    False
    >>> validar_clave("a11s")
    False
    >>> validar_clave("j5d4")
    True
    >>> validar_clave("5j6g3d")
    True
    >>> validar_clave("a5f8b9l0p1")
    True
    """
    
    #letras = "abcdefghijklmnñopqrstuvwxyz"
    #numeros = "0123456789"
    cant_digitos = 0 
    cant_alpha = 0
    posicion = 0
    indice = 0
    largo = len(clave)
    devolver = False
    
    if 4 < largo < 10 and clave.isalnum():
        
        while posicion < largo and not devolver:
            
            if clave[posicion].isdigit():
                cant_digitos += 1
            
            else: #clave[posicion].isalpha()
                cant_alpha += 1
            
            if cant_alpha == cant_digitos:
                devolver = True
            
            posicion += 1
            
        while indice < (largo - 1) and not devolver:

            if clave[indice].isalpha() == clave[indice + 1].isalpha():
                devolver = False
            
            else: #clave[indice].isdigit() == clave[indice + 1].isdigit()
                devolver = False

            indice += 1
            
    return devolver 
            
            #for i in clave.lower():
                #if i.isdigit():
                    #contador_num += 1
                #else: #i.isalpha()
                    #contador_letras += 1
#--------------------------------------------------------#
# def main():
#     cadena = input("Ingrese cadena a validar: ")
#     print(validar(cadena))
# 
# main()            


# -------------------------------- Bloque Principal -----------------------------#
 
import doctest
doctest.testmod()
 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++