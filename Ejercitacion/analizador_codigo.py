"""
Aclaraciones: para que sea mas claro el flujo del programa, los archivos se abren y se cierran en el main. Es decir, todas las funciones se independizan
de abrir o cerrar archivos.
Se intenta que cada funcion resuelva un unico problema.


1) Abre el archivo con los nombres de los programas python que analizara.
2) Luego guarda los nombres en una lista ---> lista_archivos = ["programa_principal.py","modulo_1.py","modulo_2.py",...,"modulo_n.py"]
3) Cierra el archivo de programas python.
4) Recorre la lista de nombres de archivos con codigo fuente
5) abre cada archivo, lo procesa secuencialmente.
6) Escribe en codigo_fuente.CSV o comentarios.CSV, segun correponda. 
"""




def extraer_nombres_programas_python(archivo_programas):
    """
    PRE: recibe un archivo en formato txt, valido
    POST: devuelve una lista 
    
    Devuelve los nombres de los archivos, que debe procesar, en una lista
    """
#     ruta = os.path.join('data', “datos.csv")
    archivo = open('programas.txt','r') #archivo de programas de codigo python
    lista_archivos = []
    for linea in archivo:
        linea = linea.rstrip('\n') #la llamada a rstrip elimina el fin de línea que hay al final de cada línea
        lista_archivos.append(linea)
    archivo.close()
    return lista_archivos


# print(leer_archivos_fuente())
# leer_archivos_fuente()

def procesar_archivo(archivo):
    """
    PRE: recibe un archivo valido y abierto
    POST: crea dos archivos CSV, uno con el codigo fuente y el otro con los comentarios
    
    Lee el archivo secuencialmente escribiendo el codigo de cada funcion en el archivo codigo_fuente.CSV y los comentarios en el archivo comentarios.CSV
    """
    for linea in archivo:
#         devuelve dos strings: uno con codigo y otro con comentarios

        codigo, comentarios = procesar_linea(linea) # una lista puede estar vacia y la otra no; o las dos pueden tener contenido
#         escribir codigo en codigo_fuente.CSV
#         escribir comentarios en comentarios.CSV
#         escribe en un diccionario del tipo: dic_codigo = {'funcion1':[linea1,..,lineaN],...,'funcionN':'[linea1,..,lineaN]'}
#         escribe en un diccionario del tipo dic_comentarios = {'funcion1':[comentario1,..,comentarioN],...,'funcionN':[comentario1,..,comentarioN]}  
    return dic_codigo, dic_comentarios         
    pass

    
def procesar_linea(linea):
    linea_codigo = ""
    linea_comentarios = ""
    return linea_codigo, linea_comentarios

def main():
#     abrir archivo de programas
    lista_archivos = extraer_nombres_programas_python(archivo_programas)
#     cerrar archivo de programas
    for nombre_archivo in lista_archivos:
#         abrir archivo
        procesar_archivo(nombre_archivo)
#         cerrar archivo


main()