import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

select = 'select * from produtos where id =1'
cursor.execute(select)
result = cursor.fetchone()
print(result)


update = 'update produtos set nome = ? where id = ?'
novos_valores = ('Bacon com chedar', 1)
cursor.execute(update, novos_valores)
connection.commit()

print(f'Feito')
# print(result, len(result), type(result))

# result = cursor.fetchmany(2)
# print(result, len(result), type(result))

# result = cursor.fetchall()
# print(result, len(result), type(result))