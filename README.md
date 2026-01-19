# Habit Tracker

A web-based habit streak tracker built with Flask and SQLite. Track multiple habits independently with automatic midnight streak reset, Pomodoro timer with eye break reminders, competency hour tracking for Coding/Leetcode, and a modern dark mode UI.

## Features
- Track multiple habits with independent streak counters
- Add and delete habits dynamically
- Prevent duplicate entries (only 1 completion per habit per day)
- Automatic streak reset at midnight if habit not completed
- Pomodoro timer with customizable work/break durations
- Eye break reminders (20-20-20 rule: every 20 minutes)
- Timer auto-logs hours to selected habit (Coding/Leetcode count toward competency)
- Competency-specific time tracking (only Coding/Leetcode show Time: Xh)
- Coding competency hours tracker with progress bar (0-600 hour goal)
- Collapsible table showing all competency entries with delete buttons
- Interactive calendar view with modal popups showing daily completions
- Manual backfill for competency hours (input minutes, auto-converts to hours)
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
✅ Competency-specific time display (Coding/Leetcode only)  
✅ Eye break reminders (alerts every 20 minutes during work sessions)  
✅ Manual competency backfill with habit selector (Coding vs Leetcode, input minutes)  
✅ Collapsible competency entries table with delete functionality  
✅ Delete bug fixed (removed habit_time table, simplified to competency_hours only)  
🔧 **IN PROGRESS**: Unit tests with pytest (database path config added, need to finish refactor)  
⏳ Split progress bar (show Coding vs Leetcode distribution with colors)  
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
9. ✅ Manual competency backfill with minutes input
10. ✅ Fix delete functionality (simplified to single table)
11. ✅ Write unit tests with pytest
12. ✅ Split progress bar (Coding vs Leetcode visualization)
13. ✅ Preset pomodoro buttons
14. ⏳ Visual calendar improvements
15. ⏳ Modern UI with animations

## Next Steps
- Complete database path refactor (replace all `habits.db` with `get_db_path()`)
- Finish writing unit tests for all routes
- Split progress bar to show Coding/Leetcode distribution

## Personal Notes for Coding Progress
I've been working on this project consistently since January 12th.  

Early manual estimates (conservative undershoot):  
- Coding: ~11.5 hours  
- Leetcode: ~2.5 hours  
- Total: 14 hours  

Recent sessions (Jan 19th):  
- 90 min deep work block  
- 25 min Pomodoro block  

Current rough total (still conservative): ~15.9 hours toward the 600-hour junior-dev goal.  

All future time will be auto-tracked via the timer/backfill. Once I backfill the early sessions accurately into the app, this manual note can be removed. Progress bar is live and motivating!