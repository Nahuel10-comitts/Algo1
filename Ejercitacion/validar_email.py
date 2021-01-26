"""Escribir una función que reciba una cadena de caracteres que representa una
dirección de mail. La función debera devolver True ó False, en función de
haber evaluado que dicha dirección está bien formada.
Se debe controla que:
 a. Que no contenga blancos
 b. Que sólo se utilicen letras y/o números para la parte del nombre, delante
 de la @
 c. Que haya exactamente una @
 d. Que los nombres de dominio sean: fi.uba.ar ó gmail.com """
 
def validar_email(email):
    if " " in email:
        devolver = False
    elif email.count("@") != 1:
        devolver = False
    elif not (email[:email.index("@")].isalnum()):
        devolver = False
    elif not (email[email.index("@"):] != "fi.uba.ar" and email[email.index("@"):] != "gmail.com"):
        devolver = False
    else:
        devolver = True
    return devolver
#---------------------------------------- Bloque Principal -----------------------------------------#
cadena = input("Ingrese su email: ")
print("Email Valido" if validar_email(cadena) else "Email Invalido")

#Magia, agrege un nuevo comentario
#Magia, nuevo comentario agregado