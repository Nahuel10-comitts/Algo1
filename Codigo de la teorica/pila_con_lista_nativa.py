__author__ = 'egbusquin'

class pila:

    def __init__(self):
       self._lista = []

    def apilar(self, valor):
        self._lista.append(valor)

    def desapilar(self):
        return self._lista.pop()

    def es_vacia(self):
        return self._lista == []

    def cantidad(self):
        return len(self._lista)

    def __str__(self):
        return str(self._lista)

if __name__ == "__main__":
    p = pila() #se instancia un objeto de la clase pila

    p.apilar(1)
    p.apilar(2)
    p.apilar(3)

    print(p)
    p.desapilar()

    print(p)

