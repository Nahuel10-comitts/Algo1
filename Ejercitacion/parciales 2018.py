"""1) Escribir una función que, dado un texto que se pasa por parámetro, devuelva el valor
booleano falso si antes de un punto o una coma hay un espacio,caso contrario devuelve
verdadero. No se puede utilizar el método count."""
def validar_texto(texto):
    devolver = False
    if (" ," in texto) or (" ." in texto):
        devolver = False
    else:
        devolver = True
    return devolver
#----------------- Bloque principal -------------------#
txt = input("Ingresar texto: ")
print(validar_texto(txt))
#-------------------------------------------------------------------------#
""" 2) Solicite al usuario el ingreso de un texto. Considerar que el usuario
solo ingresa palabras separadas por blancos, sin ningún otro tipo de caracteres.
De las palabras ingresadas, descartar las que tienen tres letras o menos y las que tienen
10 letras o más, además de las repetidas. Luego, mostrar una lista de las palabras que
quedaron ordenadas, en primer lugar por cantidad de letras (de menor a mayor) y, a igual
cantidad de letras, alfabéticamente. """
# Ingresa palabras y devuelve una lista de ellas.
def ingresar_texto():
    texto = input("Ingresar el texto separada en blanco: ")
    return texto.split()
# Verifica si la clave largo esta en el diccionario, en caso de estar, verfica
# si la palabra no esta y la agrega. Si largo no esta, agrega la clave con una lista
# que contiene la palabra.
def verificar(diccionario, palabra, largo):
    if largo in diccionario:
        if palabra not in diccionario[largo]:
            diccionario[largo].append(palabra)
    else:
        diccionario[largo] = [palabra]
# Toma la lista que contiene las palabras y crea un diccionario donde la clave son las
# letras y tiene una lista con las palabras.
def palabars_seleccionadas(lista):
    palabras: {}
    for palabra in lista:
        largo = len(palabra)
        if (3 < largo < 10):
            verificar(palabras, palabra, largo)
    return palabras
# Ordena cada lista del diccionario y crea una sola.
def lista_ordenada(diccionario):
    lista_final = []
    longitud_ordenada = sorted(diccionario)
    for largo in logitud_ordenada:
        longitud_ordenada.extend(sorted(diccionario[largo]))
    return lista_final
# Llamado a las funciones
def main():
    lista_original = ingresar_texto()
    diccionario_palabra = palabras_seleccionadas(lista_original)
    lista_final = lista_ordenada(diccionario_palabras)
    print(lista_final)
#----------------------------------------------------------------------------------#
"""3) Ingresar en un diccionario localidades (clave) y dos datos: cantidad de personas
en edad laboral – cantidad de empleados. Los datos surgen de distintas planillas, por lo
que una misma clave (localidad) se puede ingresar varias veces, debiendo sumarse los
valores. Se pide: 
a) Calcular el total de personas en edad laboral y empleados para cada localidad e
imprimirlo.
b) Imprimir un listado ordenado de mayor a menor por porcentaje de desocupación.
Indicando: localidad - % de desocupación"""
# Carga y devuelve un diccionario de cantidad de personas en edad laboral - cantidad
# de empleados.
def cargar_diccionario():
    diccionario = {}
    localidad = input("Ingrese localidad, con X sale: ")
    while localidad != "X":
        habitantes = int(input("Ingrese la cantidad de personas en edad laboral: "))
        empleados = int(input("Ingrese la canitidad de personas empleadas: "))
        agregar_diccionario(localidad, habitantes, empleados, diccionario)
        localidad = input("Ingrese localidad, con X sale: ")
    return diccionario
# Verifica si una localidad ya esta en el diccionario o no
# si esta suma los valores, si no los agrega.
def agregar_diccionario(localidad, habitantes, empleados, diccionario):
    if localidad in diccionario:
        diccionario[0] += habitantes
        diccionario[1] += empleados
    else:
        diccionario[localidad] = [habitantes, empleados]
        
# Imprime el diccionario.
def imprimir():
    print("Para la localidad: ", localidad)
    print("Las personas en edad laboral son: ", diccionario[localidad][0])
    print("Los empleados son: ", diccionario[localidad][1])
# Calcula el porcentaje de desocupacion para cada localidad
# devuelve un nuevo diccionario.    
def porcentaje_desocupacion(diccionario):
    desocupacion = {}
    habitantes = diccionario[localidad][0]
    desocupados = diccionario[localidad][0] - diccionario[localidad][1]
    desocupacion[localidad] = (100 * desocupados) / habitantes
    return desocupacion
# Ordena por porcentaje de desocupacion de mayor a menor
# imprime la lista.
def punto(diccionario):
    lista = sorted(diccionario.items(), key = lambda x:x[1], reverse = True)
    print("Porcentaje de desocupacion por localidad")
    for localidad in lista:
        print("Localidad: ",localidad[0], " - desocupacion",  localidad[1], "%")
# Main
def main():
    diccionario = cargar_diccionario()
    imprimir(diccionario)
    desocupacion = porcentaje_desocupacion(diccionario)
    punto(desocupacion)
    
    
    