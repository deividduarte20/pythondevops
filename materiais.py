# Copiado do arquivo for.py

# cardapio = ['Carne', 'Queijo', 'Frango', 'Calabresa', 'Pizza', 'Carne Seca']

print('Loja de materiais de informática')
print('----------------------------------')
print('')

materiais = ['Teclado', 'Mouse', 'Pen Drive', 'Notebook']

for indice,materials in enumerate(materiais):
    print(f'[{indice}]: {materials}')


'''
print(cardapio[0])
print(cardapio[1])
print(cardapio[2])
'''

'''
print('Pastelaria Devops')
print('Veja o nosso cardapio')
print('----------------------')
for indice, recheio in enumerate(cardapio):
    # print(indice, recheio)
    print(f'[{indice}]: {recheio}')

opcao = int(input('Digite o número correspondente ao sabor desejado: '))
if opcao >= 0 and opcao <= len(cardapio):
    print(f'O sabor escolhido foi {cardapio[opcao]}')
else:
    print(f'Opção inválida')
'''