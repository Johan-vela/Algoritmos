from alumno import Alumno
from docente import Docente
from curso import Curso

lista_alumnos =[]
alumno1 = Alumno('Juan', 'Ruiz', 'Guerra', '01234567','00202018', 'Informatica y Sistemas', 2023)
alumno2 = Alumno('Ana', 'Perez', 'Quirón', '45698231','00202112', 'Informatica y Sistemas', 2020,)
alumno3 = Alumno('Eduardo', 'Ramirez', 'Hernandez', '48751236','00201914', 'Informatica y Sistemas', 2021)

lista_alumnos.append(alumno1)
lista_alumnos.append(alumno2)
lista_alumnos.append(alumno3)

lista_docentes=[]
docente1= Docente('Alberto', 'Huamán', 'Mariátegui', '78569203','0020154','FIIS')
docente2= Docente(' Rocío', 'Guevara', 'Sanchez', '45612300','00201415','FIIS')

lista_docentes.append(docente1)
lista_docentes.append(docente2)

lista_cursos=[]
curso1 = Curso("C001", "Matemáticas Básica")
curso2 = Curso("C002", "Estadística")
curso3 = Curso("C003", "Matemática II")
curso4 = Curso("C004", "Física I")

lista_cursos.append(curso1)
lista_cursos.append(curso2)
lista_cursos.append(curso3)
lista_cursos.append(curso4)

band = 0
for curso in lista_cursos:
    if band<2:
        curso.asignar_docente(docente1)
    else:
        curso.asignar_docente(docente2)
    band+=1
    
for alumno in lista_alumnos:
    for curso in lista_cursos:
        alumno.agregar_curso(curso)
        
# Mostrar los cursos asignados a un alumno (alumno 2)
alumno2_cursos = alumno2.cursos
print(f"Cursos asignados al alumno/a {alumno2.get_nombre()}:")
for curso in alumno2_cursos:
    print(curso.get_nombre())

# Ingresar notas para todos los cursos de un alumno (alumno 2) ingresados por el usuario
for curso in alumno2_cursos:
    notas_curso = []

    # Solicitamos al usuario ingresar las notas para el curso actual
    for i in range(4):
        nota = float(input(f"Ingrese la nota {i + 1} para el alumno {alumno2.get_nombre()} en el curso {curso.get_nombre()}: \n"))
        notas_curso.append(nota)

    # Agregamos las notas al curso
    curso.ingresar_notas(notas_curso)

# Calculamos y mostramos el promedio de cada curso para el alumno 2
print(f"Promedios de notas para el alumno {alumno2.get_nombre()}:")
for curso in alumno2_cursos:
    promedio_curso = curso.calcularPromedio(curso.notas)
    print(f"Promedio en el curso {curso.get_nombre()}: {promedio_curso:.2f}")