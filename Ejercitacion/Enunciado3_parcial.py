""" EJERCICIO 2:

Escribir una funcion que devuelva verdadero si elegis un delivery que figura en un sitio, falso de lo 
contrario. 

La funcion recibe dos listas: una de platos y otra de valoraciones dadas en cantidad de motos.

La lista platos puede tener desde 1 a n platos.

La lista valoraciones puede tener desde 1 a m valoraciones (de 1 a 5).

Se elige el delivery cuando:

- En la lista platos tiene "milanesa" y "papas fritas" (ambos platos deben estar como dos platos distintos) 
o "pizza napolitana"  

- Ademas de lo anterior, el promedio de valoraciones tiene que ser mayor o igual que 3,

  salvo que tenga algun 1, en ese caso no se acepta

******************************************************* """

def recepcion_delivery(comidas, puntajes):
    """ 
    Casos de Prueba:

    >>> recepcion_delivery(comidas_1, puntajes_1)
    False
    >>> recepcion_delivery(comidas_2, puntajes_3)
    False
    >>> recepcion_delivery(comidas_3, puntajes_2)
    True
    >>> recepcion_delivery(comidas_4, puntajes_5)
    True
    >>> recepcion_delivery(comidas_5, puntajes_5)
    False
    >>> recepcion_delivery(comidas_4, puntajes_4)
    False
    >>> recepcion_delivery(comidas_5, puntajes_4)
    False

    """
    delivery = True
    total_puntaje = 0
    
    for puntaje in puntajes:

        if puntaje == 1:
            delivery = False
        
        total_puntaje += puntaje
        
    promedio = total_puntaje / len(puntajes)
    
    if promedio < 3 or not (("milanesa" in comidas and "papas fritas" in comidas) or "pizza napolitana" in comidas) :
        delivery = False
        
    return delivery

# ------------------------------- Bloque Principal -----------------------------#

comidas_1 = ["milanesa", "pollo", "tarta de queso"]
comidas_2 = ["tira de asado", "ensalada mixta", "pizza napolitana"]
comidas_3 = ["milanesa", "ravioles", "papas fritas"]
comidas_4 = ["pizza napolitana", "batatas fritas"]
comidas_5 = ["milanesa"]
puntajes_1 = [5]
puntajes_2 = [2, 5]
puntajes_3 = [1, 5, 4, 4]
puntajes_4 = [3, 2, 2, 2]
puntajes_5 = [3, 3]

import doctest
doctest.testmod()
# print(recepcion_delivery(comidas_3, puntajes_2))
# print(recepcion_delivery(comidas_2, puntajes_3))
# print(recepcion_delivery(comidas_4, puntajes_4))

