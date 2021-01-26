def desercionDic(materias):
	lista_desercion = []
	for materia in materias:
		desercionN = (materias[materia][1] / materias[materia][0])*100
		if ( desercionN > PORCENTAJE):
			lista_desercion.append((materia,desercionN))
	return lista_desercion


def ordenadoAprobados(materias):
	lista_aprobados = []
	for materia in materias:
		aprobadosN = (materias[materia][2] / materias[materia][1])*100
		lista_aprobados.append((materia,aprobadosN))
	return lista_aprobados

def ordenarLista(lista):
	listaOrdenada = sorted(lista, key=lambda x:x[1], reverse=True)
	return listaOrdenada


def imprimirlista(lista):
	for elemento in lista: 
		print(elemento)