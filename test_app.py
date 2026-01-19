import pytest
from app import app
import sqlite3
import os

@pytest.fixture
def client():
    # Use a test database
    app.config['TESTING'] = True
    
    # Setup test database
    conn = sqlite3.connect('test_habits.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS habits_list
                 (id INTEGER PRIMARY KEY, habit_name TEXT UNIQUE)''')
    c.execute('''CREATE TABLE IF NOT EXISTS competency_hours
                 (id INTEGER PRIMARY KEY, date TEXT, hours REAL, source TEXT, habit_name TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS habits
                 (id INTEGER PRIMARY KEY, habit_name TEXT, date TEXT, completed INTEGER)''')
    c.execute("INSERT INTO habits_list (habit_name) VALUES ('Coding')")
    conn.commit()
    conn.close()
    
    with app.test_client() as client:
        yield client
    
    # Cleanup
    os.remove('test_habits.db')
    
def test_home_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Habit Tracker' in response.data
    
def test_add_habit(client):
    response = client.post('/add_habit', data={'habit_name': 'Gym'})
    assert response.status_code == 302  # Redirect after adding
    
def test_add_competency_hours(client):
    response = client.post('/add_competency_hours', data={
        'habit_name': 'Coding',
        'minutes': 90
    })
    assert response.status_code == 302  # Redirect
    
    # Verify it was added
    conn = sqlite3.connect('test_habits.db')
    c = conn.cursor()
    c.execute("SELECT SUM(hours) FROM competency_hours WHERE habit_name = 'Coding'")
    total = c.fetchone()[0]
    conn.close()
    assert total == 1.5  # 90 minutes = 1.5 hours
    
def test_delete_competency(client):
    # First add an entry
    conn = sqlite3.connect('test_habits.db')
    c = conn.cursor()
    c.execute("INSERT INTO competency_hours (date, hours, source, habit_name) VALUES ('2026-01-18', 2.0, 'Manual', 'Coding')")
    entry_id = c.lastrowid
    conn.commit()
    conn.close()
    
    # Delete it
    response = client.post(f'/delete_competency/{entry_id}')
    assert response.status_code == 302
    
    # Verify it's gone
    conn = sqlite3.connect('test_habits.db')
    c = conn.cursor()
    c.execute("SELECT * FROM competency_hours WHERE id = ?", (entry_id,))
    assert c.fetchone() is None
    conn.close()
    
def test_mark_habit_complete(client):
    response = client.post('/complete/Coding')
    assert response.status_code == 302
    
    # Verify completion was logged
    conn = sqlite3.connect('test_habits.db')
    c = conn.cursor()
    c.execute("SELECT * FROM habits WHERE habit_name = 'Coding'")
    assert c.fetchone() is not None
    conn.close()