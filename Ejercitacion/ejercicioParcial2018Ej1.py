"""1) Escribir una función que, dado un texto que se pasa por parámetro, devuelva el valor booleano falso si antes de un punto o una 
coma hay un espacio, caso contrario devuelve verdadero. No se puede utilizar el método count."""
def validar(cadena):
    devolver = True
    if " ," in cadena or " ." in cadena:
        devolver = False
    else:
        devolver = True
    
    return devolver

def main():
    cadena = input("Ingrese texto a validar: ")
    print(validar(cadena))

main()