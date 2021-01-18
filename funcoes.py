"""
mensagem_boasvindas = 'Seja bem vindo a pastelaria DevOps'

nome_pedido1 = 'Carlos'
sabor_pedido1 = 'Frango'

nome_pedido2 = 'Pedro'
sabor_pedido2 = 'Queijo'

print(f'{nome_pedido1} pediu pastel de {sabor_pedido1}')
print(f'{nome_pedido2} pediu pastel de {sabor_pedido2}')
"""

def mensagem_boasvindas(nome):
    print(f'Seja bem vindo a pastelaria {nome}')

def add_pedidos(cliente,sabor):
    novo_pedido = f'O {cliente} pediu pastel de {sabor}'
    return novo_pedido

mensagem_boasvindas(nome='DEVOPS')
pedido1 = add_pedidos(cliente='Jose', sabor='Queijo')
print(pedido1)
pedido2 = add_pedidos('Jose','Queijo')
print(pedido2)