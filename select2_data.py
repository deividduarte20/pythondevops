import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

select = 'select * from produtos where id=5'
cursor.execute(select)
result = cursor.fetchone()
# print(result)

delete = 'delete from produtos where id = ?'
cursor.execute(delete, '4')
connection.commit()
connection.close()
