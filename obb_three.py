class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
    
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

# criar o objeto com parâmetros
usuario1 = Funcionarios('Helena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10;/2005')
usuario3 = Funcionarios('Andre', 'Iacono', '11/03/2003')

# print
# print(usuario1.nome)
print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))