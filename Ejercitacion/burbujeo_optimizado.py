# Burbujeo optimizado
def burbujeo_op(l):
    n = len(l) - 1
    intercambio = True
    while n > 0 and intercambio:
        intercambio = False
        for i in range(n):
            if l[i] > l[i + 1]:
                intercambio = True
                l[i], l[i + 1] = l[i + 1], l[i]    
        n -= 1          
    return l
#------------- Bloque Principal ------------------#
lista = [5, 3, 1, 2, 4]
print(burbujeo_op(lista))
            