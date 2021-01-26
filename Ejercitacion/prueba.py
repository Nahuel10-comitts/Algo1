# def validar_clave(clave):
#     posicion = 0
#     cont_minusculas = 0
#     cont_mayusculas = 0
#     cont_numeros = 0
#     devolver = True 
#     if (len(clave) < 8 or len(clave) > 12 or clave.isalnum() == False): 
#         devolver = False
#     else:
#         while (posicion < len(clave) and devolver):
#             if (clave[posicion].islower() == True):
#                 cont_minusculas = 1      
#             elif (clave[posicion].isupper() == True):
#                 cont_mayusculas = 1    
#             elif (clave[posicion].isdigit() == True):
#                 cont_numeros = 1
#             if ((cont_minusculas + cont_mayusculas + cont_numeros) == 3):
#                 devolver = True          
#             posicion += 1              
#     return devolver
# 
# 
# contraseña = input("Ingrese su clave: ")
# print(validar_clave(contraseña))

clave = input("Ingrese clave: ")
posicion = 0
for posicion in clave:
    if 4 <= len(clave) <= 10 and clave[posicion] != clave[posicion] + str(1):
        print("Welcome to the junge")
    posicion += 1