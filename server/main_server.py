import sqlite3


conn = sqlite3.connect('database.db')


c = conn.cursor()


c.execute('''CREATE TABLE PANDORA ( id , version)''')


conn.commit()

conn.close()
