def validar_clave(clave):
    """Escribir una función para validar una nueva clave de acceso.
    La función deberá recibir una cadena de caracteres, que contendrá la clave candidata,
    que fue ingresada por el usuario; y devolverá True o False, dependiendo de si cumple con
    las condiciones establecidas.

    Casos de Prueba a comprobar:

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
    posicion = 0
    cont_minusculas = 0
    cont_mayusculas = 0
    cont_numeros = 0
    devolver = False
    if clave.isalnum() == True and 8 <=len(clave)<= 12: 
        
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
    else:
        devolver = False
    return devolver
#--------------------------------Bloque Principal--------------------------------#
# contraseña = input("Ingrese su clave: ")
# print(validar_clave(contraseña))

import doctest
doctest.testmod()
