# Busqueda binaria
def busq_binaria(pajar, aguja):
    #Pre: Busca un elemento en la lista y devuele la posicion en la que esta.
    # Si no esta devuelve None.
    #Post: La lista tiene que estar ordenada.
    n = len(pajar)
    minimo = 0
    maximo = n
    resultado = None
    while(minimo < maximo and resultado == None):
        medio = (minimo + maximo) // 2
        if (pajar[medio] == aguja):
            resultado = medio
        elif(pajar[medio] < aguja):
            minimo = medio + 1
        else: #pajar[medio] > aguja
            minimo = medio - 1
    return resultado
#---------------- Bloque Principal ------------------#
lista = [1,2,3,4,5] # La lista tiene que estar ordenada.
print(busq_binaria(lista, 3))
