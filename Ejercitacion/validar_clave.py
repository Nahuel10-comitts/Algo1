"""
Escribir una función para validar una nueva clave de acceso.
La función deberá recibir una cadena de caracteres, 
que contendrá la clave candidata, ingresada por el usuario; 
y devolverá True o False, 
dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener como mínimo entre 4 y 8 dígitos numéricos
- Los dígitos adyacentes no pueden ser iguales
- La clave no puede formar una secuencia ordenada creciente o decreciente

Debes probar la función con al menos 6 casos de prueba representativos,
 usando la librería doctest.
"""
def validar_clave(clave): #no funciona
    """
    >>> validar_clave("dca3210")
    False
    >>> validar_clave("157g32ja")
    True
    >>> validar_clave("19gjfa2")
    False
    >>> validar_clave("amigo3298")
    True
    >>> validar_clave("amigo3347")
    False
    >>> validar_clave("1579amz")
    False
    """
    #------------------- Funcion --------------------------#
    devolver = True
    indice = 0
    largo = len(clave) - 1
    while indice < largo and devolver:
        if clave[indice] == clave[indice + 1]:
            if clave[indice].isdigit() and clave[indice + 1].isdigit():
                devolver = False
    if devolver:
        digitos = 0
        for numeros in clave:
            if numeros.isdigit():
                digitos += 1
        if digitos < 4 or digitos > 8:
            devolver = False
    if devolver:
        secuencia_ordenada_creciente = True
        secuencia_ordenada_decreciente = True
        while indice < largo and (secuencia_ordenada_creciente or secuencia_ordenada_decreciente):
            if clave[indice] > clave[indice + 1] and secuencia_ordenada_creciente:
                secuencia_ordenada_decreciente = False
            elif clave[indice] < clave[indice + 1] and secuencia_ordenada_decreciente:
                secuencia_ordenada_creciente = False
            else: #clave[indice] == clave[indice + 1] and secuenica_ordenada_creciente and secuencia_ordenada_decreciente
                secuencia_ordenada_creciente = False
                secuencia_ordenada_decreciente = False
        if secuencia_ordenada_creciente or secuencia_ordenada_decreciente:
            devolver = False
            
    return devolver
#------------------------- Test ---------------------------#
import doctest
doctest.testmod()
# contraseña = input("Ingrese contraseña: ")
# print(validar_clave(contraseña))
    