""" Ejercicio 2
    Solicite al usuario el ingreso de un texto.
    Considerar que el usuario solo ingresa palabras separadas por blancos,
    sin ningún otro tipo de caracteres. De las palabras ingresadas,
    descartar las que tienen tres letras o menos y las que tienen 10 letras
    o más, además de las repetidas.
    Luego, mostrar una lista de las palabras que quedaron ordenadas,
    en primer lugar por cantidad de letras (de menor a mayor) y,
    a igual cantidad de letras, alfabéticamente.
    """
##  ingresa palabras y devuelve una lista de esas palabras
def ingresarTexto():
    texto = input("Ingrese un texto con palabras separadas por blancos: ")
    return texto.split()

##  verifica si la clave largo esta en el diccionario
##  en caso de estar, verifica si la palabra no esta y la agrega
##  si el largo no esta, agrega la clave con una lista que contiene la palabra
def verificar(dic, palabra, largo):
    if (largo in dic):
        if (palabra not in dic[largo]):
            dic[largo] = [palabra]
    else:
        dic[largo] = [palabra]
   
##  toma la lista con las palabras y arma un diccionario donde la clave
##  es la cantidad de letras y tiene una lista con las palabras 
def palabrasSeleccionadas(lista):
    palabras = {}
    for palabra in lista:
        largo = len(palabra)
        if (3 < largo < 10):
            verificar(palabras, palabra, largo)
    return palabras

##  ordena cada lista de palabras del diccionario y arma una sola
def listaOrdenada(dic):
    listaFinal = []
    longitudOrdenada = sorted(dic)
    for largo in longitudOrdenada:
        listaFinal.extend(sorted(dic[largo]))
    return listaFinal

##  principal del ejercicio 2
def main2():
    listaOriginal = ingresarTexto()
    diccionarioPalabras = palabrasSeleccionadas(listaOriginal)
    listaFinal = listaOrdenada(diccionarioPalabras)
    print(listaFinal)