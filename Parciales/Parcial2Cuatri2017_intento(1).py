"""-----EJERCICIO1------
1) Escribir una función que, dado un texto que se pasa por parámetro, lo imprima al revés y sin ninguna
vocal. Las vocales pueden estar en minúsculas o mayúsculas."""

def validar_clave(clave):
    nueva_clave = []
    i = 0
    for i in range(len(clave)):
        if not clave[i] in "AEIOUaeiou":
            nueva_clave.append(clave[i])
    nueva_clave.reverse()
    nueva_clave = "".join(nuevaclave)
    print(nueva_clave)
    return nuevaclave

clave = str(input("Ingrese la clave: "))
print(validar_clave(clave))


"""-----EJERCICIO2-----
2) Solicite al usuario el ingreso de un texto.  El mismo debe contener al menos 100 palabras, de lo contrario deberá exigir al usuario que ingrese más
palabras, y adicionarlas a las ya ingresadas hasta superar el mínimo establecido. Considere que el usuario solo ingresa palabras separadas por blancos, sin
ningún otro tipo de caracteres. Muestre una lista de las palabras ingresadas, ordenada alfabéticamente, sin repetir palabras. """

def palabra_enlista (ingreso,lista):
    separado = ingreso.split()
    for elemento in separado:
        if elemento not in lista:
            lista.append(elemento)
    
    return sorted(lista)

def validar_texto():
    lista = []
    while len(lista)<100:
        ingreso = str(input("Ingrese un texto con un minimo de 100 palabras: "))
        nuevalista = palabra_enlista(ingreso,lista)
        lista = nuevalista
    print(lista)
    return lista


#validar_texto()

"""-----EJERCICIO3------
3) Ingresar en un diccionario  pares de datos con una clave que será un nombre de Partido Político y valor que será la cantidad de votos obtenidos en una provincia, una
misma clave se puede ingresar varias veces. Se pide: 
a) Calcular el total de votos para cada partido e imprimirlo.
b) Imprimir el listado anterior ordenado de mayor a menor por cantidad de votos.

    • Escriba en letra clara y de forma prolija, puede utilizar lápiz
    • Desarrolle el código en Python en forma estructurada aplicando funciones """


def ingresar_datos():
    dicc = {}
    bandera = True
    
    while bandera:
        partido = str(input("Ingrese el nombre del partido politico: "))
        if partido == "":
            bandera = False
        else:
            votos = int(input("Ingrese la cantidad de votos obtenidos en Buenos Aires: "))
            if partido in dicc:
                dicc[partido] += votos
            else:
                dicc[partido] = votos
    return dicc

def ordenar_votos(dicc):
    ordenado = sorted(dicc.items(),key = lambda dicc_val: dicc_val[0] ,reverse = True)
    return ordenado 
        

def main():
    diccionario = ingresar_datos()
    dicc_ordenado = ordenar_votos(diccionario)
    print(dicc_ordenado)
    return None
    
#main()    



