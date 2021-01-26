from cola_con_lista_nativa import cola

def rapipago(clientes):
    while not clientes.es_vacia():
        nombre, impuestos = clientes.desencolar()
        cobrados = impuestos if impuestos <= 5 else 5
        print("Cobramos {} impuestos a {}".format(cobrados, nombre))
        if impuestos > 5:
            clientes.encolar((nombre, impuestos - cobrados))

personas = (("Juan", 4), ("Ana", 3), ("Pedro", 12), ("María", 5), ("Diego", 10))

c = cola()

for p in personas:
    c.encolar(p)
    
rapipago(c)
