# Idea: crear una funcion que tome el archivo.py y de lo devuelva sin los comentarios.
def leer(ar_python):
    linea = ar_python.readline()
    devolver = linea.rstrip("\n") if linea else ("","")
    return devolver

def listar(ar_python):
    ar_python = open("c:es_par.py", "r")
    codigo = leer(ar_python)
    while codigo:
        if codigo.find(""""""):
            n_codigo = codigo.split("""""")
            
            

    