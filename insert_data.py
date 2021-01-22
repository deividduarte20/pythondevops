import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

dados = [
    ('Queijo', 6.00),
    ('Frango', 6.00),
    ('Pizza', 6.00),
    ('Calabresa', 6.00),
    ('Carne', 6.00),
]

cursor.executemany('INSERT INTO PRODUTOS (nome,preco) values (?,?)', dados)
connection.commit()
connection.close()