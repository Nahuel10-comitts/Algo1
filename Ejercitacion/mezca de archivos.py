##################### Mezcla de Archivos ###############################
# Genera un solo archivos en base a otros dos archivos de igual estructura
# y que estan ordenados por algunos de sus datos.
# Cuando se encuentran dos "registros" con igual comparacion,4
# ambos registros se pasan al nuevo archivo.
# Se utilizan la misma funcion de lectura para ambos archivos.
""" Mezcla dos archivos """
#----------------------------- Funciones ------------------------------#

def leer_archivo(archivo):
    linea = archivo.readline()
    return archivo.rstrip("\n").split(",") if linea else ("", "") # Devuelve una tupla vacia.

#-----------------------------------------------------------------------#

def grabar_nuevo(archivo, codigo_producto, cantidad_vendida):
    archivo.write(codigo_producto, " + ", canridad_vendida, "\n")

#-----------------------------------------------------------------------#   

def mezcla_archivos(ar_suc1, ar_suc2, ar_suc_gral):
    # Tener en cuenta que en esta funcion estamos recibiendo los archivos
    # abiertos, si no estuvieramos seguros que no encontramos al principio
    # de los archivos, antes de hacer la primera lectura, deberiamos aplicar
    # un seek(0), a ar_suc1 y ar_suc2, para asegurar que procesaremos los datos
    # desde el principio al final de cada archivo.
    cod_prod_suc1, cant_suc1 = leer_archivo(ar_suc1)
    cod_prod_suc2, cant_suc2 = leer_archivo(ar_suc2)
    while (cod_prod_s1 and cod_prod_s2):
        if (cod_prod_s1 == cod_prod_s2):
            grabar_nuevo(ar_suc_gral, cod_prod_s1, cant_s1)
            grabar_nuevo(ar_suc_gral, cod_prod_s2, cant_s2)
            cod_prod_s1, cant_s1 = leer_archivo(ar_suc1)
            cod_prod_s2, cant_s2 = leer_archivo(ar_suc2)
        elif (cod_prod_s1 < cod_prod_suc2):
            grabar_nuevo(ar_suc_gral, cod_prod_s1, cant_s1)
            cod_prod_s1, cant_s1 = leer_archivo(ar_suc_2)
        else:
            grabar_nuevo(ar_suc_gral, cod_prod_s2, cant_s2)
            cod_prod_s2, cant_s2 = leer_archivo(ar_suc_s2)
        
    while (cod_prod_S1):
        grabar_nuevo(ar_suc_gral, cod_prod_s1, cant_s1)
        cod_prod_s1, cant_s1 = leer_archivo(ar_suc1)
    
    while (cod_prod_S2):
        grabar_nuevo(ar_suc_gral, cod_prod_s2, cant_s2)
        cod_prod_s2, cant_s2 = leer_archivo(ar_suc2)
            
###############################  Bloque Principal ########################################

ar_suc1 = open("sucursal1.csd", "r")
ar_suc2 = open("sucursal2.csd", "r")
ar_suc_gral = open("sucursal_ventas.csd", "w")
mezclar_archivos(ar_suc1, ar_suc2, ar_suc_gral)
ar_suc1.close()
ar_suc2.close()
ar_suc_gral.close()
        
    
