#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Las 23 provincias más CABA realizan sus aportes a la Nación mediante impuestos, a su vez, Nación le transfiere 
fondos mediante la coparticipación.
A cada provincia se le asocian 6 datos: los 5 primeros son los impuestos que pagan a Nación, en el siguiente 
orden: IVA, Ganancias, Contribuciones, Exportaciones, Otros. El último dato es la coparticipación que paga 
Nación a las provincias.
Se pide hacer un programa en Python que:
1)  Determine el impuesto máximo abonado, indicando el tipo de impuesto y la provincia. Por ejemplo: Córdoba – 
Ganancias - $3200 millones.
2)  Indique si el IVA fue el mayor impuesto abonado en el año teniendo en cuenta el total de impuestos.
3)  Imprima un listado de las 10 provincias que recibieron mayor coparticipación en relación a sus aportes, 
ordenado de mayor a menor por porcentaje, por ejemplo, si aportó 40 y recibió 30, el porcentaje es 75% (30/40).
 Se debe indicar porcentaje – provincia:

Porcentaje  Provincia

Nota: 
•   Los montos vienen dados en millones de pesos.

•   Para la carga de la matriz solo hay que llamar a la función cargar_matriz( ) del módulo auxiliar
 que devuelve la matriz cargada.'''
 #---------------------------------------------------------------------------------------------------------------

provincia = {'cordaba':{'iva':10,'ganancia':100,'con':350,'expo':400,'otro':1000,'copa':700},'Bs as':{'iva':30000,'ganancia':400,'con':550,'expo':3000,'otro':100,'copa':900,}}

def maximo_impuesto_provincia(corrientes):
    mayor = -1
    provincia_nombre = ''
    for name in provincia:
        nombres = provincia[name]
        for impuesto in nombres:
            if(nombres[impuesto] > mayor):
                provincia_nombre = name
                mayor=nombres[impuesto]
    return mayor,provincia_nombre

def iva_mayor_impuestos(provincia):
    impuestos=[0,0,0,0,0,0]
    for name in provincia:
        impuestos[0]+=provincia[name]['iva']
        impuestos[1]+=provincia[name]['ganancia']
        impuestos[2]+=provincia[name]['con']
        impuestos[3]+=provincia[name]['expo']
        impuestos[4]+=provincia[name]['otro']
        impuestos[5]+=provincia[name]['copa']
    mayor = -1
    iva='el iva no es el impuesto mayor'
    for valor in impuestos:
        if valor > mayor:
            mayor = valor
    if mayor==impuestos[0]:
        iva='el iva es el mayor impuesto' 
    return iva
    
def ordenar_mayor(provincia):
    lista_mayor=[]
    suma=0
    por=0.00
    for nombre in provincia:
        nombres = provincia[nombre]
        for impuesto in nombres:
            suma+=nombres[impuesto]
        por=round((provincia[nombre]['copa']/suma),2)
        lista_mayor.append([nombre,por])
    ordenado = sorted(lista_mayor,reverse=False)
    return print(ordenado[:2])
    
                
mayor,nombre=maximo_impuesto_provincia(provincia)
print(nombre,mayor)
print(iva_mayor_impuestos(provincia))
ordenar_mayor(provincia)