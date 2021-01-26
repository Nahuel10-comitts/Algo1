# Busqueda lineal
def busq_lineal(pajar, aguja):
    n = len(pajar) 
    posicion = 0
    encontrado = False
    while (posicion < n and not encontrado):
        if (pajar[posicion] == aguja):
            encontrado = True
        else:
            posicion += 1
    return posicion
#------------------ Bloque Principal ---------------#
lista = [1, 12, 5, 6, 8, 10, 2]
print(busq_lineal(lista, 10))