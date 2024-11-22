from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, *estudiantes):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = []
        for estudiante in estudiantes:
            if isinstance(estudiante, list):
                self.listadoAlumnos.extend(estudiante)
            else:
                self.listadoAlumnos.append(estudiante)

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)  
        for estudiante in lista:
            if estudiante not in self.listadoAlumnos: 
                self.listadoAlumnos.append(estudiante)

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre


class Asignatura:
    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        return f"{self._nombre} {self._salon}"
