'''Primera parte:
Una persona carga datos manualmente que deberan guardarse en un dicionario. Los datos son el nombre
de una provincia, que sea la clave del diccionario, y dos valores enteros que significan: cantidad de
infectados por COVID y cantidad de fallecidos registrado en esa provincia.

Como los datos provienen de distintas localidad, el ingreso de los registrado de una provincia, quizas, se hara en mas de una oportunidad,
debiendose sumar lo nuevos datos a los que ya estaban registrados. Este proceso finaliza cuando ingrese una provincia vacia (enter)

Tu mision consistira en escribir un codigo python para realizar esta carga.
Trata de hacerlo modular porque el ejercicio tiene una segunda parte.

{
    'bs as': {
        'infectados':0,
        'fallecidos':0,
        },
    'cordoba':{
        'infectados':0,
        'fallecidos':0,
        }
}
'''

def cargar_datos_covid():
    covid = {}
    infectados = 0
    fallecidos = 0
    provincia = input('Ingrese la provincia: ')
    while provincia:
        infectados = int(input('Infectados: '))
        fallecidos = int(input('Fallecidos: '))
        if not provincia in covid:
            covid[provincia] = {'Infectados': infectados, 'Fallecidos':fallecidos}
#             covid[provincia]['Infectados'] = infectados
#             covid[provincia]['Fallecidos'] = fallecidos
        else:
            covid[provincia]['Infectados'] += infectados
            covid[provincia]['Fallecidos'] += fallecidos
        provincia = input('Ingrese la provincia: ')
    return covid

# print(cargar_datos_covid())

'''
Segunda parte

En base al diccionario que esta cargado con la aplicacion generada en el punto anterior, ahora se pide escribir el codigo para:

- indicar los casos totales de COVID y la cantidad total de fallecidos en el pais:
- del punto anterior se saca un indice de mortalidad: fallecidos / casos_totales. Listar las provincias que esten por encima de esa relacion
-listar las 5 provincias que mayor cantidad de casos detectados tiene, ordenado por cantidad de mayor a menor, indicando provincia - cantidad.

'''

def estadisticas_covid(covid):
    infectados_totales = 0
    fallecidos_totales = 0
    for provincia in covid:
        infectados_totales += covid[provincia]['Infectados']
        fallecidos_totales += covid[provincia]['Fallecidos']
    return infectados_totales, fallecidos_totales


# lista = [['bs as',100],['cordoba',70]]
# Se puede usar lista por compresion
def provincias_alta_mortalidad(covid,indice_mortalidad):
    provincias_alta_mortandad = []
    for provincia in covid:
        if covid[provincia]['Infectados'] / covid[provincia]['Fallecidos'] > indice_mortalidad:
            provincias_alta_mortandad.append(provincia)
    return provincias_alta_mortandad

def provincias_con_mas_casos(covid):
    ordenada_por_casos = sorted(covid.items(), key = lambda tupla: tupla[1]['Infectados'],reverse = True)
    return ordenada_por_casos


def main():
    
    covid = cargar_datos_covid()
    # Punto 1
    infectados, fallecidos = estadisticas_covid(covid)
    print('La cantidad total de infectados es: ',infectados)
    print('La cantidad total de fallecidos es: ',fallecidos)

    # Punto 2
    provincias_mortales = provincias_alta_mortalidad(covid, fallecidos / infectados)
    print ('Las provincias con tasa de mortalidad por encima de la promedio son: ')
    for provincia in provincias_mortales:
        print(provincia)

    # Punto 3
    provincias_mas_afectadas = provincias_con_mas_casos(covid)
    i = 1
    for tupla_provincia in provincias_mas_afectadas:
        print ('La provincia numero {} mas afectada es {} con {} casos'.format(i,tupla_provincia[0],tupla_provincia[1]['Infectados']))
        i += 1
        
main()
    

    
        
         
