"""#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Escribir una funcion que devuelva verdadero si elegis una pelicula que te proponen,
falso de lo contrario.

La funcion recibe dos listas: una de actores / actrices (actores) que actuan en esa
pelicula y otra de puntajes.

La lista actores puede tener desde 1 a n actores / actrices.

La lista puntajes puede tener desde 1 a m puntajes (del 1 al 10).

Se elige la pelicula cuando:

- En la lista actores tiene "Leonardo Di Caprio" o "Emma Stone" o "Jazmin Stuart" y 

- en la lista de puntajes, hay mayor cantidad de notas mayores o iguales a 6 que las

  que son menores a 6

Ademas, agrega DOS casos de prueba adicionales,en donde uno sea Falso y el otro Verdadero.

NOTA: bajate este archivo que tiene listas cargadas y casos de prueba. El codigo escribilo ahi mismo.

NOMBRA TU ARCHIVO DE LA SIGUIENTE FORMA: padrón_apellido_ej_2b.py reemplazando padrón por
tu padrón y apellido, por tu apellido."""

actores_1 = ["Gerardo Romano", "Jazmin Stuart", "Esteban Bigliardi"]
actores_2 = ["Emma Stone", "Michael Keaton", "Edward Norton"]
actores_3 = ["Ricardo Darin", "Soledad Villamil"]
puntajes_1 = [6]
puntajes_2 = [2, 8]
puntajes_3 = [5, 6, 9, 7, 8]

def elegir_pelicula(actores, puntajes):
    """ La funcion selecciona a las peliculas que contengan a los actores/actrices
    pedidos y devuelve True o False.
    Casos de Prueba:

    >>> elegir_pelicula(actores_1, puntajes_2)
    False
    >>> elegir_pelicula(actores_3, puntajes_3)
    False
    >>> elegir_pelicula(actores_2, puntajes_1)
    True"""
    #---------------------- Funcion ------------------------#
    actores_favoritos = ["Leonardo Di Caprio","Emma Stone", "Jazmin Stuart"]
    devolver = False
    for actor in actores:
        if actor in actores_favoritos:
            promedio = sum(puntajes) / len(puntajes)
            if promedio >= 6:
                devolver = True
            else:
                devolver = False
    return devolver
#------------------------ Test ------------------------------#
import doctest
doctest.testmod()
    
    
    