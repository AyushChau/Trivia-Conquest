from flask import Flask, redirect, request, jsonify, session, render_template
import requests
import sqlite3

app = Flask(__name__)

sql_connection = sqlite3.connect('TriviaDB.db', check_same_thread=False)
cur = sql_connection.cursor()

def query_db(category,num_of_questions):
    
    if category != 'Random':
        print(category)
        query = "SELECT question,answer from trivia where category = ? AND used == 0 ORDER BY RANDOM() Limit ?"
        cur.execute(query, (category,num_of_questions))
    else:
        query = "Select question,answer from trivia where used == 0 ORDER BY RANDOM() Limit ?"
        cur.execute(query, (num_of_questions,))

    selected_qs = cur.fetchall()

    for row in selected_qs:
        q = row[0]
        a = row[1]

        query = "UPDATE trivia SET used = 1 WHERE question = ? AND answer = ?"
        cur.execute(query,(q,a))
        sql_connection.commit()

    return dict(selected_qs)

@app.route('/')
def homepage():
    query = "SELECT count(*) from trivia where used == 0"
    cur.execute(query)
    question_count = cur.fetchone()[0]
    return render_template('home.html',count=question_count)



@app.route('/questions')
def question_set():
    num_of_questions = request.args.get('num_of_questions')
    category = request.args.get('category')
    
    questions = query_db(category,num_of_questions)
    return render_template('question.html',table=questions)



if __name__ == '__main__':

    app.run(host='0.0.0.0',port=3000,debug=True)
    sql_connection.close()