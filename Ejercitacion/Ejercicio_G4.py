# Ejercicio 1
# def raices(a, b, c):
    #Pre: la funcion verifica que el discriminante sea mayor o igual a 0
    #Post: devuelve True si tiene raices reales o False si tiene raices imaginarias
#     devolver = False
#     discriminante = b**2 - 4 * a * c
#      
#     if discriminante >=0:
#         devolver = True
#     
#     else:
#         devolver = False
#        
#     return devolver
# #------------- Bloque Principal --------------#
# a = int(input("Ingrese el termino cuadratico: "))
# b = int(input("Ingrese el termino lineal: "))
# c = int(input("Ingrese el termino independiente: "))
# 
# print(raices(a, b, c))
#-------------------------------------------------------------------#
# Ejercicio 3
# import math

# def raices(a, b, c):
    
    #Pre: la funcion calcula las raices de un polinomio de 2 grado
    #Post: devuelve True si tiene raices reales y devuelve las raices, sino devuelve False, None y None
    
#     devolver = False
#     discriminante = b**2 - 4 * a * c
#     r1 = None
#     r2 = None
#     
#     if discriminante > 0:
#         devolver = True
#         r1 = (-b + math.sqrt(discriminante)) / (2 * a)
#         r2 = (-b - math.sqrt(discriminante)) / (2 * a)
#     
#     else:
#         devolver = False
#         
#     return devolver, r1, r2
        
#--------------- Bloque Principal --------------------#
# a = int(input("Ingrese el termino cuadratico: "))
# b = int(input("Ingrese el termino lineal: "))
# c = int(input("Ingrese el termino independiente: "))
# 
# print(raices(a, b, c))        
#--------------------------------------------------------------#
# Ejercicio 4         
# def es_primo(valor):
    #Pre: La funcion verifica que un numero sea primo o no
    #Post: devuelve True si es primo o False sino lo es
#     devolver = False
# 
#     if valor <= 1:
#         devolver = False
#     
#     else:
#         divisor = 2
#         while (((valor % divisor)!=0) and (divisor <= valor/2)):
#             divisor += 1
#         
#         if divisor > valor/2:
#             devolver = True
#         
#         else:
#             devolver = False
#             
#     return devolver
#---------- Bloque principal ---------------#
# valor = int(input("Ingrese un valor: "))
# print(es_primo(valor))
#-----------------------------------------------#
# Ejercicio 5
# def es_primo(valor):
#     #Pre: La funcion verifica que un numero sea primo o no
#     #Post: devuelve True si es primo o False sino lo es
#     devolver = False
#     primo = None
#     
#     if valor <= 1:
#         devolver = False
#      
#     else:
#         divisor = 2
#         while (((valor % divisor)!=0) and (divisor <= valor/2)):
#             divisor += 1
#          
#         if divisor > valor/2:
#             devolver = True
#             primo = 2, valor
#             
#         else:
#             devolver = False
#             primo = None
#              
#     return devolver, primo
# 
# #---------- Bloque principal ---------------#
# valor = int(input("Ingrese un valor: "))
# print(es_primo(valor))
#-------------------------------------------------------------------------------#
# Ejercicio 7
# def ordenados(numeros):
#     i = 0
#     while(i < len(numeros)):
#         if (numeros[i] > numeros[i + 1]):
#             devolver = "Está ordenado de forma descendente"
#     
#         elif (numeros < numeros[i + 1]):
#             devolver = "Están ordenados de forma ascendente"
#        
#         else:
#             devolver = "No están ordenados" 
#     
#     i += 1
#     
#     return devolver
# 
# #----------------- Bloque Principal ---------------------#
# numeros =  [3,2,1,0]
# print(ordenados(numeros))
#-----------------------------------------------------------------------#
# Ejercicio 10
#C = 5/9 * (F - 32)
# def tabla_temperaturas(temp_Celsius, temp_Fahrenheit):
    #Pre: la funcion recibe dos valores, el primero en grados Celsius y el segundo en Fahrenheit
    #Post: imprime una tabla de valores en un intervalo de 10
#     for temp_Fahr in range(temp_Celsius, temp_Fahrenheit + 1, 10):
#         print("La temperatura en Celsius es: ", 5/9 * (temp_Fahr - 32), ", La temperatura en Fahrenheit es: ", temp_Fahr)
#------------------------------------- Bloque Principal -------------------------------------------#
# def main():
#     tabla_temperaturas(0, 200)
#     
# main()
#-------------------------------------------------------------------#
# Ejercicio11
# def contador_letras(telegrama):
    #Pre: la funcion calcula la cantidad de letras de un telegrama
    #Post: devuelve la cantidad de letras
    
#     contador_letras = 0
#     abcedario = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
#     
#     for i in range(len(telegrama)):
#         if telegrama[i] in abcedario:
#             contador_letras += 1
#             
#     return contador_letras
# #--------------- Bloque Principal ------------------#
# def main():
#     cadena = "Hola, como estas"
#     print(contador_letras(cadena))
# 
# main()
#---------------------------------------------------------------------------------#
# Ejercicio 13
# def contador_vocales(cadena):
#     
#     vocal_a = 0
#     vocal_e = 0
#     vocal_i = 0
#     vocal_o = 0
#     vocal_u = 0 
#     
#     if cadena.isalpha():
#         
#         for i in cadena:
#             
#             if cadena[i].lower() in "a":
#                 vocal_a += 1
#             
#             elif cadena[i].lower() in "e":
#                 vocal_e +=1
#             
#             elif cadena[i].lower() in "i":
#                 vocal_i += 1
#             
#             elif cadena[i].lower() in "o":
#                 vocal_o += 1
#             
#             else: #cadena[i].lower() in "u"
#                 vocal_u += 1
#     
#     return vocal_a, vocal_e, vocal_i, vocal_o, vocal_u
# 
# def mayor_frecuencia(vocal_a, vocal_e, vocal_i, vocal_o, vocal_u):
#     
#     if (vocal_a > vocal_e or vocal_a > vocal_i or vocal_a > vocal_o or vocal_a > vocal_u):
#         devolver = "La vocal que mas se repite es la A"
#     
#     elif(vocal_e > vocal_a or vocal_e > vocal_i or vocal_e > vocal_u or vocal_e > vocal_u):
#         devolver = "La vocal que mas se repite es la E"
#     
#     elif(vocal_i > vocal_a or vocal_i > vocal_e or vocal_i > vocal_o or vocal_i > vocal_u):
#         devolver = "La vocal que mas se repite es la I"
#     
#     elif(vocal_o > vocal_a or vocal_o > vocal_e or vocal_o > vocal_i or vocal_o > vocal_u):
#         devolver = "La vocal que mas se repite es la O"
#     
#     else: #vocal_u > vocal_a or vocal_u > vocal_e or vocal_u > vocal_i or vocal_u > vocal_o
#         devolver = "La vocal que mas se repite es la U"
# 
#     return devolver
# #-------------------------- Bloque Principal ----------------------------------#
# def main():
#     cadena = "AaeeEiiiOoOuUu"
#------------------------------------------------------------------------------------# 



