"""
// Va con un diccionario cargado - importar el modulo corredores

El diccionario runners tiene cargados a corredores desesperados por volver a correr. 

El nombre de cada corredor es la clave y se le asocia una lista de dos numeros:

el primero es la cantidad de kilometros que corrian a menudo antes de la cuarentena (flotante),

el segundo es el tiempo que tardaba en hacerlo (entero dado en minutos).


Se pide que hagas un programa en Python que:

Indique el promedio de kilometros corridos por todos los corredores.
Liste los corredores ordenados de mayor a menor por velocidad promedio.
Indicando:

corredor - velocidad (km / min) """

#import corredores
runners= {}
runners["Pablo"] = [1.5, 120]
runners["Rosa"] = [3, 20]
runners["Andy"] = [0.2, 160]
runners["Micaela"] = [3.1, 33]
runners["Uriel"] = [16, 50]
runners["Camila"] = [8, 40]
runners["Juan"] = [20, 85]

def promedio(runners):
    km_promedio = {}
    
    for corredores in runners:
        km_promedio[corredores] = (runners[corredores][0] / runners[corredores][1]) * 100

    return km_promedio

def ordenar(km_promedio):
    ordenado = sorted(km_promedio.items(), key = lambda x : x[1], reverse = True)
    return ordenado

#----------------------- Bloque Principal ----------------------#
def main():
    diccionario = promedio(runners)
    diccionario_ordenado = ordenar(diccionario)
    for corredores in diccionario_ordenado:
        print(corredores[0], corredores[1], "%")
main()