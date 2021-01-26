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


from archivo_materias import materias

def desercion():
    desercion_alta=0
    for x in materias:
        desertores = 100 - ((materias[x][1] * 100) / materias[x][0])
        if desertores > 50:
            desercion_alta+=1
            
    if desercion_alta != 0:
        devolver = "Hay {} materias con un indice de desercion mayor al 50%".format(desercion_alta)
    else:
        devolver = "No hay materias con un indice de desercion mayor al 50%"
        
    return devolver

def materias_aprobadas():
    dic= {}
    for x in materias:
        aprobados = (materias[x][2] * 100) // materias[x][1]
        dic[x]= aprobados
    return "Las materias con mayor porcentaje de aprobados ordenadas en orden decreciente son", sorted(dic.items(), key=lambda x:x[1], reverse=True)



print (desercion())
print (materias_aprobadas())
    


