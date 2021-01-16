import csv

open_file = open('menu.csv','r')
file_csv = csv.reader(open_file,delimiter=';')
for [sabor, valor, status] in file_csv:
    print(f'O pastel de {sabor} custa {valor} e seu status é {status}')

open_file.close()