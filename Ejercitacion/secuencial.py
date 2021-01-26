# Búsqueda secuencial / Linear search 

def busq_lineal(pajar, aguja):
    n = len(pajar)
    pos = None
    for i in range(n):
        if pajar[i] == aguja:
            pos = i
    
    return pos
       
l = [4, 2, 1, 5, 3]

print(busq_lineal(l, 5))