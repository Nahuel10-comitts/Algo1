"""1) Escribir una función que, dado un texto que se pasa por parámetro, lo imprima al revés y sin ninguna vocal. Las vocales pueden estar en minúsculas o mayúsculas."""

def invertir(cadena):
    vocales = "aeiou"
    cadena = cadena.lower()
    
    for i in range(1,len(cadena)+ 1):
        if cadena[-i] not in vocales:
            print(cadena[-i])

def main():
    print(invertir("OTORRINOnaringolo"))
main()