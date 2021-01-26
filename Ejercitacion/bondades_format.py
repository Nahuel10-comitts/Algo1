empleados = [ [80, "Juan Carlos Rodríguez", 9720.35],
 [178, "Rosa Rojo", 19520.85],
 [1024, "Pedro Pablo Carmona González", 29255.70]
 ] 
print("{:-^42}".format("LISTADO DE EMPLEADOS"))
print()
print("{:<8} {:<24} {:^8}".format("Legajo", "Nombre y Apellido",
"Sueldo"))
print()
for emp in empleados:
 print("{:<8d} {:<24.22} {:8.2f}".format(emp[0], emp[1], emp[2]))
input("Ingrese enter...")