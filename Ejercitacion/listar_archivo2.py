# Listar el archivos de ventas recorriendolo secuencialmente, separado cada uno de los datos
# que vienen en la linea e informando al final el total general de cantidad y de importe.

#------------------------------------Funciones------------------------------------------------#

def leer_archivo(ar_ventas): # Sufrira un cambio
    """Funcion que lee los valores del archivo y devuelve los valores leidos
       cod_sucursalr, cod_articulo, cant_ventas, imp_total.
       En caso de llegar al final devuelve 4 valores vacios."""
    
    linea = ar_ventas.readline()
    
    if linea:
        devolver = linea.rstrip("\n").split(",")
    
    else:
        devolver = "", "", "0", "0"
    
    return devolver

def listar_archivo2():
    ar_ventas = open("c:ventas.csd", "r") # Sino se utiliza el with open en el mismo modulo
                                          # tiene que abrise y cerrarse el archivo.
    cod_suc, cod_art, ventas, imp = leer_archivo(ar_ventas)
    ventas = int(ventas)
    imp = float(imp)
    cant_total_gral = imp_total_gral = 0
    
    # Lectura total del archivo linea a linea
    
    while cod_suc:
        print("{0:4}\t{1:5}\t{2:5}\t{3:8.2f}".format(cod_suc, cod_art, ventas, imp))
        
        cant_total_gral += ventas
        imp_total_gral += imp
        
        cod_suc, cod_art, ventas, imp = leer_archivo(ar_ventas)
        ventas = int(ventas)
        imp = float(imp)
    print("Total General: \t{0:5}\t{1:8.2f}".format(cant_total_gral, imp_total_gral))
    
    ar_ventas.close()
    
    return
#------------------------------------------- Bloque Principal ---------------------------------------#
listar_archivo2()