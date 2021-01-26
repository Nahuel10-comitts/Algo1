
from pila_con_lista_nativa import pila

def balanceado(expresion):
    valido = True
    p = pila()

    for c in expresion:
        if c in ('[', '(', '{'):
            p.apilar(c)
        elif c == ']':
            if p.desapilar() != '[':
                valido = False
                break
        elif c == ')':
            if p.desapilar() != '(':
                valido = False
                break
        elif c == '}':
            if p.desapilar() != '{':
                valido = False
                break

    return p.es_vacia() and valido

print(balanceado("hola!"))
print(balanceado("((()))"))
print(balanceado("((()"))
print(balanceado("((({[[]]})))"))
print(balanceado("(}"))
print(balanceado(")))"))
