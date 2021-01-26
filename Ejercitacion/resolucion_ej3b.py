
"""
// Va con un diccionario cargado - importar el modulo inscriptos

El diccionario "materias" tiene cargadas asignaturas como clave y una lista con tres numeros enteros:
cantidad de alumnos anotados (como primer valor), cantidad de alumnos que rindieron el parcial
(segundo valor), cantidad de alumnos que aprobaron el parcial (tercer valor).

Se pide que hagas un programa en Python que:

Indique si hay alguna materia cuyo indice de desercion es mayor al 50% (esto se calcula teniendo en cuenta la cantidad de alumnos
que rindieron el parcial sobre la cantidad de anotados).

Liste de mayor a menor las materias por porcentaje de aprobados (se calcula sobre la cantidad que rindieron). 
Indicando 

materia - porcentaje

NOTA: bajate este archivo que tiene un diccionario cargado. El codigo escribilo en otro archivo y este lo tenes que importar..

NOTA 2: copia y pega este enunciado como comentario al principio de tu archivo"""

#from archivo_materias import materias
materias = {}
materias["AM II"] = [2300, 1800, 250]
materias["Algebra"] = [2100, 1300, 325]
materias["Algoritmos I"] = [300, 220, 160]
materias["Algoritmos II"] = [240, 200, 150]
materias["Fisica"] = [1600, 900, 600]
materias["Quimica"] = [450, 420, 380]
materias["Computacion"] = [400, 330, 310]

#INPUT: dicc //OUTPUT: list 
def listar_creciente(asignaturas):
    dic = {}
    for key in asignaturas.keys():
        calculo_uno = asignaturas[key][1]*100 #Aprobados * 100%
        porcentaje = calculo_uno//asignaturas[key][0] #aprobados*100 / inscriptos   |   Use // para que redondee
        dic[key] = porcentaje
    dic = sorted(dic.items(), key = lambda tupla: tupla[0], reverse=True) #Aca se convierte de dicc a lista
     
    return dic #Devuelve lista de tuplas
                     
    
        
#Input: dicc //OUTPUT: list
def materia_desercion(asignaturas):
    lista_materias = []
    for materia in asignaturas:
        anotados = asignaturas[materia][0]
        rindieron = asignaturas[materia][1]
        if (rindieron/anotados) > 0.5: #Aca calcule el indice como pide en el enunciado
            lista_materias.append(materia)
    return lista_materias


def main():
    diccionario = materias #Igualo el diccionario importado a una variable local; Si quiero pude haber usado la variable "materias" de entrada
    
    lista_decresion = materia_desercion(diccionario) #Punto 1
    print("Las materias con un indice de descercion mayor al 50% son {}".format(lista_decresion))
    
    lista_ordenada = listar_creciente(diccionario) #Punto 2
    print("Las asignaturas ordenadas en forma decreciente son {}".format(lista_ordenada))
    return None

main()