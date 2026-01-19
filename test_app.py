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