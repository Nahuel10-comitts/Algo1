MAX_PADRON = 999999999

def convertir_datos(datos):
#     Convierte los datos de la linea a enteros
    l_datos = []
    for dato in datos:
        l_datos.append(int(dato))
    return l_datos

def leer(arch):
#     Lee una linea del archivo
    linea = arch.readline()
    if linea:
        datos = linea.rstrip("\n").split(",")
        devolver = convertir_datos(datos)
        
    else:
        devolver = (MAX_PADRON, 0, 0, 0, 0)
    
    return devolver

def guardar(arch, padron, notas):
#     Guarda el padron y las notas en el archivo de salida
    datos_notas = []
    for nota in notas:
        datos_notas.append(str(nota))
    notas_formato = ",".join(datos_notas)
    
    arch.write(str(padron) + "," + notas_formato + "\n")
    
def leer_lineas(l_arch):
#     Lee los archivos y devuelve una lista con lo que leyó de cada uno
    lineas = []
    si
    for arch in l_arch:
        linea = leer(arch)
        lineas.append(linea)
    return lineas

def menor_padron(lineas):
#     Calcula el menor número entre las padronursales y lo devuelve

    dato_menor = min(lineas)
    return dato_menor[0]

def merge(arch_salida, *archs_entrada):
#     PRE: arch_salida es un archivo abierto en modo sobreescritura
#          archs_entrada es una lista de archivos csv válidos abiertos en modo lectura
#          
#          Los datos de cada archivo están ordenados según el número de padrón
#          
#     POS: los datos de los archs_entrada se guardan ordenados en arch_salida

    lineas = leer_lineas(archs_entrada)
    menor = menor_padron(lineas)
    
    #Mientras no se llegue al final en todos los archivos
    while menor < MAX_PADRON:
        #Recorre las líneas al de los archivos
        for i in range(len(lineas)):
            padron, *notas = lineas[i]
            #Guarda los datos de la línea mientras la padronursal no cambie
            while padron == menor:
                guardar(arch_salida, padron, notas)
                #Actualiza los datos de la línea
                padron, *notas = leer(archs_entrada[i])
            #La línea que no cumplió la condición se guarda en la lista para el próximo ciclo
            lineas[i] = [padron, *notas]
            
        menor = menor_padron(lineas)
        
###################################################################################################
def main():
    
    arch_1 = open("andres.csv")
    arch_2 = open("ezequiel.csv")
    arch_3 = open("gustavo.csv")
    arch_4 = open("uriel.csv")
    
    arch_salida = open("correctores.csv", "w")
    
    merge(arch_salida, arch_1, arch_2, arch_3, arch_4)
    
    arch_1.close()
    arch_2.close()
    arch_3.close()
    arch_4.close()
    arch_salida.close()

main()
