import sqlite3


def question_answer_seperate(curr_category):

    with open("QuestionFiles/Numbers.txt", encoding='utf-8') as file, open("QuestionFiles/NumbersAnswers.txt", encoding='utf-8') as file2:
        questions = [line.strip() for line in file if line.strip()]
        answers = [line.strip() for line in file2 if line.strip()]

        for question,answer in zip(questions,answers):
            insert_query = "INSERT INTO trivia (question, answer, category, used) VALUES (?, ?, ?, ?)"
            values = (question,answer,curr_category,0)
            cur.execute(insert_query, values)

def one_file(curr_category):

    with open("QuestionFiles/Religion.txt") as file:
        items = [line.strip() for line in file if line.strip()]

        questions = items[::2]
        answers = items[1::2]
        questions = [question.split('. ')[-1] for question in questions]
        answers = [answer.split(': ')[-1] for answer in answers]
        for question,answer in zip(questions,answers):
            insert_query = "INSERT INTO trivia (question, answer, category, used) VALUES (?, ?, ?, ?)"
            values = (question,answer,curr_category,0)
            cur.execute(insert_query, values)

sql_connection = sqlite3.connect('TriviaDB.db', check_same_thread=False)
cur = sql_connection.cursor()

curr_category = 'Religion & Myths'

#question_answer_seperate(curr_category)
one_file(curr_category)



sql_connection.commit()
sql_connection.close()