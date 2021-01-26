"""Escribir un programa modular que solicite el ingreso de un valor, validando que el mismo este entre 0 y 20; y luego calcule e informe el factorial
del numero ingresado. Si el numero ingresado no cumple con lo solicitado, informar y pedir el reingreso del numero. Repetir la operacion hasta
que el numero sea valido."""

"""def leer_valor(minimo, maximo):
    
    valor = int(input("Calcular el factorial de: "))
    
    while valor < minimo or valor > maximo:
        print("Valor invalido. Reingrese valor entre {} y {}".format(0, 20))
        valor = int(input("Calcular el factorial de: "))
        
    return valor"""

def factorial(n):
    if n == 0:
        devolver = 1
    else:
        devolver = n * factorial(n - 1)
    return devolver

"""def main():
    
    x = leer_valor(0, 20)
    
    print("Resultado: ", factorial(x))

main()"""

x = int(input("Ingrese un valor para calcular su factorial: "))
print(factorial(x))
