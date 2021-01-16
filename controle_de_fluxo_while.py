print('Seja bem vindo a pastelaria Devops')
print('Faça seu pedido')


'''
0 - Estabelecimento fechado
1 - Estabelecimento aberto
'''

'''
status = 1
while status == 1:
    item_pedido = input('Qual o sabor do pastel que você deseja? ')
    print(f'Pedido confirmado')
    status=int(input('Digite 1 para aceitar novos pedidos e 0 para encerrar: '))
'''

contador = 0
quantidade_de_pedidos = 10
while contador < quantidade_de_pedidos:
    item_pedido = input('Qual o sabor do pastel que você deseja? ')
    print(f'Pedido confirmado')
    contador += 1