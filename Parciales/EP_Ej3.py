""" Ejercicio 3
    Ingresar en un diccionario localidades (clave) y dos datos:
    cantidad de personas en edad laboral – cantidad de empleados.
    Los datos surgen de distintas planillas, por lo que una misma clave
    (localidad) se puede ingresar varias veces, debiendo sumarse los valores.
    Se pide: 
    a) Calcular el total de personas en edad laboral y empleados
    para cada localidad e imprimirlo.
    b) Imprimir un listado ordenado de mayor a menor por porcentaje
    de desocupación. Indicando: localidad - % de desocupación"""

# --------------------------------------------------------------------------------#

def cargar_diccionario():
    diccionario = {}
    localidad = input("Ingrese localidad, con X sale: ")
    while localidad != "X":
        habitantes = int(input("Ingrese el numero de habitantes: "))
        empleados = int(input("Ingrese el numero de empleados: "))
        agregar_en_diccionario(localidad,habitante,empleado,diccionario)
        localidad = input("Ingrese la localidad, con X sale: ")
        
# --------------------------------------------------------------------------------#

def agregar_en_diccionario(localidad,habitante,empleado,diccionario):
    if localidad in diccionario:
        diccionario[o] += habitante
        diccionario[1] += empleado
    else:
        diccionario[localidad] = [habitante, empleado]
        
# -----------------------------------------------------------------------------------#

def punto_A(diccionario):
    for localidad in diccionario:
        print("Para la localidad ", localidad)
        print("Las personas en edad laboral", diccionario[localidad][0])
        print("Empleados", diccionario[localidad][1])
        
# -----------------------------------------------------------------------------------------#

def porcentaje_desocupacion(diccionario):
    desocupacion = {}
    for localidad in diccionario:
        habitantes = diccionario[localidad][0]
        desocupados = diccionario[localidad][0] - diccionario[localidad][1]
        desocupados[localidad] = (100 * desocupados) / habitantes
    return desocupacion

# ------------------------------------------------------------------------------------------#

def punto_B(diccionario):
    lista = sorted(diccionario.items (), key = lambda x : x[1], reverse = True)
    print("El porcentaje de desocupacion por localidad es")
    for localidad in lista:
        print("Localidad:    ", localidad[0], "  - desocupacion:   "   , localidad[1] , "%")
        
# ------------------------------------------------------------------------------------------#

def main():
    diccionario = cargar_diccionario()
    punto_A(diccionario)
    desocupacion = porcentaje_desocupacion(diccionario)
    punto_B(diccionario)

