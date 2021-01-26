# Ejercicio 1
# numero = int(input("Ingrese numero: "))
# lista_numeros = [ i for i in range(numero, 21)]
# print(lista_numeros)
#----------------------------------------------------------#
# Ejericio 2
# def factorial(n):
#     if n == 0:
#         devolver = 1
#     
#     else:
#         devolver = n * factorial(n - 1)
#     
#     return devolver
# #------------------------- Bloque Principal ------------------------#
# n = int(input("Ingrese numero: "))
# print(factorial(n))
#-------------------------------------------------------------------#
# Ejercicio 3
# numeros = [0]
# 
# num1 = int(input("Ingrese primer numero: "))
# numeros.append(num1)
# 
# num2 = int(input("Ingrese segundo numero: "))
# numeros.append(num2)
# 
# num3 = int(input("Ingrese tercer numero: "))
# numeros.append(num3)
# 
# print(numeros)
# 
# n = num1 + num2
# numeros.append(n)
# 
# n2 = num1 + num3
# numeros.append(n2)
# 
# n3 = num2 + num3
# numeros.append(n3)
# 
# numeros.sort()
# 
# print(numeros)
#-----------------------------------------------------#
# Ejercicio 4
# numeros = [0,3,1,2]
# num = int(input("Ingrese numero, con -1 sale: "))
# posicion = 0
# largo = len(numeros)
# 
# while posicion < largo and num != -1:
#     
#     numeros.append(num)
#     
#     if num> numeros[posicion]:
#         print("El numero maximo es: ", num, ", en la posicion: ", largo + 1)
#     
#     else: 
#         print("El numero minimo es: ", numeros[posicion], ", en la posicion: ", posicion)
#     
#     posicion += 1
#     
#     num = int(input("Ingrese numero, con -1 sale: "))
#-----------------------------------------------------------------------------------------#
# Ejercicio 5
# N1 = 7
# N2 = 3
# 
# if N1 > N2:
#     print("El numero mayor es: ", N1)
#    
# else: # N1 < N2
#     print("El numero menor es: ", N1)
# -------------------------------------------------------------------------#
# # Ejercicio 6
# nro_1 = -6
# nro_2 = 5
# 
# abs_nro_1 = -nro_1 if (nro_1 < 0) else nro_1
# abs_nro_2 = -nro_2 if (nro_2 < 0) else nro_2
# 
# if abs_nro_1 < abs_nro_2:
#     nro_menor = abs_nro_1
#     nro_mayor = abs_nro_2
# 
# else:
#     nro_menor = abs_nro_2
#     nro_mayor = abs_nro_1
# 
# resultado = 0
# 
# for i in range(nro_menor):
#     resultado += nro_mayor
# 
# signo = 1 if (nro_1 < 0 and nro_2 < 0) or (nro_1 > 0 and nro_2 > 0) else -1
# 
# print("Resultado de la multiplicacion por sumas sucesivas: ", signo * resultado)
#---------------------------------------------------------------------------------------------------#
# Ejercicio 8
# valor = int(input("Ingrese valor: "))
# 
# if valor <= 1:
#     print("El valor ingresado no es primo")
# 
# else:
#     divisor = 2
#     while (((valor % divisor)!=0) and (divisor <= valor/2)):
#         divisor += 1
#         
#         if divisor > valor/2:
#             print("El valor ingresado es primo")
#         
#         else:
#             print("El valor ingresado no es primo")
#             
#----------------------------------------------------------------------------------------------#
# Ejercicio 10
# empleado1 = "Juan Perez"
# salario1 = 2000
# empleado2 = "Nahuel Lescano"
# salario2 = 15000
# empleado3 = "Zoe Villarreal"
# salario3 = 4500
# empleado4 = "Nicolas Alves"
# salario4 = 1500
# 
# if salario2 > salario1 > salario3 > salario4:
#     print("El salario maximo es: ", salario2, "de la persona que la recibe es: " ,empleado2)
 











