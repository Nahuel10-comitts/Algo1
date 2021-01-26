"""3) Ingresar en un diccionario localidades (clave) y dos datos: cantidad de personas en edad laboral – cantidad de empleados. Los datos surgen de distintas planillas, 
por lo que una misma clave (localidad) se puede ingresar varias veces, debiendo sumarse los valores. Se pide: 
a) Calcular el total de personas en edad laboral y empleados para cada localidad e imprimirlo.
b) Imprimir un listado ordenado de mayor a menor por porcentaje de desocupación. Indicando: localidad - % de desocupación"""

def agregar_diccionario(localidad, cant_personas_edad_laboral, cant_empleados, diccionario):
    if localidad in diccionario:
        diccionario[localidad][0] += cant_personas_edad_laboral
        diccionario[localidad][1] += cant_empleados
    else:
        diccionario[localidad] = [cant_personas_edad_laboral, cant_empleados] 
    
    return

def diccionario_carga():
    diccionario = {}
    localidad = input("Ingrese localidad, o escriba X para salir: ")
    
    while localidad != "X":
        cant_personas_edad_laboral = int(input("Ingrese la cantidad de personas en edad laboral: "))
        cant_empleados = int(input("Ingrese la cantidad de empleados: "))
        
        agregar_diccionario(localidad, cant_personas_edad_laboral, cant_empleados, diccionario)
        
        localidad = input("Ingrese localidad, o escriba X para salir: ")
    
    return diccionario

def imprimir(diccionario):
    for localidad in diccionario:
        print("Para la localidad: ", localidad)
        print("La cantidad de personas en edad laboral: ", diccionario[localidad][0])
        print("La cantidad de empleados: ", diccionario[localidad][1])

    return

def porcentaje_desocupacion(diccionario):
    desocupacion = {}
    for localidad in diccionario:
        habitantes = diccionario[localidad][0]
        desocupados = diccionario[localidad][0] - diccionario[localidad][1]
        desocupacion[localidad] = (100 * desocupados) / habitantes

    return desocupacion

def ordenar_imprimir(diccionario):
    lista = sorted(diccionario.items(), key = lambda x: x[1], reverse = True)
    print("Porcentaje de desocupacion por localidad")
    for localidad in lista:
        print("Localidad: ", localidad[0], " -desocupacion: ", localidad[1])
    
    return

def main():
    diccionario = diccionario_carga()
    imprimir(diccionario)
    desocupacion = porcentaje_desocupacion(diccionario)
    ordenar_imprimir(desocupacion)

main()

