# Seleccion
def seleccion(l):
    n = len(l)
    for i in range(n):
        # Asumimos que en i esta la minima posicion.
        minimo = i
        
        # Recorremos el resto de la lista.
        for j in range(i + 1, n):
            if (l[j] < l[minimo]):
                # Si encontramos un nuevo minimo, actualizamos la posicion.
                minimo = j
                
        # Llevamos el minimo a la posicion i.
        l[i], l[minimo] = l[minimo], l[i]
    
    return l

#-------------------------- Bloque Principal -----------------------#
lista = [5, 3, 1, 2, 4]
print(seleccion(lista))