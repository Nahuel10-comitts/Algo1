def leer_info(ejs, default):
   linea = ejs.readline()
   return linea.rstrip().split(',') if linea else default.split(',')

def correo_aprobados(aprobados, correo, nombre, nota):
    pass # implementar

def correo_reprobados(reprobados, correo, nombre, nota):
    pass # implementar

max = "999999"
ultimo_parcial = max+",0"
ultimo_bd = max+",,,"

parcial1 = open("parcial1.csv", "rt")
bd = open("7540_1C2020.csv", "rt")
notas = open("7540_1C2020_parcial1.csv", "wt")
aprobados = open("aprobados.txt", "wt")
reprobados = open("reprobados.txt", "wt")

padron_p1, nota = leer_info(parcial1, ultimo_parcial)
padron_bd, apellido, nombre, correo = leer_info(bd, ultimo_bd)

while padron_p1 != max and padron_bd != max:
    
    if padron_p1 == padron_bd:
        notas.write("{}, {} {}, {}", padron_p1, apellido, nombre, nota)
        if nota >= 4:
            correo_aprobado(aprobados, correo, nombre, nota)
        else:
            correo_reprobado(reprobados, correo, nombre, nota)
        padron_p1, nota = leer_info(parcial1, ultimo_parcial)
        padron_bd, apellido, nombre, correo = leer_info(bd, ultimo_bd)
    elif padron_p1 > padron_bd:
        padron_bd, apellido, nombre, correo = leer_info(bd, ultimo_bd)
    

parcial1.close()
bd.close()
notas.close()
aprobados.close()
reprobados.close()