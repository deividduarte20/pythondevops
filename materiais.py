# Copiado do arquivo for.py

print('Loja de materiais de informática')
print('----------------------------------')
print('')

materiais = ['Teclado', 'Mouse', 'Pen Drive', 'Notebook']

for indice,materials in enumerate(materiais):
    print(f'[{indice}]: {materials}')

produto = int(input('Digite o número correspondente ao material desejado: '))
if produto >= 0 and produto <= len(materiais):
    print(f'O produto escolhido é {materiais[produto]}')
else:
    print(f'Produto inválido')


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