import sqlite3

connection = sqlite3.connect("product_DB. db")
cur = connection.cursor()
print(connection)
print(cur)