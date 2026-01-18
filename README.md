# Habit Tracker

A web-based habit streak tracker built with Flask and SQLite. Track multiple habits independently with automatic midnight streak reset, Pomodoro timer with eye break reminders, competency hour tracking, and a modern dark mode UI.

## Features
- Track multiple habits with independent streak counters
- Add and delete habits dynamically
- Prevent duplicate entries (only 1 completion per habit per day)
- Automatic streak reset at midnight if habit not completed
- Pomodoro timer with customizable work/break durations
- Eye break reminders (20-20-20 rule: every 20 minutes)
- Timer auto-logs hours to selected habit (Coding/Leetcode count toward competency)
- Per-habit time tracking (see total hours spent on each habit)
- Coding competency hours tracker with progress bar (0-600 hour goal)
- Interactive calendar view with modal popups showing daily completions
- Manual backfill for past streak data and competency hours
- Dark mode with clean UI
- Persistent local database

## Current Status
✅ Multi-habit tracking system  
✅ Add/delete habit functionality  
✅ Streak calculation with midnight reset  
✅ Styled dark mode UI  
✅ Pomodoro timer with pause/reset  
✅ Backfill past streaks (single & bulk)  
✅ Calendar view with modal popups (shows all habits per day)  
✅ Competency hours tracker with progress bar (2 decimal precision)  
✅ Timer-to-habit integration (auto-logs time for selected habit)  
✅ Per-habit total time display  
✅ Eye break reminders (alerts every 20 minutes during work sessions)  
⏳ Delete/undo entries (fix mistakes in competency hours/time logs)  
⏳ Habit selector for manual competency backfill (Coding vs Leetcode)  
⏳ Calendar visual indicators (color-coded habit dots without clicking)  
⏳ Preset pomodoro duration buttons (25/5, 50/10, 90/15)  
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

-- Competency hours tracking (Coding/Leetcode only)
CREATE TABLE competency_hours
(id INTEGER PRIMARY KEY,
 date TEXT,
 hours REAL,
 source TEXT)

-- Per-habit time tracking (all habits)
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
6. ✅ Calendar view with multi-habit display
7. ✅ Eye break reminders
8. ✅ Timer integration with habit tracking
9. ⏳ Delete/undo functionality for mistakes
10. ⏳ Preset pomodoro buttons
11. ⏳ Visual calendar improvements
12. ⏳ Modern UI with animations

## Development TODO
- [ ] Complete delete functionality for competency entries
  - Update home() route to fetch competency_entries
  - Add /delete_competency/<id> route
  - Add CSS for entry table display
- [ ] Add habit selector to manual competency backfill form
- [ ] Calendar visual improvements (colored dots per habit)
- [ ] Preset pomodoro duration buttons
- [ ] Modern UI animations