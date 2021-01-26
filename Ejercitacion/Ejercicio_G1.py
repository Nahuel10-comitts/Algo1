#Ejercicio 1:
# numero = input("Ingrese numero: ")
# print("Numero ingresado: ", numero)
#-----------------------------------------------#
#Ejercicio 2:

# def suma(num1, num2):
#     #Pre: la funcion suma calcula la suma entre el primer numero y el segundo
#     #Post: devuelve la suma entre el primer numero y el segundo
#     return num1 + num2

# def resta(num1, num2):
#     #Pre: la funcion resta calcula la diferencia entre el primer numero y el segundo
#     #Post: devuelve la suma entre el primer numero menos el segundo
#     return suma(num1, -num2)

# def multiplicacion(num1, num2):
#     #Pre: la funcion multiplicacion calcula el producto entre el primer numero y el segundo
#     #Post: devuelve el producto entre el primer numero y el segundo
#     return num1 * num2

# def division_entera(num1, num2):
#     #Pre: la funcion division_entera calcula el cociente entre el primer numero y el segundo, suponiendo que este es distinto de 0
#     #Post: devuelve la division entre entre el primer numero y el segundo
#     return num1 // num2

# def division_decimal(num1, num2):
#     #Pre: la funcion division_decimal calcula el cociente entre el primer numero y el segundo, suponiendo que este es distinto de 0
#     #Post: devuelve la division con decimal entre el primer numero y el segundo
#     return num1 / num2
# #------------------------------------- Bloque Principal -----------------------------------------#
# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero: "))
# print("La suma es: ", suma(num1, num2))
# print("La diferencia es: ", resta(num1, num2))
# print("El producto es: ", multiplicacion(num1, num2))
# print("La division entera es: ", division_entera(num1, num2))
# print("La division con decimal es: ", division_decimal(num1, num2))
#---------------------------------------------------------------------------------------------------------------------------------------#
#Ejercicio 3
# nombre = input("Ingrese su nombre: ")
# print("Hola", nombre, "bienvenido a mi programa")
#------------------------------------------------------------------------------------------------------------------------------------#
#Ejercicio 4
# pi = 3.14
# 
# def volumen_esfera(r):
#     #Pre: la funcion volumen_esfera cacula el volumen de la esfera
#     #Post: devuelve el valor del volumen de la esfera
#     return 4/3*pi*r**3
# 
# def superficie_esfera(r):
#     #Pre: la funcion superficie_esfera calcula la superficie de la esfera
#     #Post: devuelve la superficie de la esfera
#     return 4*pi*r**2
# 
# #-------------------------------------------------------Bloque Principal ---------------------------------------------------------------#
# r = int(input("Ingrese el radio de la esfera: "))
# print("El volumen de la esfera es: ", volumen_esfera(r))
# print("La superficie de la esfera es: ", superficie_esfera(r))
#----------------------------------------------------------------------------------------------------------------------#
#Ejercicio 5

# def superficie(b, h):
#     #Pre: la funcion superficie calcula la superficie del rectangulo
#     #Post: devuelve la superficie del rectangulo
#     return b * h
# 
# def perimetro(b, h):
#     #Pre: la funcion perimetro calcula el perimetro del rectangulo
#     #Post: devuelve el perimetro del rectangulo
#     return 2 * superficie(b, h)
# #-------------------------------------------------- Bloque Principal ---------------------------------------------------#
# b = int(input("Ingrese la base del rectangulo: "))
# h = int(input("Ingrese la altura del rectangulo: "))
# print("La superficie del rectangulo es: ", superficie(b, h))
# print("El perimetro del rectangulo es: ", perimetro(b, h))
#--------------------------------------------------------------------------------------------------------#
#Ejercicio 6
# A = input("Ingrese el primer numero: ")
# B = input("Ingrese el segundo numero: ")
# A = B
# print(A)
