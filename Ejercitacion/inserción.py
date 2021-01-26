# Insercion
def insercion(l):
    n = len(l)
    for i in range(1, n):
        # Se empieza por el segundo elemento, tomo cada uno de ellos.
        
        elemento = l[i]
        j = i - 1
        
        # Y miro hacia atras haciendo lugar.
        while (j >= 0 and elemento < l[j]):
            # Muevo para adelante los que son mayores a elem.
            l[j + 1] = l[j]
            # Y sigo retrocediendo
            j -= 1
        # Al salir del ciclo, inserto el elemento ordenado.
        l[j + 1] = elemento
        
    return l
#---------------------------- Bloque Principal ------------------------#
lista = [5, 3, 1, 2, 4]
print(insercion(lista))