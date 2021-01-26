"""Programar una funcion que dada una palabra calcule la cantidad de veces que esta cada
una de las letras que la contiene."""

def cantidad_de_letras(palabra):
    cant_letras = {}
    for letra in palabra:
        if letra not in cant_letras:
            cant_letras[letra] = 1
        else:
            cant_letra[letra] += 1
            
    for letra in cant_letras:
        print("La letra", letra, "se encuentra", cant_letras, "veces")
#--------------------------------- Bloque Principal ---------------------------------------------#      
palabra = input("Ingresa una palabra: ")
cantidad_de_letras(palabra)