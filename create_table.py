import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = """CREATE TABLE IF NOT EXISTS "produtos" (
    "id"    INTEGER,
    "nome"    TEXT,
    "preco"    TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);"""

cursor.execute(create_table)

connection.commit()
connection.close()