"""
Escribir una funcion que devuelva verdadero si un alumno aprobó la cursada
de la materia, falso de lo contrario.
La funcion recibe dos listas: una de trabajos practicos (tps) y otra de notas.
La lista de tps puede tener tres valores: "no satisfactorio", "satisfactorio", "supera lo esperado"
La lista de notas es numerica con valores del 1 al 10. Puede tener desde una nota (si es 4 o mas) hasta
tres notas (si las dos primeras son menores a 4)


Se aprueba la cursada cuando:
- La lista tps tiene TODOS los valores con "satisfactorio" o "supera lo esperado" Y 
- la lista notas tiene por lo menos un 4 o mas.

Ademas, agrega DOS casos de prueba adicionales,en donde uno sea Falso y el otro Verdadero."""

tps_1 = ["satisfactorio", "supera lo esperado", "satisfactorio"]
tps_2 = ["satisfactorio", "no satisfactorio", "supera lo esperado", "satisfactorio"]
tps_3 = ["satisfactorio"]
notas_1 = [6]
notas_2 = [2, 8]
notas_3 = [2, 2]
tps_4 = ["satisfactorio", "supera lo esperado", "satisfactorio"]
notas_4 = [2,2,9]
tps_5 = ["satisfactorio", "supera lo esperado", "no satisfactorio"]
notas_5 = [2,2,1]

def aprobo_cursada(tps, notas):
    
    """ Casos de Prueba:
    >>> aprobo_cursada(tps_1, notas_3)
    False
    >>> aprobo_cursada(tps_2, notas_2)
    False
    >>> aprobo_cursada(tps_3, notas_1)
    True
    >>> aprobo_cursada(tps_4, notas_4)
    True
    >>> aprobo_cursada(tps_5, notas_5)
    False
    >>> aprobo_cursada(tps_3, notas_2)  
    True
    """
    #--------- Escribi el Codigo de la Funcion a partir de aqui ---------------#
    aprobo = True

    if "no satisfactorio" in tps or notas[-1] < 4:
        aprobo = False
        
    return aprobo
#------------- Bloque Principal ----------------#
import doctest
doctest.testmod(verbose = True)