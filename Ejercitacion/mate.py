def sumar(x, y):
    return x + y

def multiplicar(a, b):
    cont = 0
    for i in range(a):
        cont = sumar(cont,b)

    return cont

def restar(x, y):
    return sumar(x, -y)

def dividir(a, b):
    return a // b, a % b

if __name__ == '__main__':
    print(sumar(5,4))
    print(multiplicar(4, 6))
    print(restar(5,10))
    print(dividir(8, 4))
    