__author__ = 'egbusquin'

class cola:

    def __init__(self):
       self._lista = []

    def encolar(self, valor):
        self._lista.append(valor)

    def desencolar(self):
        return self._lista.pop(0)

    def es_vacia(self):
        return self._lista == []

    def cantidad(self):
        return len(self._lista)

    def __str__(self):
        return str(self._lista)

if __name__ == "__main__":
    c = cola() #se instancia un objeto de la clase pila

    c.encolar(1)
    c.encolar(2)
    c.encolar(3)

    print(c)
    c.desencolar()

    print(c)

