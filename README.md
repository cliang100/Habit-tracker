# Habit Tracker

A simple web-based habit tracker built with Flask and SQLite.

## Features
- Mark daily habits as complete
- Track consecutive day streaks
- Local SQLite database for persistence

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -c "from app import init_db; init_db()"
python app.py
```

Visit `http://localhost:5000`

## Tech Stack
- Python 3.12
- Flask
- SQLite