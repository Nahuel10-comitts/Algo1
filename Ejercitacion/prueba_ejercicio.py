'''
3) Ingresar en un diccionario localidades (clave) y dos datos: cantidad de habitantes – cantidad de centros asistenciales de salud (CAS). Los datos surgen de distintas planillas, 
por lo que una misma clave (localidad) se puede ingresar varias veces, debiendo sumarse los valores. Se pide: 
a) Listar el total de habitantes y CAS para cada localidad.
b) Imprimir un listado ordenado de mayor a menor de las 5 localidades de mayor relación habitantes / CAS. Indicando: localidad – relación.
'''

def print_dicc_sorted(dicc_info):
    list_info = []
    for key in dicc_info.keys():
        if dicc_info[key]['habitantes'] != 0 and dicc_info[key]['CAS'] != 0:
            equation = dicc_info[key]['habitantes'] // dicc_info[key]['CAS']
        else:
            equation = 0
        list_info.append([key,equation])

    order_list = sorted(list_info, key = lambda x: x[1], reverse = True)
    print('\nLas localidades com ayor relación son:')
    for elemento in order_list[:5]:
        print(elemento)


def list_information(dicc_info):

    for key in dicc_info.keys():
        pass
    return print(list(dicc_info))

def build_dicc(dicc_info, location, amount_population, amounto_health_centers):
        if location not in dicc_info.keys():
            dicc_info[location] = {'habitantes': amount_population, 'CAS': amounto_health_centers}
        else:
            dicc_info[location]['habitantes'] += amount_population
            dicc_info[location]['CAS'] += amounto_health_centers
        return dicc_info

def log_information():
    dicc_info = {}
    
    print('\nPresione ENTER para salir')
    location = str(input('Ingrese la localidad: ')).title()
    while location != '':
        
        amount_population = int(input('Ingrese la cantidad de habitantes: '))
        amounto_health_centers = int(input('Ingrese la cantidad de centros asistenciales: '))

        build_dicc(dicc_info, location, amount_population, amounto_health_centers) 

        print('\nPresione ENTER para salir')
        location = str(input('Ingrese la localidad: ')).title()
    
    return dicc_info


def main():
    dictionary = log_information()

    #list_information(dictionary)

    print_dicc_sorted(dictionary)  
    
main()