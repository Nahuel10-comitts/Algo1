def agregar_diccionario(localidad, cant_habitantes, cant_centro_asistenciales_de_salud,diccionario):

    if not localidad in diccionario:  # Si no esta en el diccionario los agrega como una lista
        diccionario[localidad] = [cant_habitantes, cant_centro_asistenciales_de_salud]

    else:  # localidad in diccionario: #Si ya estan los suman con los valores que estaban antes
        diccionario[localidad][0]+= cant_habitantes
        diccionario[localidad][1]+= cant_centro_asistenciales_de_salud

    return diccionario

def imprimir_por_pantalla(diccionario):
    ordenamiento=sorted(diccionario.items(),key=lambda x:x[-1])
    ordenamiento.reverse()
    print('''Opciones para imprimir:
    opcion a:imprimir todo el listado
    opcion b:imprimir las 5 localidades con mayor poblacion''')
    respuesta=input("Que opcion elige a/b:").lower()
    n=0
    for clave in ordenamiento:
        if respuesta == "b" and n < 5:
            print(f"La localida {clave[0]} tiene {clave[1][0]} habitantes y {clave[1][1]} centro de asistencia de salud")
            n+=1
        elif respuesta=="a":
            print(f"La localida {clave[0]} tiene {clave[1][0]} habitantes y {clave[1][1]} centro de asistencia de salud")


def carga_datos_diccionario():
    n=True
    diccionario = {}  # Inicializo un diccionario vacio donde despues voy a agregar los datos de los habitantes y CAS por localidad
    while n:  # Mientras se siga ingresando localidades entra al ciclo
        consulta=input("Desea ingresar datos si/no:").lower()
        if consulta=="si":
            localidad = input("Ingrese la localidad: ").capitalize()  # Pido por pantalla el ingreso de la localidad
            cant_habitantes = int(input("Ingrese la cantidad de habitantes: "))  # Pido por pantalla el ingreso de los habitantes y los casteo a entero
            cant_centro_asistenciales_de_salud = int(input("Ingrese la cantidad de Centros Asistenciales de Salud (CAS): "))  # Pido por pantalla el ingreso CAS por pantalla y lo casteo a entero
            diccionario = agregar_diccionario(localidad, cant_habitantes, cant_centro_asistenciales_de_salud,diccionario) # Llamada a una funcion que agrega los datos al diccionario

        else:
            n=False


    imprimir_por_pantalla(diccionario)

carga_datos_diccionario()

