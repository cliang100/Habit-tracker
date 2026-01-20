# Habit Tracker

A web-based habit streak tracker built with Flask and SQLite. Track multiple habits independently with automatic midnight streak reset, Pomodoro timer with eye break reminders, competency hour tracking for Coding/Leetcode, and a modern dark mode UI.

## Features & Status
- ✅ **Multi-habit tracking** - Track multiple habits with independent streak counters
- ✅ **Add/delete habits** - Dynamically manage habits
- ✅ **Automatic streak reset** - Midnight reset if habit not completed
- ✅ **Pomodoro timer** - Customizable work/break durations with preset buttons (25/5, 50/10, 90/15)
- ✅ **Eye break reminders** - 20-20-20 rule alerts every 20 minutes during work sessions
- ✅ **Timer integration** - Auto-logs hours to selected habit (Coding/Leetcode count toward competency)
- ✅ **Competency tracking** - 600-hour goal with split progress bar (Coding vs Leetcode visualization)
- ✅ **Manual backfill** - Input minutes for competency hours, auto-converts to hours
- ✅ **Collapsible entries table** - View and delete all competency entries
- ✅ **Calendar view** - Interactive calendar with color-coded habit dots and modal popups
- ✅ **Modern UI** - Glassmorphism, smooth animations, gradient effects
- ✅ **Unit tests** - pytest coverage for core functionality
- ✅ **Dark mode** - Clean, modern design
- 🔧 **IN PROGRESS** - Delete individual habit completions from calendar modal

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` and start tracking!

## Running Tests
```bash
pytest test_app.py -v
```

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

-- Competency hours tracking (Coding/Leetcode only)
CREATE TABLE competency_hours
(id INTEGER PRIMARY KEY,
 date TEXT,
 hours REAL,
 source TEXT,
 habit_name TEXT)
```

## Tech Stack
- Python 3.12
- Flask
- SQLite
- HTML/CSS/JavaScript
- pytest (testing)

## Personal Notes for Coding Progress
I've been working on this project consistently since January 12th.  

Early manual estimates + recent sessions:  
- Coding: ~11.5 hours  
- Leetcode: ~2.5 hours  
- Recent Jan 19th sessions: 3.5 hours (90 min + 25 min + 90 min)
- **Total: ~17.5 hours toward 600-hour junior-dev goal**

All future time will be auto-tracked via the timer/backfill. Once I backfill the early sessions accurately into the app, this manual note can be removed. Progress bar is live and motivating!