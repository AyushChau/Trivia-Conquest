import sqlite3

sql_connection = sqlite3.connect('TriviaDB.db', check_same_thread=False)
cur = sql_connection.cursor()

query = "UPDATE trivia SET used = 0"
cur.execute(query)

sql_connection.commit()
sql_connection.close()
