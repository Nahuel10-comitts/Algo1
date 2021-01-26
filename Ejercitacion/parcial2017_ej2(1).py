"""2)Solicite al usuario el ingreso de un texto.  El mismo debe contener al menos 100 palabras, de lo contrario deberá exigir al usuario que ingrese más palabras, y adicionarlas a 
las ya ingresadas hasta superar el mínimo establecido. Considere que el usuario solo ingresa palabras separadas por blancos, sin ningún otro tipo de caracteres. 
Muestre una lista de las palabras ingresadas, ordenada alfabéticamente, sin repetir palabras. """
def imprimir_palabras():
    texto = ""
    texto = input("ingrese su texto: ")
    texto = texto.split(" ")
    cant_palabras = len(texto)
    while cant_palabras < 10:
        ingreso = input("ingrese su texto: ").split(" ")
        cant_palabras += len(ingreso)
        for palabra in ingreso:
            texto.append(palabra)
    texto = sorted(texto)
    print(texto)
    
imprimir_palabras()
