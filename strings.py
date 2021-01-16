nome_estabelecimento= 'Pastelaria Devops'
pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Calabresa'
pastel5 = 'Carne com queijo'
pastel6 = 'Carne com frango'

print('--------')
print('')
print('Substituindo caracteres')
novo_sabor = pastel5.replace('queijo','frango')
print(novo_sabor)
print(pastel5.upper())
print(pastel5.lower())
print(pastel5.startswith('Queijo'))
print(pastel5.startswith('Carne'))
print(pastel5.endswith('frango'))
print(pastel5.endswith('queijo'))

# Transforma até a segunda palavra em maiuscula
# print(pastel5[0:2].upper())

result = 'Frango' in pastel5
print(result)