pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Calabresa'

cardapio = ['Carne', 'Queijo', 'Frango', 'Calabresa']
print(cardapio)

print(f'Tamanho da lista é de {len(cardapio)}')

print(f'Acessando o primeiro indice da lista: {cardapio[0]}')
print(f'Acessando o terceiro indice da lista: {cardapio[2]}')

print(f'Acessando o ultimo indice da lista: {cardapio[-1]}')
print(f'Acessando o penultimo indice da lista: {cardapio[-2]}')

# Queijo = Mussarela

cardapio[1] = 'Mussarela'
print(cardapio)

print('-------')

novo_cardapio = []
print(len(novo_cardapio))
print(type(cardapio))

print('')
print('Adicionando elementos na lista')
novo_cardapio.append('Carne')
novo_cardapio.append('Queijo')
novo_cardapio.append('Frango')
novo_cardapio.append('Calabresa')
print(novo_cardapio)

print('-------')
print('')
print('Acessando trechos da lista')

print(novo_cardapio[1:3])
print(novo_cardapio[2:])
print(novo_cardapio[:3])

print('-------')
print('')
print('Organizando uma lista em ordem alfabetica')
print(novo_cardapio)
print(sorted(novo_cardapio, key=str.lower))

print(novo_cardapio.remove('Calabresa'))
print(novo_cardapio)

print('')
novo_cardapio.remove('Queijo')
print(novo_cardapio)

print('')
novo_cardapio.append('Frango')
novo_cardapio.append('Frango')
print(novo_cardapio)

print(novo_cardapio.count('Frango'))

novo_cardapio.insert(0,'Palmito')
novo_cardapio.insert(2,'Pizza')
print(novo_cardapio)

print(novo_cardapio.pop(4))
print(novo_cardapio)

print(novo_cardapio.pop())
print(novo_cardapio)

del novo_cardapio[:3]
print(novo_cardapio)

print('-----')
vendas = []
vendas.append(12.00)
vendas.append(16.00)
vendas.append(24.00)
print(vendas)
print(sum(vendas))
print(max(vendas))
print(min(vendas))
print(f'{sum(vendas)/len(vendas):.2f}')

numeros = list(range(1,101))
print(numeros)
print(len(numeros))
del numeros[:10]
del numeros[:10]
print(numeros)