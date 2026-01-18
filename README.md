# Habit Tracker

A web-based habit streak tracker built with Flask and SQLite. Track multiple habits independently with automatic midnight streak reset, Pomodoro timer, and a modern dark mode UI.

## Features
- Track multiple habits with independent streak counters
- Add and delete habits dynamically
- Prevent duplicate entries (only 1 completion per habit per day)
- Automatic streak reset at midnight if habit not completed
- Pomodoro timer with customizable work/break durations
- Backfill past streak data (single day or date range)
- Coding competency hours tracker (600-800 hour goal)
- Interactive calendar view with completion history
- Dark mode with clean UI
- Persistent local database

## Current Status
✅ Multi-habit tracking system  
✅ Add/delete habit functionality  
✅ Streak calculation with midnight reset  
✅ Styled dark mode UI  
✅ Pomodoro timer with pause/reset  
✅ Backfill past streaks (single & bulk)  
✅ Calendar view with modal popups  
✅ Competency hours tracker with progress bar  
🔄 Timer-to-habit integration (in progress)  
⏳ Calendar visual indicators (color-coded habit dots)  
⏳ Eye break reminders  
⏳ Preset pomodoro durations  
⏳ Modern UI with animations

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
-- Habit completions
CREATE TABLE habits 
(id INTEGER PRIMARY KEY, 
 habit_name TEXT, 
 date TEXT, 
 completed INTEGER)

-- Available habits
CREATE TABLE habits_list
(id INTEGER PRIMARY KEY,
 habit_name TEXT UNIQUE)

-- Competency hours tracking
CREATE TABLE competency_hours
(id INTEGER PRIMARY KEY,
 date TEXT,
 hours REAL,
 source TEXT)

-- Per-habit time tracking
CREATE TABLE habit_time
(id INTEGER PRIMARY KEY,
 habit_name TEXT,
 date TEXT,
 minutes INTEGER)
```

## Tech Stack
- Python 3.12
- Flask
- SQLite
- HTML/CSS/JavaScript
- Dark mode styling

## Project Goals
1. ✅ Multi-habit tracking
2. ✅ Add/delete habits
3. ✅ Midnight reset logic
4. ✅ Pomodoro timer with custom durations
5. ✅ Backfill past streak data
6. 🔄 Calendar view (in progress - bug with multi-habit display)
7. ⏳ Eye break reminders
8. ⏳ Sound effects & motivational quotes