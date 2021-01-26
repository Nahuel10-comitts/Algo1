"""3) Ingresar en un diccionario localidades (clave) y dos datos: cantidad de habitantes – cantidad de centros asistenciales de salud (CAS). Los datos surgen de distintas planillas, 
por lo que una misma clave (localidad) se puede ingresar varias veces, debiendo sumarse los valores. Se pide: 
a) Listar el total de habitantes y CAS para cada localidad.
b) Imprimir un listado ordenado de mayor a menor de las 5 localidades de mayor relación habitantes / CAS. Indicando: localidad – relación."""

def agregar_diccionario(localidad, cant_habitantes, cant_CAS, diccionario):
    if not localidad in diccionario: #Si no esta en el diccionario los agrega como una diccionario
        diccionario[localidad] = {"Habitantes": cant_habitantes, "CAS": cant_CAS}

    else: #localidad in diccionario: #Si ya estan los suman con los valores que estaban antes
        diccionario[localidad]["Habitantes"] += cant_habitantes
        diccionario[localidad]["CAS"] += cant_CAS

    return diccionario #Devuelve el diccionario con los datos cargados

def carga_datos_diccionario():
    diccionario = {} #Inicializo un diccionario vacio donde despues voy a agregar los datos de los habitantes y CAS por localidad
    localidad = input("Ingrese la localidad: ") #Pido por pantalla el ingreso de la localidad
    
    while localidad: #Mientras se siga ingresando localidades entra al ciclo
        cant_habitantes = int(input("Ingrese los habitantes: ")) #Pido por pantalla el ingreso de los habitantes y los casteo a entero
        cant_CAS = int(input("Ingrese los Centros Asistenciales de Salud (CAS): ")) #Pido por pantalla el ingreso de los CAS por pantalla y lo casteo a entero
        
        agregar_diccionario(localidad, cant_habitantes, cant_CAS, diccionario) #Llamada a una funcion que agrega los datos al diccionario

        localidad = input("Ingrese la localidad: ") #Vuelve a pedir el ingreso de la localidad al usuario
    
    return diccionario #Devuelve el diccionario con los datos ingresados

def imprimir(diccionario):
    ordenado = sorted(diccionario.items(), key = lambda localidad: localidad[1]["Habitantes"] / localidad[1]["CAS"], reverse = True) #Devuelve una lista del par clave-valor ordenado
    #por la relacion habitantes / CAS
    for elemento in ordenado[: 5]: #Por cada elemento en la lista "ordenado"
        print(ordenado[indice][0]," - ", ordenado[indice][1]["CAS"]) #Imprime por pantalla la localidad, los habitantes y el CAS.
        indice += 1

#----------------------------------------------- Bloque Principal -----------------------------------------------------------#
def main():
    diccionario = carga_datos_diccionario()
    imprimir(diccionario)
main()
    
