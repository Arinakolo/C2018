import sqlite3

connection = sqlite3.connect("product_DB.db", 5)
cur = connection.cursor()

#cur.execute("CREATE TABLE products (title TEXT, price TEXT, count Integer);")

#cur.execute("INSERT INTO products (title, price, count") VALUES ("Adidas", "55.40", 12)")
#cur.execute("INSERT INTO products (title, price, count") VALUES ("Puma", "53.40", 17)")


connection.commit()

cur.execute(("SELECT * FROM products WHERE title IS 'Adidas' "))
for row in cur:
    print(row)


connection.close()