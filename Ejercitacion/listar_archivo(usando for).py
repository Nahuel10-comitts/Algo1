############################################################################
#
# Listar archivo elemento a elemento, separando cada uno de los datos
# que vinen en la línea e informando al final el total general de
# cantidad y de importe
#
########################### FUNCIONES ######################################
"""---------------------------------------------------------------------------
Funcion que hace el recorrido del archivo elemento a elemento, utilizando
un ciclo for. Dado que el archivo es un objeto iterable, no es necesario
utilizar en este caso una funcion de lectura, ya que el metodo de iteracion
se encarga de acceder a cada uno de los elementos (lineas), en el archivo.
Tambien como alternativa valida, se utiliza with open para la apertura
"""
def leer_archivo(ar_ventas):
    
    linea = ar_ventas.readline()
    
    if linea:
        devolver = linea.rstrip("\n").split(",")
    
    else:
        devolver = " ", " ", "0", "0"
        
    return devolver

def listar_archivo():
    
    with open("c:ventas.csv", "r") as ar_ventas:
        
        cantidad_total_general = importe_total_general = 0
        
        for linea in ar_ventas:
            cod_sucursal, cod_articulo, cantidad, importe = leer_archivo(ar_ventas)
            print(cod_sucursal, cod_articulo, cantidad, importe)
            
            cantidad_total_general += int(cantidad)
            importe_total_general += float(importe)
        print("Total General: ", cod_sucursal, cod_articulo, cantidad, importe)
    
    return
#-------------------------- Bloque Principal --------------------------------#
listar_archivo()