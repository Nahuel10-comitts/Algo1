def validar_cadena(cadena):
    """ Casos de Prueba:

    >>> validar_cadena("Algoritmos y Programación")
    '*'
    >>> validar_cadena("Programación1")
    'oai'
    >>> validar_cadena("")
    '*'
    >>> validar_cadena("+*ab")
    '*'
    >>> validar_cadena("AÉREO")
    'AÉO'
    >>> validar_cadena("Aerolíneas")
    'Aeoí'
    >>> validar_cadena("-P-f/7")
    '*'
    """
    
    devolver = ""
    vocales = "áaéeíióoúu"
    if cadena.isalnum():
        for elemento in cadena:
            if (elemento.lower() in vocales): #and (elemento.lower() not in devolver)
                devolver += elemento
            
            encontrar = vocales.find(elemento.lower())
            if (encontrar == 0):
                vocales = vocales.replace(vocales[encontrar+1],"")
                vocales = vocales.replace(vocales[encontrar],"")
            elif (encontrar != -1) and (encontrar %2 != 0):
                vocales = vocales.replace(vocales[encontrar],"")
                vocales = vocales.replace(vocales[encontrar-1],"")
                
    else:
        devolver = "*"
        
    return devolver

import doctest
doctest.testmod(verbose=True)