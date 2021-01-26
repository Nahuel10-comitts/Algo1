# Genera un vector aleatorio y luego lo ordena por selección. Calcula el tiempo que tarda.
# Andres Juarez

import random
from time import time

MAX = 10
MAX_RANGO = 100000

def cargar(n):
##    random.seed(1)
    v = []
    for i in range(n):
        v.append(random.randint(1, MAX_RANGO))
    return v


def intercambiar(v, i, j):
    aux = v[i]
    v[i] = v[j]
    v[j] = aux


def ordenar(v, n):
    for i in range(n-1):
        minimo = i
        for j in range(i+1, n):
            if (v[j] < v[minimo]):
                minimo = j
        intercambiar(v, i, minimo);

def mostrar(v):
    for elem in v:
        print(elem)

def main():
    vec = cargar(MAX)
    print("Empieza a ordenar...")
    t0 = time()
    ordenar(vec, MAX)
##  si se quiere ordenar por medio de Python comentar la linea anterior y descomentar la siguiente    
##  vec.sort()
    t1 = time()
    
    print("Termine de ordenar. Tarde ", t1 - t0, " segundos")
##  para ver el vector ordenado sacar los comentarios siguiente linea    
##  mostrar(vec)

main()
                 
