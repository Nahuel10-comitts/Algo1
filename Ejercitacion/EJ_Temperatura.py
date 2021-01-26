"""Escribir un programa modular en Python, que permita porcesar un conjunto de datos
meteorologicos de un grupo de ciudades de ciudadez, y brinde informacion al respecto.
El programa debera invocar al modulo cargar_datos(mes, año), que pertenece a la biblioteca 
datos.py. Dicho modulo devolvera un diccionario con los datos a procesar; que contendra para
cada nombre de cuidad (clave del diccionario), una lista de ternas de valores, que se
corresponden con: dia temperatura minima y temperatura maxima. La lista asociada a cada
nombre de ciudad, tendra tantas ternas como dias tiene le mes por parametro.
Ejemplo:
{"San Isidro" : [[1, 7, 15], [2, 10, 16], [3, 6, 12],........, [29, 7, 12], [30, 8, 12]]
"Dolores" : [[1, 6, 13], [2, 9, 11],[3, 4, 8],..............,[29, 5, 10], [30, 6, 12]]
"Mar del Plata" : [[1, 4, 9], [2, 8, 13], [3, 6, 11],................,[29, 6, 10],[30, 7, 12]]}
El programa debera brindar la siguiente informacion:
1. Cual fue la temperatura maxima y minima promedio durante el mes. para cada ciudad, ordenado
por el nombre de la ciudad.
2. Cuales ciudades tuvieron la menor temperatura maxima del mes.
3. Cual fue la temperatura minima promedio de todas las ciudades, el ultimo dia del mes.
4. Cual fue la maxima amplitud termica diaria, para cada ciudad, y que dias ocurrio.
Ordenado por amplitud termica (diferencia entre la temperatura maxima y la minima)
5. Permitir el ingreso de nombres de un a ciudad, hasta que se ingrese uno en blanco.
Por cada ingreso, mostrar los datos asociados a la ciudad o mensaje "Ciudad Inexistente"""

# Hay 2 alternativas para resolver este ejercicio. La otra es hacer las listas por compresion.

# Punto 1
def calcular_temperatura_promedio(diccionario_datos):
    temperatura_promedio = []
    for clave in diccionario_datos:
        temperatura_minima = 0
        temperatura_maxima = 0
        for dias in diccionario_datos[clave]:
            temperatura_minima += dias[1]
            temperatura_maxima += dias[2]
        temperatura_promedio.apendd([clave, round(temperatura_minima / len(dias), 1), round(temperatura_maxima) / len(dias), 1])   
    
    temperatura_promedio.sort()
    return temperatura_promedio
#----------------------------------------- Punto 2 ---------------------------------------------------------------------------------------------#
def mininmo_temperatura_maxima_mes(diccionario_datos):
    minimo_maximo = min([dias[2] for clave in diccionario_datos for dias in diccionario_datos[dias]])
    return minimo_maximo

def ciudades_con_minimo_maximo(diccionario_datos, minimo_maximo):
    ciudades = []
    for ciudades in diccionario_datos:
        l = []
        for dia in diccionario_datos[ciudad]:
            l.append(dias[2])
            if minimo_maximo in l:
                ciudades.append(ciudad)
    return ciudades
#--------------------------------------------- Punto 3 --------------------------------------------------------------------------------------------#
def temperatura_minima_promedio(diccionario_datos):
    promedio_temperatura_minima = 0
    for ciudad in diccionario_datos:
        promedio_temperatura_minima += diccionario_datos[-1][1]
    return promedio_temperatura / len(diccionario_datos)
#----------------------------------------------- Punto 4 -------------------------------------------------------------------------------------------#
def mayor_amplitud(diccionario_datos):
    l = []
    for clave in diccionario_datos:
        dias = []
        max_at = diccionario_datos[clave][0][2] - diccionario_datos[clave][0][1]
        for dias in diccionario_datos[clave]:
            if (dias[2] - dias[1]) > max_at:
                max_at = dias[2] - dias[1]
            elif (dias[2] - dias[1]) == max_at:
                dias.append(dias[0])
        l.append([clave, max_at, dias])
        dias.sort(key = lambda x : x[1])
    return l
#------------------------------------------------------- Punto 5 ---------------------------------------------------------------------------------------#
def mostrar_datos_ciudad(diccionario_datos):
    print("Datos de la ciudad")
    ciudad = input("Ingresar nombre de la ciudad: ")
    while ciudad != "":
        if ciudad in diccionario_datos:
            print("Ciudad: ", ciudad)
            print("/tdias, /tTemp Min, /tTemp Max")
            for dias in diccionario_datos[ciudad]:
                print("/t:(0, 3d) /t:(0, 5d) /t/t(0, 5d)".format(dias[0], dias[1], dias[2]))
        else:
            print("Ciudad inexistente")
            ciudad = input("Ingresar nombre de la ciudad: ")
    return ciudad
#------------------------------------------------------ Bloque Principal ------------------------------------------------------------------------------------------#
import datos
diccionario_temperartura = datos.cargar_datos(10, 2018)
# Punto 1
temperatura_promedio_por_ciudad = calcular_temperatura_promedio(diccionario_temperatura)
for ciudad in temperatura_promedio_por_ciudad:
    print(ciudad[0].ljust(20), ciudad[1], ciudad[2], sep="\t ")
# Punto 2
temperatura_minima_maxima = minima_temperatura_maxima_mes(diccionario_tempertura)
print("\nMenor Temperatura Maxima del Mes: ", temperatura_minima_maxima)
print("Ciudades: ", ciudades_con_minimo_maximo(diccionario_temperatura, temperatura_minima_maxima))
# Punto 3
print("\nTemperatura minima promedio el ultimo dia del mes: ",temperatura_minima_promedio(diccionario_temperatura))
# Punto 4
print("\nMayor Amplitud Termica por Ciudad")
la_amplitud_termica = mayor_amplitud(diccionario_temperatura)
for ciudad in la_amplitud_termica:
    print("Ciudad: {0:20} Amplitud: {1:2d} Dias: {2}".format(ciudad[0], ciudad[1],
ciudad[2]))
# Punto 5
mostrar_datos_ciudad(diccionario_temperatura)         
          