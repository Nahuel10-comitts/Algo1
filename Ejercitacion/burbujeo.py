# Burbujeo/ version 1
def burbujeo(l):
    n = len(l)
    for i in range(n):
        #Desde la primer posicion hasta la anteultima.
        for j in range(0, n - i - 1):
            #Compara los adyacentes y los intercambia si estan desordenados.
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                
    return l
#----------------------- Bloque Principal -------------------------------------#
lista = [4, 3, 1, 2, 5]
print(burbujeo(lista))
            