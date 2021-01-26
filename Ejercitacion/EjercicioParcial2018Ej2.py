"""2) Solicite al usuario el ingreso de un texto. Considerar que el usuario solo ingresa palabras separadas por blancos, sin ningún otro tipo 
de caracteres. De las palabras ingresadas, descartar las que tienen tres letras o menos y las que tienen 10 letras o más, además de las repetidas. 
Luego, mostrar una lista de las palabras que quedaron ordenadas, en primer lugar por cantidad de letras (de menor a mayor) y, a igual cantidad de letras, alfabéticamente."""
def ingresar_texto():
    texto = input("Ingrese texto separado por blancos: ")
    return texto.split()

def verificar(diccionario, palabra, largo):
    if largo in diccionario:
        if palabra not in diccionario[largo]:
            diccionario[largo] = palabra
    else:
        diccionario[largo] = palabra

def palabras_seleccionadas(lista):
    palabras = {}
    for palabra in lista:
        largo = len(palabra)
        if 3 < largo < 10:
           verificar(palabras, palabra, largo)
    
    return palabras

def ordenar_lista(diccionario):
    lista_ordenada = []
    diccionario_ordenado = sorted(diccionario)
    for largo in diccionario_ordenado:
        lista_ordenada.extend(sorted(diccionario[largo]))
    
    return lista_ordenada

def main():
    lista_original = ingresar_texto()
    diccionario_palabras = palabras_seleccionadas(lista_original)
    lista_final = ordenar_lista(diccionario_palabras)
    print(lista_final)

main()