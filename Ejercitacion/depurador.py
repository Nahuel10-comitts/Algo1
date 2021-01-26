""" Ejemplo de debuggin"""
# Escribir un programa que pida al usuario el ingreso de 2 numeros e imprima el producto usando sumas sucesivas.

def sumar(i, j):
    return i + j

def multiplicar(x, y):
    acum = 0
    
    for count in range(0, y):
        acum = sumar(acum, x)
    
    return acum

def main():
    a = int(input("Ingrese un numero A: "))
    b = int(input("Ingrese un numero B: "))
    print("El producto de A por B es: ", multiplicar(a, b))
    
main()