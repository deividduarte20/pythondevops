import csv

create_file = open('pedidos.csv', 'w', newline='', encoding='utf-8')
write = csv.writer(create_file,delimiter=';')
header = ['ID', 'Cliente', 'Valor total']
write.writerow(header)

pedido1 = ['01', 'Jose', '24.00']
write.writerow(pedido1)
pedido2 = ['02', 'Carlos', '30.00']
write.writerow(pedido2)
pedido3 = ['03', 'Lucas', '47.00']
write.writerow(pedido3)

create_file.close()