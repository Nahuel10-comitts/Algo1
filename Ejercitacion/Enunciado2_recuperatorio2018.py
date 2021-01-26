"""2) Solicite al usuario el ingreso de un texto. Considerar que el usuario solo ingresa palabras separadas por blancos, sin ningún otro tipo de caracteres. Si el usuario ingresó 
menos de 100 palabras se debe pedir que siga ingresando hasta completar o superar dicha cantidad. De las palabras ingresadas, descartar las que empiezan con “ab” y las que empiezan 
con “pseudo”. Mostrar una lista ordenada alfabéticamente de las palabras que quedaron.""" 

def imprimir_palabras():
    texto = input("Ingresar palabras separadas por blancos: ").split()
    cant_palabras = len(texto)
    
    while cant_palabras < 10:

        if "ab" in texto[0]:
            texto.pop("ab")

        elif "pseudo" in texto[0]:
            texto.pop("pseudo")

        ingreso = input("Faltan palabras, siga ingresando: ").split()

        if "ab" in ingreso[0]:
            ingreso.pop("ab")

        elif "pseudo" in ingreso[0]:
            ingreso.pop("pseudo")

        cant_palabras += len(ingreso)

        for palabra in ingreso:
            texto.append(palabra)

    texto.sort()
    print(texto)
           

 

def main():  
    imprimir_palabras()
main()