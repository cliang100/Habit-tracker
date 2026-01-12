from flask import Flask, render_template, request
import sqlite3
from datetime import date

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS habits
                 (id INTEGER PRIMARY KEY, date TEXT, completed INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/complete', methods=['POST'])
def complete():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    today = str(date.today())
    c.execute("INSERT INTO habits (date, completed) VALUES (?, 1)", (today,))
    conn.commit()
    conn.close()
    return "Habit marked complete for today!"

if __name__ == "__main__":
    app.run(debug=True)