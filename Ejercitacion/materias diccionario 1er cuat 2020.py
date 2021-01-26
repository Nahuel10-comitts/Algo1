

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""



// Va con un diccionario cargado - importar el modulo inscriptos



El diccionario "materias" tiene cargadas asignaturas como clave y una lista con tres numeros enteros:

cantidad de alumnos anotados (como primer valor), cantidad de alumnos que rindieron el parcial

(segundo valor), cantidad de alumnos que aprobaron el parcial (tercer valor).



Se pide que hagas un programa en Python que:

1. Indique si hay alguna materia cuyo indice de desercion es mayor al 50% (esto se calcula
teniendo en cuenta la cantidad de alumnos que rindieron el parcial
sobre la cantidad de anotados).
2. Liste de mayor a menor las materias por porcentaje de aprobados (se calcula sobre la cantidad que rindieron). 
   
Indicando 

materia - porcentaje

NOTA: bajate este archivo que tiene un diccionario cargado. El codigo escribilo en otro archivo y este lo tenes que importar..

NOTA 2: copia y pega este enunciado como comentario al principio de tu archivo.

NOMBRA TU ARCHIVO DE LA SIGUIENTE FORMA: padrón_apellido_ej_3b.py  reemplazando padrón por tu padrón y apellido, por tu apellido


-------------------------------------------------------------------------------

Aqui coloca tu Padron: 

Aqui coloca tu Apellido y Nombre: 

-------------------------------------------------------------------------------

"""

import inscriptos

def indicar_materias_desercion(materias):
    """Pre: recibe un diccionario no vacio
       Post: Devuelve None
       
    imprime las materias con porcentaje de desercion mayor al 50%
    """
    claves = list(materias.keys())
    i = 0
    hay_desercion = False
    while i < len(claves) and hay_desercion == False:
        if materias[claves[i]][1] / materias[claves[i]][0] < 0.5:
            hay_desercion = True
        else:
            hay_desercion = False
        i += 1
    return hay_desercion
    
#     i = 0
#     hay_desercion = False 
#     while i < len(materias) and hay_desercion == False:
#         if materias[asigmat][1] / materias[asig][0] < 0.5:
#             hay_desercion = True
#         else:
#             hay_desercion = False
#         i+= 1
#     return hay_desercion
#     for asig in materias:
#         if materia[asig][1] / materia[asig][0] < 0.5:
#             es_desercion = True
#         else:
#             es_desercion = False
    
#     
#         if (materias[asig][0] - materias[asig][1]) / materias[asig][0] > 0.5:
#             print ('la asignatura',materias[asig],'tiene mas del 50% de desercion')
#         print('No hay desercion mayor al 50% en ningun materia')
#     return None 
        
# def ordena_aprobados(materias):
#     materias_aux = []
#     for asig in materias:
#     materias_aux = {}
#     dic = {}
#     for asig in materias:
#         if not asig in dic:
#             dic[asig] = [materias[2]/materias[1]]
#         else:
#             dic[asig].append(materias[2]/materias[1])
#     lista_materias = materias.items()
#     lista_aprobados = sorted(dic,key=lambda dic : dic.items(),reverse = True)



materias = {}
materias["AM II"] = [2300, 1800, 250]
materias["Algebra"] = [2100, 1300, 325]
materias["Algoritmos I"] = [300, 220, 160]
materias["Algoritmos II"] = [240, 200, 150]
materias["Fisica"] = [1600, 900, 600]
materias["Quimica"] = [450, 420, 380]
materias["Computacion"] = [400, 330, 310]


def main():
    indicar_materias_desercion(materias)
#     ordena_aprobados(materias)
    
main()
    

