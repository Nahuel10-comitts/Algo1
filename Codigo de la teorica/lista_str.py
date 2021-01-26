class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.prox = None 

class ListaEnlazada:
    def __init__(self):
        self.primero=None


    def agregarAlFinal(self, valor):
        if self.primero==None:
            self.primero=Nodo(valor)
        else:
            actual = self.primero
            while actual.prox != None:
                actual = actual.prox

            actual.prox = Nodo(valor)

    def agregarAlPrincipio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.prox = self.primero
        self.primero = nuevo_nodo

    def sacarDelFinal(self):
        if self.primero == None:
            raise LookupError

        if self.primero.prox == None:
            valor = self.primero.valor
            self.primero = None
            return valor

        actual = self.primero
        while actual.prox.prox != None:
            actual = actual.prox

        valor = actual.prox.valor
        actual.prox = None
        return valor

    def sacarDelPrincipio(self):
        if self.primero == None:
            raise LookupError

        valor = self.primero.valor
        self.primero = self.primero.prox
        return valor

    def __str__(self):
        salida = "[ "
        actual = self.primero
        while actual != None:
            salida += "{} {}".format(actual.valor, " -> " if actual.prox != None else "")
            actual = actual.prox
        return salida + "]"

if __name__=='__main__':
    print('Probando...')
    lista = ListaEnlazada()
    lista.agregarAlFinal(8)
    lista.agregarAlFinal(4)
    lista.agregarAlFinal(2)
    lista.agregarAlFinal(1)
    lista.agregarAlFinal(7)
    lista.agregarAlFinal(5)
    print(lista)
    assert lista.sacarDelFinal()==5, 'Esperaba sacar 5 del final'
    assert lista.sacarDelPrincipio()==8, 'Esperaba sacar 8 del principio'
    lista.agregarAlPrincipio(1)
    assert lista.sacarDelPrincipio()==1, 'Esperaba sacar 1 del principio'
    print("Lista al finalizar:")
    print(lista)


