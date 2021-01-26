""" Problema:
Se pide que ingresen por teclado pares de Equipo-Puntos ganados, el mismo par se puede ingresar
varias veces. Se pide generar una Tabla de Puntos Acumulados para cada equipo, ordenando la tabla
por puntos en forma decreciente. """

def solicitar_valor(mensaje):
    valor = input(mensaje)
    return valor

#----------------------------------------------------------------------------------------------------#

def cargar_tabla():
    nombre = solicitar_valor("Cargar equipo: ")
    if nombre != "NO":
        puntos = int(solicitar_valor("Cargar puntos: "))
    tabla ={}
    while nombre!= "NO":
        if nombre not in tabla:
            tabla[nombre] = puntos
        else:
            tabla[nombre] += puntos
    nombre = solicitar_valor("Cargar equipo: ")
    if nombre != "NO":
        puntos = int(solicitar_valor("Cargar puntos: "))
    return tabla

# Existen dos maneras de ordenar una lista dentro de un diccionario #

def ordenar_lista1(t):
    lista_tabla = t.items()
    print(sorted(lista_tabla, key = lambda l : l[1], reverse = True))
    
# O #

# def ordenar_lista2(t):
#     import operator
#     tord = (sorted(t.items, key = operator.itemgetter(1), reverse = True))
#     print(tord)

#-----------------------------------------Main----------------------------------------------------#
    t = cargar_tabla
    ordenar_lista1(t)
#     ordenar_lista2(t)
# Depende de cual de las dos use para ordenar, nunca uses los dos al mismo tiempo.#

        