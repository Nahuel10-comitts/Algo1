# Escribir un programa en Python que solicite las medidas de los 3 lados de un triangulo
# e imprima por pantalla si el triangulo es equilatero (3 lados iguales), isosceles
# (2 lados iguales) o escaleno (3 lados distintos).
lado1 = int(input("Ingrese el primer lado del triangulo: "))
lado2 = int(input("Ingrese el segundo lado del triangulo: "))
lado3 = int(input("Ingrese el tercer lado del triangulo: "))
if (lado1 == lado2 == lado3):
    print("El triangulo es equilatero")
elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print("El triangulo es isosceles")
else: #lado1 != lado2 != lado3
    print("El triangulo es escaleno")
    