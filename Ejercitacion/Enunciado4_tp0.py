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

    cant_digitos = 0 
    cant_alpha = 0
    posicion = 0
    largo = len(clave)
    devolver = False
    
    if (not 4 <= largo <= 10) or (not largo % 2 == 0) or (not clave.isalnum()):
        devolver = False
    
    else:
        
        while posicion < (largo - 1) and not devolver:
            
            if clave[posicion].isalpha() and clave[posicion + 1].isdigit():
                cant_alpha += 1
            
            elif clave[posicion].isdigit() and clave[posicion + 1].isalpha():
                cant_digitos += 1
            
            else:
                devolver = False
            
            posicion += 1

            if posicion == largo -1:
    
                if clave[posicion].isalpha():
                    cant_alpha += 1

                else:
                    cant_digitos += 1 
            
        if cant_digitos == cant_alpha and  cant_digitos + cant_alpha == largo:
            devolver = True
            
    return devolver
    
# -------------------------------- Bloque Principal -----------------------------#
 
import doctest
doctest.testmod()
  
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# print(validar_clave("a11s"))
# print(validar_clave("5j6g3d"))
# print(validar_clave("hola"))
# print(validar_clave("asd"))
# validar_clave("a1a1d")
# 
# validar_clave("hola")
# print(validar_clave("asd"))
# validar_clave("aa5j")
# print(validar_clave("a11s"))
# print(validar_clave("j5d4"))
# validar_clave("5j6g3d")
# print(validar_clave("a5f8b9l0p1"))
# print(validar_clave("a5g66"))
#             if posicion == largo -1: 
#                 
#                 if clave[posicion].isalpha():
#                     cant_alpha += 1
#                 
#                 else:
#                     cant_digitos += 1

#             if not (clave[posicion].isdigit() or clave[posicion+1].isdigit()):
#             if clave[posicion].isdigit() and clave[posicion + 1].isalpha():
#                 cant_digitos += 1
                #cant_alpha += 1
#             elif not (clave[posicion].isalpha() or clave[posicion+1].isalpha()):
#                  else: #clave[posicion].isalpha() and clave[posicion + 1].isdigit():
#                 cant_alpha += 1
#                 cant_digitos += 1
                            
#             posicion += 2

""" Mi codigo original """
# def validar(clave):
#     #letras = "abcdefghijklmnñopqrstuvwxyz"
#     #numeros = "0123456789"
#     cant_digitos = 0 
#     cant_alpha = 0
#     posicion = 0
#     indice = 0
#     largo = len(clave)
#     devolver = False
#     
#     if 4 < largo < 10 and clave.isalnum():
#         
#         while posicion < largo and not devolver:
#             
#             if clave[posicion].isdigit():
#                 cant_digitos += 1
#             
#             else: #clave[posicion].isalpha()
#                 cant_alpha += 1
#             
#             if cant_alpha == cant_digitos:
#                 devolver = True
#             
#             posicion += 1
#             
#         while indice < (largo - 1) and not devolver:
# 
#             if clave[indice].isalpha() == clave[indice + 1].isalpha():
#                 devolver = False
#             
#             else: #clave[indice].isdigit() == clave[indice + 1].isdigit()
#                 devolver = False
# 
#             indice += 1
# 
#     else: 
#         devolver = False
# 
#     return devolver 
#             
#             #for i in clave.lower():
#                 #if i.isdigit():
#                     #contador_num += 1
#                 #else: #i.isalpha()
#                     #contador_letras += 1
# #--------------------------------------------------------#
# def main():
#     cadena = input("Ingrese cadena a validar: ")
#     print(validar(cadena))
# 
# main()            
