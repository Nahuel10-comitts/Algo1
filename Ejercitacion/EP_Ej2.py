""" Ejercicio 2
    Solicite al usuario el ingreso de un texto.
    Considerar que el usuario solo ingresa palabras separadas por blancos, sin ningún
    otro tipo de caracteres. De las palabras ingresadas, descartar las que tienen tres
    letras o menos y las que tienen 10 letras
    o más, además de las repetidas.
    Luego, mostrar una lista de las palabras que quedaron ordenadas,
    en primer lugar por cantidad de letras (de menor a mayor) y,
    a igual cantidad de letras, alfabéticamente.
    """
# pido al usuario que ingrese un texto

def ingresar_texto():
    texto = input("Ingrese texto separados por espacios en blanco: ")
    return texto.split()

##  verifica si la clave largo esta en el diccionario
##  en caso de estar, verifica si la palabra no esta y la agrega
##  si el largo no esta, agrega la clave con una lista que contiene la palabra

def verificar(dic, largo, palabra):
    if largo in dic:
        if not palabra in dic[largo]:
            dic[largo].append()
        else:
            dic[largo] = [palabra]
            
##  toma la lista con las palabras y arma un diccionario donde la clave
##  es la cantidad de letras y tiene una lista con las palabras 

def seleccionar_palabra(lista):
    palabras = {}
    for palabra in lista:
        largo = len(palabra)
        if 3 < largo < 10:
            verificar(palabra, palabras, largo)
    return palabras

##  ordena cada lista de palabras del diccionario y arma una sola

def ordenar_lista(dic):
    lista_final = []
    lista_ordenada = lista.sorted(dic)
    for largo in lista_ordenada:
        lista_final.extend(sorted(dic[largo]))
    return lista_final

# programa principal

def main():
    lista_original = ingresar_texto()
    diccionario_palabras = palabras_seleccionadas(lista_original)
    lista_final = ordenar_lista(diccionario_palabras)
    print(lista_final)
    
            
