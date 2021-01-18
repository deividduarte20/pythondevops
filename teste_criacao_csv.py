import csv

file_create = open('teste.csv','w', newline='', encoding='utf-8')
escrita = csv.writer(file_create,delimiter=';')
header = ['ID', 'Nome']
escrita.writerow(header)


teste = ['1', 'Deivid']
escrita.writerow(teste)


