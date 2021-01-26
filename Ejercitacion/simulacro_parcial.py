'''Primera parte (este ejercicio consta de dos partes)

Una persona carga datos manualmente que deberán guardarse en un diccionario. Los datos consisten en un
nombre de una provincia (que será la clave del diccionario) y dos valores enteros que significan: cantidad
de infectados por el COVID y cantidad de fallecidos registrados en esa provincia.

Como los datos provienen de distintas localidades, el ingreso de los registros de una provincia, seguramente,
se hará en más de una oportunidad, debiéndose sumar los nuevos datos a los que ya estaban registrados. Este
proceso finaliza cuando ingrese una provincia vacía (presione enter).

Tu misión consistirá en escribir el código en Python para realizar esta carga.
Tratá de hacerlo bien modular porque este mismo ejercicio tiene una segunda parte.'''

def cargar_datos_covid():
    datos_covid = {}
    provincia = input("Ingrese provincia: ")
    while provincia != "":
        infectados = int(input("Ingrese infectados: "))
        fallecidos = int(input("Ingrese fallecidos: "))
        if provincia in datos_covid:
            datos_covid[provincia]["infectados"] += infectados
            datos_covid[provincia]["fallecidos"] += fallecidos
            
        else:
            datos_covid[provincia] = {"infectados": infectados, "fallecidos": fallecidos }
        
        provincia = input("Ingrese provincia: ")
    return datos_covid

'''
Segunda parte 

En base al diccionario que está cargado con la aplicación generada en el punto anterior, ahora se pide
escribir el código para:

- Indicar los casos totales de COVID y la cantidad total de fallecidos en el país.

- Del punto anterior se saca un índice de mortalidad: fallecidos / casos_totales. Listar las provincias que
estén por encima de esa relación.

- Listar las 5 provincias que mayor cantidad de casos detectados tiene, ordenado por cantidad de mayor a
menor, indicando: provincia - cantidad
'''

def estadisticas_totales(datos_covid):
    infectados = 0
    fallecidos = 0
    for provincia in datos_covid:
        infectados += datos_covid[provincia]["infectados"]
        fallecidos += datos_covid[provincia]["fallecidos"]
    
    return infectados, fallecidos

def provincias_con_alta_mortalidad(datos_covid, indice_de_mortalidad_general):
    provincias_mortales = []
    for provincia in datos_covid:
        indice_mortalidad_provincia = datos_covid[provincia]["fallecidos"] / datos_covid[provincia]["infectados"]
        if indice_mortalidad_provincia > indice_de_mortalidad_general:
            provincias_mortales.append(provincia)
    return provincias_mortales

def provincias_con_mas_casos(datos_covid):    
    ordenada_por_casos = sorted(datos_covid.items(), key = lambda tupla: tupla[1]["infectados"], reverse=True)[:2]
    return ordenada_por_casos


datos_covid = cargar_datos_covid()

#Punto 1.
infectados, fallecidos = estadisticas_totales(datos_covid)
print("La cantidad total de infectados es: ", infectados)
print("La cantidad total de fallecidos es: ", fallecidos)

#Punto 2.
provincias_mortales = provincias_con_alta_mortalidad(datos_covid, fallecidos / infectados)
print("Las provincias con una tasa de mortalidad por encima de la promedio son: ")
for provincia in provincias_mortales:
    print(provincia)

#Punto 3.
provincias_mas_afectadas = provincias_con_mas_casos(datos_covid)
i = 1
for tupla_provincia in provincias_mas_afectadas:
    print("La provincia numero {} mas afectada es {}".format(tupla_provincia[0], tupla_provincia[1]["infectados"]))
    i+=1