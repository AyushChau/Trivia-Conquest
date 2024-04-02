import pandas as pd
import sqlite3

sql_connection = sqlite3.connect('TriviaDB.db', check_same_thread=False)
cur = sql_connection.cursor()

df = pd.read_sql_query("SELECT * from trivia",sql_connection)

print(df)

