file = open('pedidos.txt')
pedidos = file.readlines()
for pedido in pedidos:
    print(pedido.replace('\n',''))