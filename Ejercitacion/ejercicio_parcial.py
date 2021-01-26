
'''
Ejercicio:

Elecciones PASO

Primera parte:

Se cargan datos en un diccionario en forma manual. Estos datos consisten en el nombre de un partido politico,
la cantidad de votos validos, y la cantidad de votos invalidos que obtuvo en alguna localidad de nuestro
país (no se ingresa la localidad, solo se ingresa el nombre del partido y dos enteros, y un partido puede ser
ingresado muchas veces).
La carga finalizara cuando el data-entry presione enter cuando se le pida el nombre de un partido.

Escribir una funcion que permita realizar la carga, y su valor de retorno sea el diccionario deseado.
'''

def cargar_datos_elecciones():
    votacion = {}
    partido_politico = input("Ingrese el partido politico: ")
    while partido_politico != "":
        votos_validos = int(input("Ingrese la cantidad de votos validos: "))
        votos_invalidos = int(input("Ingrese la cantidad de votos invalidos: "))
        if partido_politico in votacion:
            votacion[partido]["validos"] += votos_validos
            votacion[partido]["invalidos"] += votos_invalidos
        else:
            votacion[partido] = {"validos": votos_validos, "invalidos": votos_invalidos}
        partido_politico = input("Ingrese el partido politico: ")
    return votacion

'''
Segunda parte:

En esta seccion buscaremos obtener algunas estadisticas a partir del diccionario cargado en la primera parte.
Se deben aplicar los criterios de modularizacion vistos en clases. Se pide calcular:

- Cual es partido ganador de las elecciones (es decir, el que sume mayor cantidad de votos validos).'''

def ganador_elecciones(votacion):
    partido_ganador = ""
    votos_ganador = -1
    for partido in votacion:
        if votacion[partido]["votos_validos"] > votos_ganador:
            partido_ganador = partido
            votos_ganador = votacion[partido]["votos_validos"]

    return partido_ganador, votos_ganador


'''
- Cuales son los partidos que pasaron estas elecciones PASO (es decir, aquellos que sacaron una cantidad mayor
a un 10% respecto del total de votos ingresados considerando unicamente los votos validos).'''

def total_votos(votacion):
    votos = 0
    for partido in votacion:
        votos += votacion[partido]["votos_validos"]
    return votos

def clasificados_eleccion_general(votacion):
    votos_totales = total_votos(votacion)
    clasificados = []
    for partido in votacion:
        if votacion[partido]["votos_validos"] / votos_totales > 0.1:
            clasificados.append(partido)
    return clasificados


'''
- Imprimir un ranking que indique cuales son los partidos que mayor cantidad de votos invalidos recibieron.
Este ranking debe ser impreso en forma descendente (es decir, los de mayor cantidad de votos invalidos primero).
'''

{"a": "hola",
 "b": "algoritmos"}

[("a", "hola"), ("b", "algoritmos")]

sorted(dic.items(), key = lambda x: len(x[1]))

def ranking_votos_invalidos(votacion):
    ranking = sorted(votacion.items(), key = lambda tupla_votos: tupla_votos[1]["votos_invalidos"], reverse=True)
    return ranking


'''
- Cual es el porcentaje de votos invalidos respecto al total de votos (se entiende al total de votos por la
suma entre los votos validos y los votos invalidos).
    
'''