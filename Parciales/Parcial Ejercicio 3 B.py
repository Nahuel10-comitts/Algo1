"""
// Va con un diccionario cargado - importar el modulo inscriptos
El diccionario "materias" tiene cargadas asignaturas como clave y una lista con tres
numeros enteros:
cantidad de alumnos anotados (como primer valor), cantidad de alumnos que rindieron el
parcial (segundo valor), cantidad de alumnos que aprobaron el parcial (tercer valor).
Se pide que hagas un programa en Python que:
*Indique si hay alguna materia cuyo indice de desercion es mayor al 50% (esto se calcula
teniendo en cuenta la cantidad de alumnos que rindieron el parcial sobre la cantidad de
anotados).
*Liste de mayor a menor las materias por porcentaje de aprobados (se calcula sobre la
cantidad que rindieron). 
Indicando 
materia - porcentaje

NOTA: bajate este archivo que tiene un diccionario cargado. El codigo escribilo en otro
archivo y este lo tenes que importar..

NOTA 2: copia y pega este enunciado como comentario al principio de tu archivo.

NOMBRA TU ARCHIVO DE LA SIGUIENTE FORMA: padrón_apellido_ej_3b.py  reemplazando padrón
por tu padrón y apellido, por tu apellido
"""
def indice_desercion(nombre, materia):
    
    indice=materia[nombre][0]/materia[nombre][1]
    
    return indice

def desercion(materia):
    desercion=False
    
    
    for nombre in materia:
        
        if indice_desercion(nombre, materia)>0.5:
            desercion= True
            
    return desercion


def ranking(materias):
    
    ranking={}
    
    for nombre in materias:
        
        ranking[nombre]=materias[nombre][2]/materias[nombre][1]*100
        
    ranking=sorted(ranking.items(), key= lambda x: x[1] , reverse= True )
    
    return ranking



from materias import materias




if desercion(materias):
    print("Por lo menos hay una materia cuyo indice de desercion es mayor al 50%")
else:
    print("No hay materias cuyo indice de desercion es mayor al 50%")

ranking=ranking(materias)

print("Porcentaje de aprobados")

for i in range(0, len(ranking)):
    
    print(ranking[i][0], "-",ranking[i][1])
