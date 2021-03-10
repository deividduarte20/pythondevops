# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar objetos (instances)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes são utilizadas para agrupar dados e funções,
    # podendo reutilizar
    # ===
    # Class: Frutas
    # Objects: Abacate, Banana...

# criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

# criar o objeto com parâmetros
usuario1 = Funcionarios('Helena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10;/2005')

# print
print(usuario1.nome)
print(usuario2.data_nascimento)
# print
print(usuario1.nome)
print(usuario2.data_nascimento)


# criar os parametros do usuario1
# usuario1.nome = 'Helena'
# usuario1.sobrenome = 'Cabral'
# usuario1.data_nascimento = '12/01/2009'

# criar os parametros do usuario1
# usuario2.nome = 'Carol'
# usuario2.sobrenome = 'Silva'
# usuario2.data_nascimento = '15/10/2005'


