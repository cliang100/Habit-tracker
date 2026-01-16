let currentMonth = new Date().getMonth();
let currentYear = new Date().getFullYear();
let habitData = {};

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
        const hasData = habitData[dateStr] && habitData[dateStr].length > 0;
        const isToday = new Date().toDateString() === new Date(currentYear, currentMonth, day).toDateString();

        calendarHTML += `<div class="calendar-day ${hasData ? 'completed' : ''} ${isToday ? 'today' : ''}"
        onclick="showDayDetails('${dateStr}')">
        ${day}
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
        alert(`Completed on ${dateStr}:\n- ${habits.join('\n- ')}`);
    }
}

// Load on page load
loadHabitData();