# Ejercicio clase archivos de texto (csv).
# Recorrer el archivo maestro de clientes, y aplicar al saldo del cliente una
# actualización del 50%. Mostrar los datos del cliente, con su saldo original y
# el actualizado. Al mismo tiempo, generar un nuevo archivo que contenga en lugar
# del saldo original, el saldo actualizado.
#----------------------------------------------------------------------------#
def leer_archivo(archivo):
    
    linea = archivo.readline()
    
    if linea:
        return linea.rstrip("\n").split(",")
    else:
        return " ", " ", "0","0"
 
 #--------------------------------------------------------------------------#
 
def mostrar_datos(numero, nombre_apellido, saldo_original, saldo_actualizado):
    
    print("Cliente: {0} - {1}".format(numero, nombre_apellido))
    print("Saldo original: {0, 5d} - Saldo actualizado: {1: 5d}\n".format(saldo_original, saldo_actualizado))
    
    return

#------------------------------------------------------------------------------#

def salvar_datos(archivo, numero, nombre_apellido, saldo):
    
    linea = "{}, {}, {}".format(numero, nombre_apellido, saldo)
    archivo.write(linea)
    
    return
#-----------------------------------------------------------------------------#
def procesar_archivo(fmaestro, fmaestro_nuevo):
    
    numero, nombre_apellido, saldo = leer_archivo(fmaestro)
    
    while numero:
        saldo = int(saldo)
        saldo_actualizado = int(saldo * 1.5)
        mostrar_datos(numero, nombre_apellido, saldo)
        salvar_datos(fmaestro_nuevo, numero, nombre_apellido, saldo_actualizado)
        numero, nombre_apellido, saldo = leer_archivo(fmaestro)
        
    return
############################## Bloque Principal ################################################
def main():
    
    fmaestro = open("c:maestro.csv")
    fmaestro_nuevo = open("c:maenuevo", "w")
    
    procesar_archivo(fmaestro, fmaestro_nuevo)
    
    fmaestro.close()
    fmaestro_nuevo.close()
    
main()
    