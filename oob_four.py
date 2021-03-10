from datetime import datetime

# Python Object-Oriented Programming

# Classes
    # Utilizadas para criar objetos (instances)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes são utilizadas para agrupar dados e funções,
    # podendo reutilizar

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    
    def nome_completo(self):
        return (self.nome + ' ' + self.sobrenome)
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

# criar o objeto com parâmetros
usuario1 = Funcionarios('Helena', 'Cabral', 2009)
usuario2 = Funcionarios('Carol', 'Silva', 2005)
usuario3 = Funcionarios('Andre', 'Iacono', 2003)

# print
print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))
print(Funcionarios.idade_funcionario(usuario3))