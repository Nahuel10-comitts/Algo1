"""#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Escribir una funcion que devuelva verdadero si elegis una pelicula que te proponen, falso de lo contrario.

La funcion recibe dos listas: una de actores / actrices (actores) que actuan en esa pelicula y otra de puntajes.

La lista actores puede tener desde 1 a n actores / actrices.

La lista puntajes puede tener desde 1 a m puntajes (del 1 al 10).

Se elige la pelicula cuando:

- En la lista actores tiene "Leonardo Di Caprio" o "Emma Stone" o "Jazmin Stuart" y 

- en la lista de puntajes, hay mayor cantidad de notas mayores o iguales a 6 que las

  que son menores a 6

Ademas, agrega DOS casos de prueba adicionales,en donde uno sea Falso y el otro Verdadero."""

actores_1 = ["Gerardo Romano", "Jazmin Stuart", "Esteban Bigliardi"]
actores_2 = ["Emma Stone", "Michael Keaton", "Edward Norton"]
actores_3 = ["Ricardo Darin", "Soledad Villamil"]
puntajes_1 = [6]
puntajes_2 = [2, 8]
puntajes_3 = [5, 6, 9, 7, 8]
#-------------------------------------------------------------------------------#

def elegir_pelicula(actores, puntajes):
    """ Casos de Prueba:

    >>> elegir_pelicula(actores_1, puntajes_2)
    False
    >>> elegir_pelicula(actores_3, puntajes_3)
    False
    >>> elegir_pelicula(actores_2, puntajes_1)
    True
    >>> elegir_pelicula(actores_3, puntajes_1)
    False
    >>> elegir_pelicula(actores_2, puntajes_3)
    True
    """
    #--------- Escribi el Codigo de la Funcion a partir de aqui ---------------#
    actores_favoritos = ["Leonardo Di Caprio", "Emma Stone", "Jazmin Stuart"]
    devolver = False
    
    for actor in actores:
        
        if actor in actores_favoritos:
            suma = sum(puntajes)
            promedio = suma / len(puntajes)
            
            if promedio >= 6:
                devolver = True

    return devolver

#---------------------------------------------------#
import doctest
doctest.testmod(verbose = True)
# print(elegir_pelicula(actores_1, puntajes_2))
# print(elegir_pelicula(actores_3, puntajes_3))
# print(elegir_pelicula(actores_2, puntajes_1))

#---------------------------- Codigo original -------------------------------#
"""    actores_favoritos = ["Leonardo Di Caprio", "Emma Stone", "Jazmin Stuart"]
    acum = 0
    promedio = 0
    devolver = False

    for actor in actores:
        if actor in actores_favoritos:
            for puntaje in puntajes:
                acum += puntaje
            promedio = acum / len(puntajes)
            
    if promedio >= 6:
        devolver = True
        
    else:
        devolver = False

    return devolver"""