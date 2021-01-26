# import sys
# sys.setrecursionlimit(10**6) # Evita RecursionError: maximum recursion depth exceeded
#Ejercicio
"""La facultad nos solicita que implementemos una clase que modele
a los distintos cursos que existen. El curso debe poder, a través de
sus métodos: configurar un nombre, ingresar un alumno con su
nota conjuntamente, devolver la cantidad de alumnos, preguntar si
un alumno está en el curso y permitir preguntar por la nota de un
alumno.
Pista: Los métodos están bien definidos. Pensar en él/los atributos
que debe tener nuestro objeto."""
# Continuacion
""" Se nos solicita que distingamos entre cursos del departamento de
computación y cursos del departamento de matemática.
Para esto, se debe dividir la clase Curso en dos clases distintas.
Una vez divididas, se debe implementar el método con la siguiente
firma:
def esta_aprobado(alumno):
Si el curso es de computación, el alumno aprueba si tiene promedio
mayor o igual a 6. Si es de matemática, con promedio 4 está aprobado."""
class Curso_Computacion:
    cantidad_de_cursos = 0

    def __init__(self, nombre_titular, nombre_JTP):
        self.nombre_titular = nombre_titular
        self.nombre_JTP = nombre_JTP
        self.alumnos = {}
        Curso_Matematica.cantidad_de_cursos += 1

    def titulares_catedra(self):
        return self.nombre_titular, self.nombre_JTP
    
    def esta_aprobado(self, alumno):
        return self.nota_del_alumno(alumno) >= 6 #Aca es donde jode

    def configurar_nombre(self, nombre):
        self.nombre = nombre

    def ingresar_alumno_con_nota(self, nombre_alumno, nota):
        self.alumnos[nombre_alumno] = nota

    def cantidad_de_alumnos(self):
        return len(self.alumnos)

    def alumno_esta_en_curso(self, alumno):
        return alumno in self.alumnos

    def nota_del_alumno(self, alumno):
        if self.alumno_esta_en_curso(alumno):
            return self.alumnos[alumno]
        else:
            raise Exception ("El alumno no se encuentra en el curso")
    
    def cantidad_de_cursos_registrados(self):
        return Curso_Matematica.cantidad_de_cursos

class Curso_Matematica:
    cantidad_de_cursos = 0

    def __init__(self, nombre_titular, nombre_JTP):
        self.nombre_titular = nombre_titular
        self.nombre_JTP = nombre_JTP
        self.alumnos = {}
        Curso_Computacion.cantidad_de_cursos += 1

    def titulares_catedra(self):
        return self.nombre_titular, self.nombre_JTP
    
    def esta_aprobado(self, alumno):
        return self.nota_del_alumno(alumno) >= 4

    def configurar_nombre(self, nombre):
        self.nombre = nombre

    def ingresar_alumno_con_nota(self, nombre_alumno, nota):
        self.alumnos[nombre_alumno] = nota

    def cantidad_de_alumnos(self):
        return len(self.alumnos)

    def alumno_esta_en_curso(self, alumno):
        return alumno in self.alumnos

    def nota_del_alumno(self, alumno):
        if self.alumno_esta_en_curso(alumno):
            return self.alumnos[alumno]
        else:
            raise Exception ("El alumno no se encuentra en el curso")
    
    def cantidad_de_cursos_registrados(self):
        return Curso_Computacion.cantidad_de_cursos
    

curso_de_Pablo = Curso_Computacion("Guarna", "Juarez")
# curso_de_Pablo.configurar_nombre("Guarna-AlgoI")
print(curso_de_Pablo.cantidad_de_alumnos())

# curso_de_Pablo.ingresar_alumno_con_nota("Nahuel", 10)
# curso_de_Pablo.ingresar_alumno_con_nota("Uriel", 4)
# curso_de_Pablo.ingresar_alumno_con_nota("Matias", 8)
curso_de_Pablo.ingresar_alumno_con_nota("Zoe", 7)

# print(curso_de_Pablo.alumno_esta_en_curso("Nahuel"))
# print(curso_de_Pablo.alumno_esta_en_curso("Tomas"))

print("Cantidad de alumnos: ", curso_de_Pablo.cantidad_de_alumnos())

# print(curso_de_Pablo.nota_del_alumno("Nahuel"))

curso_de_Andy = Curso_Matematica("Juarez", "Perez")

curso_de_Andy.ingresar_alumno_con_nota("Zoe", 5)

print(curso_de_Andy.cantidad_de_alumnos())
print(curso_de_Andy.cantidad_de_cursos_registrados())

cursos_de_Zoe = [curso_de_Pablo, curso_de_Andy]

cursos_aprobados = 0

for curso in cursos_de_Zoe:
    if curso.esta_aprobado("Zoe"):
        cursos_aprobados += 1

print("Zoe aprobó {} cursadas".format(cursos_aprobados))
