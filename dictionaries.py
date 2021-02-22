# Dicionários
    # Utiliza index no formato de keys e values
    # Aceita string, integer, float, boolean...

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'Aprovação': True}

# aluno['nome'] = 'Jose'
# print(aluno)


# aluno.update({'nome': 'Jose', 'nota_final': 'B'})
# aluno.update({'endereco': 'Rua A'}) # Caso não exista informação esse comando insere

del aluno['idade'] # Remove dado do dicionário
print(aluno)

#print(aluno.get('endereco', 'O valor não existe')) # Se caso não existe retorna none e segue sem erro