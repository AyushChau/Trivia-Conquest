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
    

    print(cur.fetchall())



@app.route('/')
def homepage():
    return render_template('home.html')



@app.route('/questions')
def question_set():
    num_of_questions = request.args.get('num_of_questions')
    category = request.args.get('category')
    
    query_db(category,num_of_questions)
    return render_template('question.html')



if __name__ == '__main__':

    app.run(host='0.0.0.0',port=3000,debug=True)