def area_triangulo(base, altura): # Parametros formales
    area = (base * altura) / 2
    return area
b = int(input("Ingrese la base del triangulo: "))
h = int(input("Ingrese la altura del triangulo: "))
print(area_triangulo(b, h)) # Parametros actuales