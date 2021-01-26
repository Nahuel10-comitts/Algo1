"""

Ejercicio 2 e)

 

Escribir una función que devuelva verdadero si te conviene elegir un delivery que figura en un sitio, falso de lo contrario.

La función recibe dos listas: una de platos ofrecidos y otra de platos deseados.

Las longitudes de las listas pueden ser diferentes.

 

Se recomienda el delivery cuando:

En la lista de ofrecidos tiene la mitad o más de los platos deseados (en caso de tener cantidad impar asumir la división entera).

 

Además, agrega DOS casos de prueba adicionales, en donde uno sea Falso y el otro Verdadero.

 Nota: el archivo debe llamarse: ej_2e_apellido.py



 

----------------------------------------------------------------------

Aquí coloca tu padrón: 105743

Aquí coloca tu Apellido y Nombre: Lescano Nahuel

----------------------------------------------------------------------

"""

 

ofrecidos_1 = ["milanesa", "pollo", "tarta de queso"]

ofrecidos_2 = ["tira de asado", "pollo", "ensalada mixta", "pizza napolitana"]

ofrecidos_3 = ["pizza napolitana", "ñoquis", "Tarta de jamon y queso"] #Agrego 

 

deseados_1 = ["tira de asado", "pollo", "ravioles"]

deseados_2 = ["tira de asado", "pollo", "ravioles", "canelones"]

deseados_3 = ["pizza napolitana", "ñoquis", "ensalada"] #Agrego

 

 

def elegir_delivery(ofrecidos, deseados):

    """ Casos de Prueba:

    >>> elegir_delivery(ofrecidos_1, deseados_1)
    True
    >>> elegir_delivery(ofrecidos_1, deseados_2)
    False
    >>> elegir_delivery(ofrecidos_2, deseados_2)
    True
    >>> elegir_delivery(ofrecidos_3, deseados_1) #Agrego
    False
    >>> elegir_delivery(ofrecidos_3, deseados_3) #Agrego
    True
    """
    #-------------- Codigo --------------#
    devolver = False
    contador = 0

    #for comida in deseados:

    for comida_ofrecida in ofrecidos:
            
        if comida_ofrecida in deseados:
                contador += 1
                
    if contador >= len(deseados) // 2:
        devolver = True

    return devolver
#--------------------------------------------------------------------#
import doctest
doctest.testmod(verbose = True)
# print(elegir_delivery(ofrecidos_1, deseados_1))