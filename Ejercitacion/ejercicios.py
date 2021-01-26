"""14. Dado un texto terminado en “.” se pide determinar cuántas veces aparece
determinada letra que se indica por teclado. Sin utilizar funciones de string, salvo
len.""" 

def contador_letras(cadena):
    cant_apariciones = 0
    for i in range(len(cadena)):
        if cadena[i] == cadena[i - 1]:
            cant_apariciones += 1
    return cant_apariciones

cadena = input("Ingrese cadena: ")
print(contador_letras(cadena))
