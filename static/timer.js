let workDuration = 25 * 60;
let breakDuration = 5 * 60;
let timeLeft = workDuration;
let timerInterval = null;
let isRunning = false;
let isBreak = false;
let eyeBreakInterval = 20 * 60;
let timeSinceLastEyeBreak = 0;

function updateDisplay() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    document.getElementById('timer-display').textContent =
        `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function startTimer() {
    if (isRunning) return;
    isRunning = true;

    // Validate habit selection before starting
    const habitSelect = document.getElementById('timer-habit');
    if (!habitSelect.value) {
        alert('Please select a habit before starting the timer!');
        return;
    }

    timerInterval = setInterval(() => {
        timeLeft--;
        timeSinceLastEyeBreak++;
        updateDisplay();

        // Check for eye break every 20 minutes
        if (timeSinceLastEyeBreak >= eyeBreakInterval && !isBreak) {
            alert('👁️ Eye Break! Look at something 20 feet away for 20 seconds.');
            timeSinceLastEyeBreak = 0;
        }

        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            isRunning = false;

            // Log hours if work session (not break)
            if (!isBreak) {
                logCompetencyHours(workDuration / 60);
            }

            alert(isBreak ? 'Break over! Back to work.' : 'Time for a break!');
            switchMode();
        }
    }, 1000);
}

function pauseTimer() {
    clearInterval(timerInterval);
    isRunning = false;
}

function resetTimer() {
    clearInterval(timerInterval);
    isRunning = false;
    timeLeft = isBreak ? breakDuration: workDuration;
    updateDisplay();
}

function switchMode() {
    isBreak = !isBreak;
    timeLeft = isBreak ? breakDuration: workDuration;
    document.getElementById('timer-mode').textContent = isBreak ? 'Break Time' : 'Work Session';
    updateDisplay();
}

function updateSettings() {
    workDuration = parseInt(document.getElementById('work-duration').value) * 60;
    breakDuration = parseInt(document.getElementById('break-duration').value) * 60;
    resetTimer();
}

function logCompetencyHours(minutes) {
    const habitSelect = document.getElementById('timer-habit');
    const habitName = habitSelect.value;

    fetch('/log_habit_time', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `habit_name=${habitName}&minutes=${minutes}`
    });
}

function setPreset(workMin, breakMin) {
    document.getElementById('work-duration').value = workMin;
    document.getElementById('break-duration').value = breakMin;
    updateSettings();
}

// Initialize on page load
updateDisplay();