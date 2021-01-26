#-------------------------------------------------------------------------------------------------------------------------------------------
'''Elecciones PASO

Primera parte:

Se cargan datos en un diccionario en forma manual. Estos datos consisten en el nombre de un partido politico,
la cantidad de votos validos, y la cantidad de votos invalidos que obtuvo en alguna localidad de nuestro
país (no se ingresa la localidad, solo se ingresa el nombre del partido y dos enteros, y un partido puede ser
ingresado muchas veces).
La carga finalizara cuando el data-entry presione enter cuando se le pida el nombre de un partido.

Escribir una funcion que permita realizar la carga, y su valor de retorno sea el diccionario deseado.

- Cual es partido ganador de las elecciones (es decir, el que sume mayor cantidad de votos validos).

- Cuales son los partidos que pasaron estas elecciones PASO (es decir, aquellos que sacaron una cantidad mayor
a un 10% respecto del total de votos ingresados considerando unicamente los votos validos).'''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def cargar_datos_paso():
    partido={}
    nombre_patido =input('partido politico: ')
    while(nombre_patido == ""):
        validos=input('votos validos: ')
        invalidos=input('votos invalidos: ')
        if not nombre_patido in partido:
            partido[nombre_patido]={'validos':validos,'invalidos':invalidos}
        else:
            partido[nombre_patido]['validos']+=validos
            partido[nombre_patido]['invalidos']+=invalidos
        nombre_patido=input('partido politico: ')
    return partido

def partido_ganador(partidos):
    key = list(partidos.keys())[0]
    for nombre in partidos:
        if(partidos[nombre]['validos']>partidos[key]['validos']):
            ganador = nombre
            puntos=partidos[nombre]['validos']
    return ganador,puntos

def partidos_diez(partidos):
    suma_total_puntos = 0
    for nombre in partidos:
        suma_total_puntos += partidos[nombre]['validos']
    diez_prociento=suma_total_puntos*0.1
    return diez_prociento

def clasificados(partidos):
    ganadores = []
    for nombre in partidos:
        if partidos[nombre]['validos']>partidos_diez(partidos):
            ganadores.append(nombre)
    return ganadores



