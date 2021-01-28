# from calculadora import Calculadora

# objeto = Calculadora(18, 10)
# objeto.soma()

class Curso:

    def __init__(self, curso, professor):
        self.curso = curso
        self.professor = professor
        
cursos = Curso('Curso de Python', 'Deivid')
print(cursos.curso)
print(cursos.professor)