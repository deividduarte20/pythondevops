cardapio = {}
print(type(cardapio))

pastel1 = {'sabor': 'queijo', 'valor': 6.00, 'status': True}
print(pastel1)

print(pastel1['sabor'])
print(pastel1['valor'])
print(pastel1['status'])
# print(pastel1['quantidade']) - # KeyError, chavbe não encontrada

pastel1['valor'] = 7.00
print(pastel1['valor'])

print(pastel1.get('quantidade'))
if pastel1.get('quantidade'):
    print(pastel1.get('quantidade'))
else:
    pastel1['quantidade'] = 10

print(pastel1)

keys = pastel1.keys()
print(keys)
for key in keys:
    if key == 'status':
        print(f'A chave {key} foi Encontrado no dicionario')
    else:
        print('Não encontrado')

values = pastel1.values()
print(values)
for value in values:
    print(f'O elemente {value} está no dicionário')

dict_values = pastel1.items()
print(dict_values)
for info in dict_values:
    print(f'A chave {key} possui o valor {value}')

pastel1.pop('quantidade')
print(pastel1)