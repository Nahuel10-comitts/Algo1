"""Solicite al usuario el ingreso de un texto.  El mismo debe contener al menos 100 palabras, de lo contrario deberá exigir al usuario que ingrese más palabras, y adicionarlas a 
las ya ingresadas hasta superar el mínimo establecido. Considere que el usuario solo ingresa palabras separadas por blancos, sin ningún otro tipo de caracteres. 
Muestre una lista de las palabras ingresadas, ordenada alfabéticamente, sin repetir palabras. """

def revisar_ingreso(lista,string):
    nueva_lista = []

    for elemento in string:
        if (elemento not in lista) and (elemento not in nueva_lista):
            nueva_lista.append(elemento)

    return nueva_lista

def main():
    lista = [] #input("Ingrese un string: ").split()
    
    while (len(lista) < 10):
        string = str(input("Ingrese mas palabras: "))

        lista.append(string) if ((string.count(" ") == 0) and string not in lista) else lista.extend(revisar_ingreso(lista,string.split()))
        
    return print(sorted(lista))

main()
        