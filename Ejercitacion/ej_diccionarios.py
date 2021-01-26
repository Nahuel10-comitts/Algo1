"""Ejercicio: Elecciones PASO
Primera parte:
Se cargan datos en un diccionario en forma manual. Estos datos consisten en el nombre de un partido
politico, la cantidad de votos validos, y la cantidad de votos invalidos que obtuvo en alguna
localidad de nuestro país (no se ingresa la localidad, solo se ingresa el nombre del partido y dos
enteros, y un partido puede ser ingresado muchas veces).
La carga finalizara cuando el data-entry presione enter cuando se le pida el nombre de un partido.

Escribir una funcion que permita realizar la carga, y su valor de retorno sea el diccionario deseado."""

def armar_diccionario():
    diccionario = {}
    bandera = True
    while bandera:
        partido = str(input("Ingrese la partido (o presione ENTER para salir): ")).title()
        if partido == "":
            bandera = False
        else:
            validos = int(input("Ingrese el numero de votos validos del partido {} : ".format(partido)))
            invalidos = int(input("Ingrese el numero de votos invalidos del partido {} : ".format(partido)))
            if partido in diccionario:
                diccionario[partido]["validos"] += validos
                diccionario[partido]["invalidos"] += invalidos
            else:
                diccionario[partido] = {"validos":validos,"invalidos":invalidos}
    return diccionario

"""
Segunda parte:

En esta seccion buscaremos obtener algunas estadisticas a partir del diccionario cargado en la primera parte.
Se deben aplicar los criterios de modularizacion vistos en clases. Se pide calcular:

- Cual es partido ganador de las elecciones (es decir, el que sume mayor cantidad de votos validos)."""

def partido_ganador(diccionario):
    partidoganador = ""
    votosganador = -1
    for partido in diccionario:
        if diccionario[partido]["validos"] > votosganador:
            partidoganador = partido
            votosganador = diccionario[partido]["validos"]
    return partidoganador,votosganador

"""
Tercera parte:

Cuales son los partidos que pasaron estas elecciones PASO (es decir, aquellos que sacaron una cantidad mayor a
un 10% respecto dle total de votos ingresados considerando unicamente los votos validos)"""

def total_votos(diccionario):
    votos = 0
    for partido in diccionario:
        votos += diccionario[partido]["validos"]
    return votos

def porcentaje_partidos(diccionario,votostotales):
    #votostotales = total_votos(diccionario)
    clasificados = []
    for partido in diccionario:
        if (diccionario[partido]["validos"] / votostotales) > 0.1:
            clasificados.append(partido)
    
    return clasificados
    
"""
Cuarta parte:
Imprimir un ranking que indique cuales son los partidos que mayor cantidad de votos invalidos recibieron
Este ranking debe estar impreso en forma descendente (es decir, los de mayor cantidad de votos invalidos primero"""

def ranking_votos(diccionario):
    ranking = sorted(diccionario.items(),key = lambda tupla_votos: tupla_votos[1]["invalidos"], reverse = True)
    return ranking

"""
Quinta parte:

Cual es el porcentaje de votos invalidos respecto al total de votos (se entiende, al total de votos por la
suma entre """

def main():
    diccionario = armar_diccionario()#Punto1
    partido,votos = partido_ganador(diccionario)#Punto2
    clasificados = porcentaje_partidos(diccionario,votos)#Punto3
    ranking = ranking_votos(diccionario)#Punto 4

main()