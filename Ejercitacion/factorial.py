''' Solicitar el ingreso de un número, calcular su factorial y luego informarlo.
 Tener en cuenta que el factorial de un número N, entero positivo, es el
 producto de todos los números enteros positivos desde 1 hasta N; y que el
 factorial de 0, es 1.
 Si el usuario ingresa un valor menor a cero, se debe mostrar un mensaje que
 diga que no es factible calcular el factorial de dicho número.
'''
numero = int(input("Ingrese un numero: "))

if numero < 0:
    print("No es posible calcular el factorial al numero ingresado")
    
else: #Calcula el factorial del numero
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    print("El factorial del numero ingresado es: ", resultado)
    