def leer_codigo(path_archivo):
#Pre: Ingresa el path a un archivo con codigo de python
#Post se imprime linea a linea sin comentarios
    archivo = open(path_archivo, 'r') #Solamente leo el archivo

    #Leo la primera linea y en base a eso defino si entro
    #o no entro al while
    comentado_multi = False
    linea, comentado_multi = leer_linea(archivo, comentado_multi)

    while linea != None: #Mientras la linea no este vacia
        if linea != "":
            print(linea)
        linea, comentado_multi = leer_linea(archivo, comentado_multi)
    
    return None

def leer_linea(archivo, comentado_multi):
#Pre:ingresa un archivo ya abierto
#Post:Elimina de la linea los comentarios
    
    linea = archivo.readline()
    texto = ""
    
    if linea: #Si la linea es distanta de algo nulo
        indice = 0
        comentado = False

        while linea[indice] != '\n' and not comentado:
        #Ciclo hasta el final de la linea o hasta que encuentro
        #un comentario
            comentado, comentado_multi = identificar_comentarios(linea, indice, comentado_multi)
            if not comentado_multi and not comentado:
                texto += linea[indice]
            indice += 1
    
    else:
        texto = None

    return texto, comentado_multi #Devuelvo el texto sin comentar de la linea

def identificar_comentarios(linea, indice_actual, comentado_multi):
#Pre: ingresa la linea y su posicion
#Post: se fija si esa linea esta o no comentada
    if linea[indice_actual] == "#":
        comentado = True

    elif indice_actual + 2 < len(linea) and (linea[indice_actual] + linea[indice_actual+1] + linea[indice_actual+2]) == "\"\"\"":
        comentado_multi = not comentado_multi
        comentado = True

    else:
        comentado = False

    return comentado, comentado_multi

if __name__=="__main__":
    leer_codigo("ejercicios_parcial\datos.py")