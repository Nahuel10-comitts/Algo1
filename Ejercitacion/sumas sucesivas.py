suma = 0
num1 = int(input("Ingrese un primer numero entero: "))
num2 = int(input("Ingrese un segundo numero entero: "))
if num1>num2:
   for i in range(1, num2+1):
     suma += num1
print(suma)
