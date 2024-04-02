import sqlite3


sql_connection = sqlite3.connect('TriviaDB.db', check_same_thread=False)
cur = sql_connection.cursor()

cur.execute("DROP TABLE IF EXISTS trivia")
cur.execute("CREATE TABLE trivia(id INTEGER PRIMARY KEY,question VARCHAR(1000) UNIQUE COLLATE NOCASE,answer VARCHAR(100), category VARCHAR(100), used BOOLEAN)")