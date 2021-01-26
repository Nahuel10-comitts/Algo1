# Escribir un programa en python que solicite el ingreso de una temperatura en grados
# Celsius e imprima por pantalla sus equivalentes temperatura en Kevin y grados Farenheit.
temp_Celsius = float(input("Ingrese temperatura en grados Celsius: "))
temp_Kelvin = temp_Celsius + 273
print("La temperatura en Kelvin es: ", temp_Kelvin)
temp_Farenheit = temp_Celsius * 9/5 + 32
print("La temperatura en grados Farenheit es: ", temp_Farenheit)

