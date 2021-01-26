

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
    


def ordena_aprobados(materias):
    aprobados = {}
    for materia in materias:
        aprobados[materia] = (materias[materia][2] / materias[materia][1]) * 100
    ordenada_por_casos = sorted(aprobados.items(), key = lambda materia: materia[1],reverse = True)
    return ordenada_por_casos


materias = {}
materias["AM II"] = [2300, 1800, 250]
materias["Algebra"] = [2100, 1300, 325]
materias["Algoritmos I"] = [300, 220, 160]
materias["Algoritmos II"] = [240, 200, 150]
materias["Fisica"] = [1600, 900, 600]
materias["Quimica"] = [450, 420, 380]
materias["Computacion"] = [400, 330, 310]


def main():
    if indicar_materias_desercion(materias):
        print ('hay materias con desercion mayor al 50%')
    else:
        print ('no hay materias con desercion mayor al 50%')
    print('lista mayor cantidad de aprobados por materia: ')
    dic_aprobados = ordena_aprobados(materias)
    for materia in dic_aprobados:
        print(materia[0], materia[1])
    
    
main()
    

