import sqlite3
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("