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

# SOMA

pedido1 = valor_pastel1 + valor_pastel2
print('Valor total pedido1: ', pedido1, type(pedido1))

pedido2 = valor_pastel1 + valor_pastel3
print('Valor do pedido2: ', pedido2, type(pedido2))

# Subtracao

custo = 3.0
subtracao1 = pedido1 - custo
print('Exemplo 1 subtração: ', subtracao1)

# Divisao

ticket_medio = (pedido1 + pedido2)/2
print('O ticket médio é: ', ticket_medio)

# Multiplicacao

dias_mes = 22
faturamento = ticket_medio * 22
print('Previsão de faturamento: ', faturamento)