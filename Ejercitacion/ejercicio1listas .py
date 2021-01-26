"""1. Desarrollar una función que devuelva en un vector (una lista) los números primos
entre 2 y 200. Reutilizar lo que ya se escribió y probó. """
def es_primo(valor):
    #Pre: La funcion verifica que un numero sea primo o no
    #Post: devuelve True si es primo o False sino lo es
    devolver = False
    lista_primos = []
 
    if valor <= 1:
        devolver = False
    
    else:
        divisor = 2
        while (((valor % divisor)!=0) and (divisor <= valor/2)):
            divisor += 1
        
        if divisor > valor/2:
            devolver = True
            lista_primos.append(valor)
         
        else:
            devolver = False
            
    return devolver