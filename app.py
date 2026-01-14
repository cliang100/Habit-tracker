from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import date

app = Flask(__name__)

def get_streak(habit_name):
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("SELECT date FROM habits WHERE habit_name = ? ORDER BY date DESC", (habit_name,))
    dates = [row[0] for row in c.fetchall()]
    conn.close()
    
    if not dates:
        return 0
    
    streak = 1
    current = date.fromisoformat(dates[0])
    
    for i in range(1, len(dates)):
        prev = date.fromisoformat(dates[i])
        if (current - prev).days == 1:
            streak += 1
            current = prev
        else:
            break
    
    return streak

def init_db():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS habits
                 (id INTEGER PRIMARY KEY,
                  habit_name TEXT, 
                  date TEXT, 
                  completed INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    habits = ['Coding', 'Gym', 'LeetCode']
    habit_data = []
    for habit in habits:
        streak = get_streak(habit)
        habit_data.append({'name': habit, 'streak': streak})
    return render_template('index.html', habits=habit_data)

@app.route('/complete/<habit_name>', methods=['POST'])
def complete(habit_name):
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    today = str(date.today())
    
    # Check if already marked complete today
    c.execute("SELECT * FROM habits WHERE habit_name = ? AND date = ?", (habit_name, today))
    if c.fetchone() is None:
        # If it wasn't done today, insert into database
        c.execute("INSERT INTO habits (habit_name, date, completed) VALUES (?, ?, 1)", (habit_name, today))
        conn.commit()
    
    conn.close()
    return redirect(url_for('home'))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)