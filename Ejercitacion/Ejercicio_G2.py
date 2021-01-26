# Ejercicio 1
# numero = float(input("Ingrese un numero real: "))
# if numero > 0:
#     print("El numero ingresado es mayor a 0")
# elif numero < 0:
#     print("El numero ingresado es menor a 0")
# else: #numero = 0
#     print("El numero es 0")
#---------------------------------------------------------------#
# Ejercicio 2
# num1 = float(input("Ingrese un numero real: "))
# num2 = float(input("Ingrese otro numero real: "))
# if (num1 > num2):
#     print("El numero mas grande es: ", num1)
# else: #(num1 < num2)
#     print("El numero mas grande es: ", num2)
#---------------------------------------------------------------#
# Ejercicio 3
# D = int(input("Ingrese el valor de la distancia recorrida en km: "))
# T = int(input("Ingrese el valor del tiempo: "))
# velocidad = D / T
# print("La velocidad promedio es: ", velocidad)
#----------------------------------------------------------------------#
# Ejercicio 4
# def es_par(numero):
#     #Pre: la funcion es_par determina si el numero ingresado es par
#     #Post: devuelve si es par o no
#     return "Es par" if numero % 2 == 0 else "Es impar"
# #-------------------------- Bloque Principal ------------------------------#
# # print(es_par(5))
# #-------------------------------------------------------------------#
# # Ejercicio 5
# numero = int(input("Ingrese un numero: "))
# print(es_par(numero))
#-----------------------------------------------------------#
# Ejercicio 6
# def divisible(num1, num2):
#     #Pre: la funcion divisible verifica que dos numeros sean divisibles
#     #Post: indica si dos numeros son divisibles o no
#     return "Es divisible" if num1 % num2 == 0 else "No es divisible"
# #------------------------ Bloque Principal -------------------------------#
# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))
# print(divisible(num1, num2))
#--------------------------------------------------------------------#
# Ejercicio 7    
# def suma(num1, num2):
#     #Pre: la funcion suma calcula la suma entre el primer numero y el segundo
#     #Post: devuelve la suma entre el primer numero y el segundo
#     return num1 + num2
# 
# def resta(num1, num2):
#     #Pre: la funcion resta calcula la diferencia entre el primer numero y el segundo
#     #Post: devuelve la suma entre el primer numero menos el segundo
#     return suma(num1, -num2)
# 
# def multiplicacion(num1, num2):
#     #Pre: la funcion multiplicacion calcula el producto entre el primer numero y el segundo
#     #Post: devuelve el producto entre el primer numero y el segundo
#     return num1 * num2
# 
# def division(num1, num2):
#     #Pre: la funcion division_decimal calcula el cociente entre el primer numero y el segundo, suponiendo que este es distinto de 0
#     #Post: devuelve la division con decimal entre el primer numero y el segundo
#     return num1 / num2
# #----------------------------------- Bloque Principal -------------------------------#
# def main():
#     num1 = int(input("Ingrese primer numero: "))
#     num2 = int(input("Ingrese otro numero: ")) 
#     
#     print("La suma es: ", suma(num1, num2))
# # print("La suma es: ", suma(num1, num2))
# # print("La diferencia es: ", resta(num1, num2))
# # print("El producto es: ", multiplicacion(num1, num2))
# # print("La division es: ", division(num1, num2))
#     
# main()
#--------------------------------------------------------------------------------------#
# Ejercicio 8
def main():
    print("Opcion 1")
    print()
    print("Opcion 2")
    print()
    print("Opcion 3")
    print()
    print("Opcion 4")
    print()
    print("Opcion 5, terminar")
    print("-----------------------------")
    
    opcion = int(input("Ingrese una opcion: "))
    
    while opcion != 5:
        
        if opcion == 1:
            print("Elegiste la primera opcion")
        
        elif opcion == 2:
            print("Elegiste la segunda opcion")
        
        elif opcion == 3:
            print("Elegiste la tercera opcion")
        
        else: #opcion == 4
            print("Elegiste la cuarta opcion")
        
        opcion = int(input("Ingrese una opcion, con ENTER sale: "))

main()
#------------------------------------------------------------------------------#
# Ejercicio 9
# T = int(input("Ingrese periodo en segundos: "))
# T_minutos = T / 60
# print("El periodo en minutos es: ", T_minutos)
# T_horas = T_minutos / 60
# print("El periodo en horas es: ", T_horas)
# T_dias = T_horas / 24
# print("El periodo en dias es: ", T_dias)
#--------------------------------------------------------#
# Ejercicio 10
# x = 3
# if (x < 5):
#     x += 1
# if (x == 5):
#     x += 2
# if (x > 5):
#     x += 3
# if (x > 5):
#     x += 1
# elif (x == 5):
#     x += 2
# else:
#     x += 3
# print(x)
