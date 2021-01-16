pedidos_dia1 = [
    {'cliente':'Jose', 'Pastel':'Queijo'},
    {'cliente':'Jose', 'Pastel':'Queijo'},
    {'cliente':'Pedro', 'Pastel':'Carne'},
    {'cliente':'Lucas', 'Pastel':'Queijo'},
    {'cliente':'Carlos', 'Pastel':'Frango'},
]

pedidos_dia2 = [
    {'cliente':'Marcos', 'Pastel':'Pizza'},
    {'cliente':'Daniel', 'Pastel':'Queijo'},
    {'cliente':'Pedro', 'Pastel':'Carne'},
    {'cliente':'Lucas', 'Pastel':'Queijo'},
    {'cliente':'Gabriel', 'Pastel':'Frango'},
]

clientes_dia1 = set()
for pedido in pedidos_dia1:
    clientes_dia1.add(pedido['cliente'])

print(f'Dia 1: {clientes_dia1}')

clientes_dia2 = set()
for pedido in pedidos_dia2:
    clientes_dia2.add(pedido['cliente'])

print(f'Dia 2: {clientes_dia2}')

todos_clientes = clientes_dia1 | clientes_dia2
print(f'União {todos_clientes}')

clientes_comprou_todos_os_dias = clientes_dia1.intersection(clientes_dia2)
print(f'Interseção {clientes_comprou_todos_os_dias}')

clientes_diferenca = clientes_dia1 - clientes_dia2
print(f'Diferença {clientes_diferenca}')