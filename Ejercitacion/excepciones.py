# NameError: name 'c' is not defined
# ZeroDivisionError: division by zero
# IndexError: list index out of range
# SyntaxError: invalid syntax
# ValueError: invalid literal for int() with base 10: 'j'

# Lanzar una excepción (raise, throw)

f()

x = None
while x == None:
    try:
        x = int(input("Ingrese un num: "))
        print("El inverso de x es {0}".format(1/x))
        f()
    except ValueError as err:
        print("Ups! Eso no es un número! Detalles: {0}"
              .format(err))
    except ZeroDivisionError:
        print("No puedo dividir por cero...")
    except:
        print("Algo salió mal")
    else:
        # Se ejecuta solo en caso de no ejecuta ningún except
        print("Gracias, salió todo de 10")
    finally:
        # Se ejecuta después de cualquier except o el else
        print("Limpieza")
        x = None
print(x)