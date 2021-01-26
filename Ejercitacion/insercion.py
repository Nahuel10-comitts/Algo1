# Inserción / Insertion Sort 

def insercion(l):
    n = len(l)
    for i in range(1, n):
        
        # Empezando del segundo elemento, tomo cada uno
        elem = l[i]
        j = i-1
        
        # Y miro hacia atrás haciendo lugar
        while j >= 0 and elem < l[j]:
            # Muevo para adelante los que son mayores a elem
            l[j+1] = l[j]
            # Y sigo retrocediendo
            j -= 1
        
        # Al salir del ciclo inserto elem ordenado
        l[j+1] = elem
        
    return l

l = [4, 2, 1, 5, 3]

print(insercion(l))