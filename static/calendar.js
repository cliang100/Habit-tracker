let currentMonth = new Date().getMonth();
let currentYear = new Date().getFullYear();
let habitData = {};

const habitColors = {
    'Coding': '#f97316',
    'Leetcode': '#3b82f6'
};

const availableColors = ['#e0e0e0', '#ff0000', '#8b5cf6', '#ec4899', '#14b8a6', '#44003e'];
let colorIndex = 0;

function getHabitColor(habitName) {
    if (!habitColors[habitName]) {
        habitColors[habitName] = availableColors[colorIndex % availableColors.length];
        colorIndex++;
    }
    return habitColors[habitName];
}

async function loadHabitData() {
    const response = await fetch('/api/habit_data');
    habitData = await response.json();
    renderCalendar();
}

function renderCalendar() {
    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"];

    document.getElementById('current-month').textContent = 
        `${monthNames[currentMonth]} ${currentYear}`;
    
    const firstDay = new Date(currentYear, currentMonth, 1).getDay();
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();

    let calendarHTML = `<div class = "calendar-grid">`;

    // Day headers
    const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    days.forEach(day => {
        calendarHTML += `<div class="calendar-header">${day}</div>`;
    });

    // Empty cells before first day
    for (let i = 0; i < firstDay; i ++) {
        calendarHTML += `<div class="calendar-day empty"></div>`;
    }

    // Days of month
    for (let day = 1; day <= daysInMonth; day++) {
        const dateStr = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
        const habits = habitData[dateStr] || [];
        const hasData = habits.length > 0;
        const isToday = new Date().toDateString() === new Date(currentYear, currentMonth, day).toDateString();

        let dotsHTML = '';
        if (hasData) {
            dotsHTML = '<div class="habit-dots">';
            habits.forEach(habit => {
                const color = getHabitColor(habit);
                dotsHTML += `<span class="habit-dot" style="background-color: ${color}"></span>`;
            });
            dotsHTML += '</div>';
        }

        calendarHTML += `<div class="calendar-day ${hasData ? 'completed' : ''} ${isToday ? 'today' : ''}"
        onclick="showDayDetails('${dateStr}')">
        <span class="day-number">${day}</span>
        ${dotsHTML}
        </div>`;
    }

    calendarHTML += `</div>`;
    document.getElementById('calendar-container').innerHTML = calendarHTML;
}

function previousMonth() {
    currentMonth--;
    if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--; 
    }
    renderCalendar();
}

function nextMonth() {
    currentMonth++;
    if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
    }
    renderCalendar();
}

function showDayDetails(dateStr) {
    const habits = habitData[dateStr];
    if (habits && habits.length > 0) {
        document.getElementById('modal-date').textContent = dateStr;
        const container = document.getElementById('modal-habits-container');

        container.innerHTML = habits.map(h => `
            <div style="display: flex; justify-content: space-between; align-items: center; 
                        padding: 12px; background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); 
                        margin: 8px 0; border-radius: 10px;">
                <span>${h}</span>
                <form action="/delete_habit_completion" method="POST" style="margin: 0;">
                    <input type="hidden" name="habit_name" value="${h}">
                    <input type="hidden" name="date" value="${dateStr}">
                    <button type="submit" class="delete-btn-small" 
                            onclick="return confirm('Delete ${h} from ${dateStr}?')">×</button>
                </form>
            </div>
        `).join('');

        document.getElementById('day-modal').style.display = 'block';
    }
}

function closeModal() {
    document.getElementById('day-modal').style.display = 'none';
}

// Load on page load
loadHabitData();