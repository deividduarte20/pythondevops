import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

select = 'select * from produtos'
cursor.execute(select)
# result = cursor.fetchone()
# print(result, len(result), type(result))

result = cursor.fetchmany(2)
print(result, len(result), type(result))

# result = cursor.fetchall()
# print(result, len(result), type(result))