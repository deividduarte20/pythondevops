import csv

file = open('materiais.csv','w',newline='', encoding='utf-8')
write = csv.writer(file, delimiter=';')
header = ['ID', 'Descricao', 'Status']
write.writerow(header)

materiais1 = ['01', 'Mouse', 'Disponível']
write.writerow(materiais1)

materiais2 = ['02', 'Webcam', 'Indisponível']
write.writerow(materiais2)

file.close()