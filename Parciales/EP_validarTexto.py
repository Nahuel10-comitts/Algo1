""" ejercicio 1
    Escribir una función que, dado un texto que se pasa por parámetro,
    devuelva el valor booleano falso si antes de un punto o una coma
    hay un espacio, caso contrario devuelve verdadero.
    No se puede utilizar el método count.
    """
def validar_texto(texto):
    if " ," in texto or " ." in texto:
        devolver = False
    else:
        devolver = True
    
    return devolver

enunciado = input("Ingrese texto: ")
print(validar_texto(enunciado))
    
        