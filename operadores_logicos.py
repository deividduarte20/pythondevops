nome_estabelecimento= 'Pastelaria Devops'
pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Calabresa'
status = True
valor_pastel1 = 6.0
valor_pastel2 = 6.0
valor_pastel3 = 6
valor_pastel4 = 6
print(nome_estabelecimento)
print(pastel1, valor_pastel1, status)
print(pastel2, valor_pastel2, status)
print(pastel3, valor_pastel3, status)
print(pastel4, valor_pastel4, status)

print('-------')
print('')

pagamento_pedido1_cartao = True
pagamento_pedido2_cartao = True
print('Precisa levar a máquina de cartão: ',pagamento_pedido1_cartao and pagamento_pedido2_cartao)

pagamento_pedido1_cartao = True
pagamento_pedido2_cartao = True
print('Precisa levar a máquina de cartão: ',pagamento_pedido1_cartao or pagamento_pedido2_cartao)

pagamento_pedido1_cartao = False
pagamento_pedido2_cartao = False
print('Precisa levar a máquina de cartão: ',pagamento_pedido1_cartao or pagamento_pedido2_cartao)
pagamento_pedido1_cartao = False