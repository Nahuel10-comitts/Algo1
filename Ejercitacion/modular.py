#Escribir un programa modular que haciendo uso de listas, permita:
# 1. El ingreso de una secuencia de valores, que termina con el valor 0.
# 2. Muestre los valores ingresados.
# 3. Muestre los valores hasta encontrar el 3er. valor impar ingresado inclusive.
# 4. Muestre los elementos que se encuentren en posiciones pares.
# 5. Muestre los elementos ordenados de menor a mayor, sin repetirlos.
# En todos los casos, las salidas deben contener un título que indique lo que se está mostrando
# y mostrar un valor por línea.
def ingresarvalores():
    lista=[]
    print("Ingreso de Valores - Finalice ingresando 0", end ="\n\n")
    valor=int(input('ingresar valores:'))
    while valor!=0:
        lista.append(valor)
        valor=int(input('ingresar valores:'))
    return lista
def mostrarvalores(titulo,lista):
    print("\n",titulo)
    for elemento in lista:
        print("\t",elemento)
def mostrarhasta3impar(lista):
    contador=0
    listamostrar=[]
    i=0
    while contador<=2 :
        if lista[i]%2==1:
            contador+=1
        listamostrar.append(lista[i])
        i+=1
    return(listamostrar)
def mostrarpares(lista):
    listamostrar=[]
    for elemento in range(0,len(lista),2):
        listamostrar.append(lista[elemento])
    return(listamostrar)
def mostrarordenado(lista):
    listamostrar=[]
    for elemento in range (0,len(lista)):
        if lista[elemento] not in listamostrar:
            listamostrar.append(lista[elemento])
    listamostrar.sort()
    return(listamostrar)
lista=ingresarvalores()
mostrarvalores('elementos ingresados:',lista)
listaimpares=(mostrarhasta3impar(lista))
mostrarvalores('hasta 3 impares',listaimpares)
listapares=(mostrarpares(lista))
mostrarvalores('muestro pares',listapares)
listaordenada=(mostrarordenado(lista))
mostrarvalores('listaordenado',listaordenada)
        
    
    
        
    
#esta es una nueva linea