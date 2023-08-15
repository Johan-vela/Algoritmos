from persona import Persona


class Alumno(Persona):
    codigo = ''
    facultad = ''
    año_ingreso = 0
    cursos=[]

    def __init__(self, nombre, ap_paterno, ap_materno, dni, codigo, facultad, año_ingreso):
        super().__init__(nombre, ap_paterno, ap_materno, dni)
        self.codigo = codigo
        self.facultad = facultad
        self.año_ingreso = año_ingreso
        self.cursos= []
    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_facultad(self):
        return self.facultad

    def set_facultad(self, facultad):
        self.facultad = facultad

    def get_anio_ingreso(self):
        return self.año_ingreso

    def set_anio_ingreso(self, anio):
        self.año_ingreso = anio
    
    def agregar_curso(self,curso):
        self.cursos.append(curso)
    
    def quitar_curso(self,curso):
        if curso in self.cursos:
            self.cursos.remove(curso)
        else:
            print(f'El curso {curso} no se encuentra en la lista')

    def imprimir(self):
        per_data = super().imprimir()
        codigo = self.codigo
        facultad = self.facultad
        año = self.año_ingreso
        return f'datos del alumno es : {per_data}, codigo de ingreso {codigo}, {facultad=}, el año de ingreso es: {año}'
    
