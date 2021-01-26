"""
// Va con un diccionario cargado - importar el modulo inscriptos

El diccionario "materias" tiene cargadas asignaturas como clave y una lista con tres
numeros enteros:

+cantidad de alumnos anotados (como primer valor),
+cantidad de alumnos que rindieron el parcial (segundo valor),
+cantidad de alumnos que aprobaron el parcial (tercer valor).

Se pide que hagas un programa en Python que:

Indique si hay alguna materia cuyo indice de desercion es mayor al 50% (esto se calcula
teniendo en cuenta la cantidad de alumnos que rindieron el parcial sobre la cantidad de
anotados).

Liste de mayor a menor las materias por porcentaje de aprobados (se calcula sobre la
cantidad que rindieron).

Indicando 
materia - porcentaje

"""
from inscriptos import materias

def desercion(materias):
    
    devolver = False
    for i in materias:
        if (materias[i][1]/materias[i][0]) > 0.5: #revisar ---> usar while
            devolver = True
    return devolver
    
        
def tabla(materias):
    return sorted(materias.items(), key = lambda x : x[1][2] / x[1][1], reverse = True)

def main():
    
    if desercion(materias):
        print("Hay al menos una materia cuya desecrion es mayor al 50%")
    else:
        print("No hay ninguna materia cuya descions sea mayor al 50%")
        
    tablax = tabla(materias)
    for i in tablax:
        print(i[0], i[1][2]/i[1][1])
main()