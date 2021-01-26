# 11. Contar la cantidad de letras de un telegrama que termina en punto sin utilizar funciones de string, salvo la que indica la longitud

# def contar_letras(cadena):
#     cant_letras = 0
#     for c in range(len(cadena)):
#         if cadena[c].isalpha():
#             cant_letras += 1
#             print (cadena[c])
#     return cant_letras
# 
# 
# print(contar_letras("hola, como estas"))
#         

# def contar_letras(caden):
#     ind = 0
#     cant_letras = 0
#     while ind < (range(len(cadena))):
#         if cadena[ind].isalpha():
#             cant_letras += 1
#         ind += 1
#     return cant_letras

# 12: Contar la cantidad de letras hasta que encuentre un punto.....

def contar_letras(cadena):
    ind = 0
    cant_letras = 0
    while cadena[ind] != ".":
        if cadena[ind].isalpha():
            cant_letras += 1
        ind += 1
    return cant_letras


cadena = "hola como estas"
print(contar_letras(cadena))