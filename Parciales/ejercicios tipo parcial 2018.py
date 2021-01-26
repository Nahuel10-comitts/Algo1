"""1) Escribir una función que, dado un texto que se pasa por parámetro, devuelva
el valor booleano falso si antes de un punto o una coma hay un espacio, caso contrario
devuelve verdadero. No se puede utilizar el método count."""
def validar_texto(texto):
    devolver = False
    if (" ." in texto) or (" ," in texto):
        devolver = False
    else:
        devolver = True
    return devolver
#---------------------- Bloque Principal ---------------------#
txt = input("Ingrese texto: ")
print(validar_texto(txt))
#---------------------------------------------------------------------------#
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
def imprimir():
    texto = input("Ingresar texto separados por blancos: ")
    return texto.split()
def verificar(diccionario, palabra, largo):
    diccionario = {}
    if largo in diccionario:
        if palabra not in diccionario[largo]:
            diccionario[largo] = palabra
    else:
        diccionario[largo] = palabra
    return diccionario
def palabras_seleccionadas(lista):
    palabras = {}
    for palabra in lista:
        largo = len(palabra)
        if 3 < largo < 10:
            verficar(palabras, palabra, largo)
    return palabras
        
# imprimir
# Texto = "Hola soy German"
# Texto.split() = ["Hola", "soy", "German"]
# palabras_seleccionadas
# len("Hola") = 4 len("soy") = 3 len("German") = 6
# "soy" no pasa y los demas van a la siguiente funcion
# 