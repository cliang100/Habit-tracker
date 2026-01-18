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
✅ Per-habit total time display  
✅ Eye break reminders (alerts every 20 minutes during work sessions)  
✅ Manual competency backfill with habit selector (Coding vs Leetcode, input minutes)  
✅ Collapsible competency entries table with delete functionality  
🐛 **BUG**: Deleting competency entry removes ALL habit_time entries instead of just matching one  
⏳ Add collapsible habit_time log table (similar to competency entries)  
⏳ Calendar visual indicators (color-coded habit dots without clicking)  
⏳ Preset pomodoro duration buttons (25/5, 50/10, 90/15)  
⏳ Modern UI with animations  
⏳ Write unit tests with pytest

## Known Issues
**CRITICAL BUG - Delete Function:**
- Deleting a competency entry removes ALL matching habit_time entries for that habit/date, not just the specific minutes amount
- Example: Two 30-min Coding entries on same day = 1h total. Deleting one entry removes BOTH, zeroing out the time.
- **Fix needed**: DELETE query is too broad - matches on `habit_name`, `date`, and `minutes`, but multiple entries can have same values. Need better matching logic or unique constraint.

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
 source TEXT,
 habit_name TEXT)

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
9. ✅ Manual competency backfill with minutes input
10. 🐛 Fix delete functionality (currently broken)
11. ⏳ Add habit_time log table
12. ⏳ Preset pomodoro buttons
13. ⏳ Visual calendar improvements
14. ⏳ Modern UI with animations
15. ⏳ Write unit tests

## Next Session Priority
**Fix the delete bug**: The DELETE query matches multiple rows when there are duplicate entries. Need to either:
- Track `competency_hours.id` → `habit_time.id` relationship in database
- Delete using `LIMIT 1` and `ORDER BY id` to only remove oldest/newest match
- Store a unique session_id to link entries across tables