# Una opcion es usar el for
# No recomendable

def listar_archivos():
    """ La funcion hace que el recorrido del archivo elemento a elemento, utilizando un ciclo for.
        Dado a que el archivo es un objeto iterable, no es necesario utilizar en este caso la funcion
        de lectura ya que el metodo de iteracion se encarga de acceder a cada uno de los elementos
        (lineas), en el archivo. Tambien como alternativa valida, se utiliza un with.open para la
        apertura"""
    
    with open("c:ventas.csd", "r") as ar_ventas:
        cant_total_gral = imp_total_gral = 0
        for linea in ar_ventas:
            suc, art, cant, imp = linea.rstrip("\n").split(",")
            print("{0:4}\t{1:5}\t{2:5}\t{3:8.2f}".format(suc, art, int(cant), float(imp)))
            
            cant_total_gral += int(cant)
            imp_total_gral += float(imp)
            
        print("Total General: \t{0:5}\t{1:8.2f}".format(cant_total_gral, imp_total_gral))
    
    return

#----------------------------------- Bloque Principal ----------------------------------------------------#

listar_archivos()