"""3) Ingresar en un diccionario pares de datos con una clave que será un nombre de Partido Político y valor que será la cantidad de votos obtenidos en una provincia, 
una misma clave se puede ingresar varias veces. Se pide: 
a) Calcular el total de votos para cada partido e imprimirlo.
b) Imprimir el listado anterior ordenado de mayor a menor por cantidad de votos."""
def agregar_diccionario(partido_politico, cant_votos, diccionario):
    if partido_politico in diccionario:
        diccionario[partido_politico][0] += cant_votos
    
    else:
        diccionario[partido_politico] = [cant_votos]
    
    return diccionario

def carga_diccionario():
    diccionario = {}
    partido_politico = input("Ingrese el nombre del partido politico, o escriba X para salir: ")
    
    while partido_politico != "X":
        cant_votos = int(input("Ingrese la cantidad de votos: "))
        agregar_diccionario(partido_politico, cant_votos, diccionario)
        
        partido_politico = input("Ingrese el nombre del partido politico, o escriba X para salir: ")
    
    return diccionario

def imprimir(diccionario):
    lista = sorted(diccionario.items(), key = lambda x: x[1], reverse = True)
    for partido_politico in lista:
        print("Para el partido politico: ", partido_politico[0], ", la cantidad de votos es: ", partido_politico[1])
        
    return

def main():
    diccionario = carga_diccionario()
    imprimir(diccionario)

main()

