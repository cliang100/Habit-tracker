from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import date, timedelta

app = Flask(__name__)

def get_streak(habit_name):
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("SELECT date FROM habits WHERE habit_name = ? ORDER BY date DESC", (habit_name,))
    dates = [row[0] for row in c.fetchall()]
    conn.close()
    
    if not dates:
        return 0
    
    today = date.today()
    most_recent = date.fromisoformat(dates[0])
    
    # If most recent is more than 1 day ago, streak is broken
    if (today - most_recent).days > 1:
        return 0
    
    streak = 1
    current = most_recent
    
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

def init_competency_db():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS competency_hours
                 (id INTEGER PRIMARY KEY,
                  date TEXT,
                  hours REAL,
                  source TEXT)''')
    conn.commit()
    conn.close()

def init_habit_time_db():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS habit_time
                 (id INTEGER PRIMARY KEY,
                  habit_name TEXT,
                  date TEXT,
                  minutes INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("SELECT habit_name FROM habits_list")
    habits = [row[0] for row in c.fetchall()]
    
    # Get total competency hours
    c.execute("SELECT SUM(hours) FROM competency_hours")
    total_hours = c.fetchone()[0] or 0
    
    conn.close()
    
    habit_data = []
    for habit in habits:
        streak = get_streak(habit)
        habit_data.append({'name': habit, 'streak': streak})
        
    return render_template('index.html', habits=habit_data, total_hours=round(total_hours, 1))

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

@app.route('/add_habit', methods=['POST'])
def add_habit():
    habit_name = request.form['habit_name']
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO habits_list (habit_name) VALUES (?)", (habit_name,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass    # Habit already exists, ignore
    conn.close()
    return redirect(url_for('home'))

@app.route('/delete_habit/<habit_name>', methods=['POST'])
def delete_habit(habit_name):
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("DELETE FROM habits_list WHERE habit_name = ?", (habit_name,))
    c.execute("DELETE FROM habits WHERE habit_name = ?", (habit_name,))     # Also delete completion history
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/backfill', methods=['POST'])
def backfill():
    habit_name = request.form['habit_name']
    date_str = request.form['date']
    
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    
    # Check if entry already exists for this date
    c.execute("SELECT * FROM habits WHERE habit_name = ? AND date = ?", (habit_name, date_str))
    if c.fetchone() is None:
        c.execute("INSERT INTO habits (habit_name, date, completed) VALUES (?, ?, 1)", (habit_name, date_str))
        conn.commit()
    
    conn.close()
    return redirect(url_for('home'))

@app.route('/bulk_backfill', methods=['POST'])
def bulk_backfill():
    habit_name = request.form['habit_name']
    start_date = date.fromisoformat(request.form['start_date'])
    end_date = date.today() # Always end at today
    
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    
    current = start_date
    while current <= end_date:
        date_str = str(current)
        c.execute("SELECT * FROM habits WHERE habit_name = ? AND date = ?", (habit_name, date_str))
        if c.fetchone() is None:
            c.execute("INSERT INTO habits (habit_name, date, completed) VALUES (?, ?, 1)", (habit_name, date_str))
        current += timedelta(days=1)
    
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/add_competency_hours', methods=['POST'])
def add_competency_hours():
    hours = float(request.form['hours'])
    source = request.form.get('source', 'Manual')
    today = str(date.today())
    
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("INSERT INTO competency_hours (date, hours, source) VALUES (?, ?, ?)",
               (today, hours, source))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/get_total_hours')
def get_total_hours():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("SELECT SUM(hours) FROM competency_hours")
    total = c.fetchone()[0] or 0
    conn.close()
    return {'total': round(total, 1), 'goal': 600}

@app.route('/api/habit_data')
def habit_data():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("SELECT date, habit_name FROM habits ORDER BY date")
    rows = c.fetchall()
    conn.close()
    
    # Group by date
    data = {}
    for date_str, habit_name in rows:
        if date_str not in data:
            data[date_str] = []
        data[date_str].append(habit_name)
    
    return data

if __name__ == "__main__":
    init_db()
    init_competency_db()
    init_habit_time_db()
    app.run(debug=True)