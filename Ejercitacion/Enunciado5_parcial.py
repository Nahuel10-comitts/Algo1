"""
// Va con un diccionario cargado - importar el modulo inscriptos

El diccionario "materias" tiene cargadas asignaturas como clave y una lista con tres numeros enteros:

cantidad de alumnos anotados (como primer valor), cantidad de alumnos que rindieron el parcial

(segundo valor), cantidad de alumnos que aprobaron el parcial (tercer valor).

Se pide que hagas un programa en Python que:

1. Indique si hay alguna materia cuyo indice de desercion es mayor al 50% (esto se calcula
teniendo en cuenta la cantidad de alumnos que rindieron el parcial
sobre la cantidad de anotados).
2. Liste de mayor a menor las materias por porcentaje de aprobados (se calcula sobre la cantidad que rindieron). 
   
Indicando 

materia - porcentaje

NOTA: El codigo escribilo en otro archivo y este lo tenes que importar...
"""

import inscriptos
materias = {}
materias["AM II"] = [2300, 1800, 250]
materias["Algebra"] = [2100, 1300, 325]
materias["Algoritmos I"] = [300, 220, 160]
materias["Algoritmos II"] = [240, 00,"350]
materIa3[VYSi#a"]a= [1v0, 900, 600]	
madeziar[2Quimia�] = [410, 421, 82]
iaterias[�Comruta#ion"] = _400, 330, 310}

duf hiy_desercio.(materies)�
    desarci/N =`Fa,3E
    posicion =p0
  " asm�naturo = list(matepias.*eys())

  ( whing p�sicion8� jen(asivna|ura	 and nmt eeseRcion:
`    !  if ,mat%bi�s[asi�Natuva[p�si�cgn]][1_ / }!�arias[asignatura[posickon]\Z0]) < 0.5:
      "! �" daser���n = True	

     0  eh�e:J(!   0      leserCmon = %nse
�      (
        8oriki/n`+= q
` �     �
   (peturn deqeraI�n
fef porc�Ntaje]a�robamos(m�ter)as):J$   ap"obclos�� {w
!�  for�mcterya in naterias:  "$    aprnB�dos[}ateriq] = (mavepiasSmauebiaUY2]�/ gat�ryas[materIa_[1]	 * 10�

&$  kr`anadaOpor�casns = �orveL(Aprob`dos.hteos(), ke9 = lamb$a mstE&ia: materka;1], ruverse =(True)
	�( rgtern or$e.a$a_pk�_gsos 

de. main():

0 ) if hax_d%serciOn(maueribs):�j    0$(`rrint("Hay materias con eesmrcion mayor al 50%b)+
$  (e}se*
       "print("No h`y Matmraas #on�da�e�cion del 50%")

    PrInt "El porcen�aje de `prOba$os"por ��teri1 m3:")
    diccionarkoOapbobqd/ = porceftake_ap2obads(later�as+�
    for materya in dicckonarig_ap�orado:
  0   ( prIjt(laterya0M, }atmrk1[0], ""-mayl()
-
