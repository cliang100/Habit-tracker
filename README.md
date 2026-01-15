# Habit Tracker

A web-based habit streak tracker built with Flask and SQLite. Track multiple habits independently with automatic midnight streak reset and a modern dark mode UI.

## Features
- Track multiple habits with independent streak counters
- Add and delete habits dynamically
- Prevent duplicate entries (only 1 completion per habit per day)
- Automatic streak reset at midnight if habit not completed
- Dark mode with color-coded habit categories
- Persistent local database

## Current Status
✅ Multi-habit tracking system  
✅ Add/delete habit functionality  
✅ Streak calculation with midnight reset  
✅ Styled dark mode UI  
⏳ Timer/Pomodoro functionality (planned)  
⏳ Customizable streak notifications (planned)

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` and start tracking!

## Database Schema
```sql
CREATE TABLE habits 
(id INTEGER PRIMARY KEY, 
 habit_name TEXT UNIQUE, 
 date TEXT, 
 completed INTEGER)
```

## Tech Stack
- Python 3.12
- Flask
- SQLite
- HTML/CSS with dark mode styling

## Project Goals (In Progress)
1. ✅ Multi-habit tracking
2. ✅ Add/delete habits
3. ✅ Midnight reset logic
4. ⏳ Timer with pause functionality
5. ⏳ Pomodoro mode with work/break intervals
6. ⏳ Data export functionality