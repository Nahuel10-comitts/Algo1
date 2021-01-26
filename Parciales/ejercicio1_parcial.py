"""
Escribir una función que reciba una cadena de caracteres alfanuméricos y devuelva una cadena formada por las vocales que hay en
la cadena, en el orden que aparecen, sin repetirlas . Estén o no acentuadas, ó esten en mayúscula ó minúscula,
sólo deben aparecer una vez (ver los casos de prueba).

Validar que la cadena recibida esté formada sólo por caracteres alfanuméricos, caso contrario, devovler '*' (caracter asterisco).

Deberá comprobar el correcto funcionamiento, mediante los siguientes casos de prueba usando la librería doctest.

Para "Algoritmos y Programación", debe devolver '*'
Para "Programación1", debe devolver 'oai'
Para "", debe devolver '*'
Para "+*ab", debe devolver '*'
Para "AÉREO", debe devolver 'AÉO'
Para "Aerolíneas", debe devolver 'Aeoí'
Para "-P-f/7", debe devolver '*'

INCLUÍ EL ENUNCIADO QUE TE HA TOCADO, en el programa como comentario inicial, seleccionado y pegando todo el texto.

NOMBRA TU ARCHIVO DE LA SIGUIENTE FORMA: padrón_apellido_ej1.py  reemplazando padrón por tu padrón y apellido, por tu apellido.
"""
""" 
    >>> validar_clave("Algoritmos y Programación")
    *
    >>> validar_clave("Programación1")
    oai
    >>> validar_clave("")
    *
    >>> validar_clave("+*ab")
    *
    >>> validar_clave("Algoritmos y Programación")
    *
    >>> validar_clave("Algoritmos y Programación")
    *
    >>> validar_clave("Algoritmos y Programación")
    *
    """
    
                
#----------------------- Bloque Principal ---------------------------#

import doctest
doctest.testmod()
