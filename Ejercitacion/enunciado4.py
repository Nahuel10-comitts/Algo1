"""
Escribir una funcion para validar una nueva clave de acceso.
La funcion deber recibir una cadena de caracteres, que contendra la clave
candidata, que fue ingresada por el usuario; y devolvera True o False,
dependiendo de si cumple con las condiciones establecidas.

La clave debe:
- Tener una longitud total de entre 4 y 10 caracteres
- Estar formada por igual cantidad de caracteres numericos y caracteres
  alfabeticos, y no puede contener ningun otro caracter.
- Los caracteres alfabeticos y numericos deben estar intercalados, no pueden
  haber dos letras consecutivas, ni dos digitos numericos consecutivos."""



def validar_acceso(clave):
    """ Casos de Prueba:
 
    >>> validar_acceso("asd")
    False
    >>> validar_acceso("hola")
    False
    >>> validar_acceso("a1a1d")
    False
    >>> validar_acceso("aa5j")
    False
    >>> validar_acceso("a11s")
    False
    >>> validar_acceso("j5d4")
    True
    >>> validar_acceso("5j6g3d")
    True
    >>> validar_acceso("a5f8b9l0p1")
    True
    """
    posicion = 0
    contcaracter = 0
    contnumeros = 0
    devolver = True
    
    if len(clave)%2 != 0 or 4> len(clave) >10 or clave.isalnum() == False:
        devolver = False
    else:
        while (posicion < len(clave)-1) and devolver:
            if posicion == len(clave)-1:
                if clave[posicion].isalpha() == True:
                    contcaracter += 1
                else:
                    contnumeros += 1
            elif (clave[posicion].isalpha() == True) and (clave[posicion+1].isalpha() == False):
                contcaracter += 1
            elif (clave[posicion].isdigit() == True) and (clave[posicion+1].isdigit() == False):
                contnumeros += 1
            else:
                devolver = False
            posicion += 1
    
    if contcaracter == contnumeros and contcaracter+contnumeros == len(clave):
        devolver = True        
    
    return devolver

# import doctest
# doctest.testmod()             
# print(validar_acceso("a11s"))
# print(validar_acceso("a5f8b9l0p1"))
print(validar_acceso("j5d4"))
