let workDuration = 25 * 60;
let breakDuration = 5 * 60;
let timeLeft = workDuration;
let timerInterval = null;
let isRunning = false;
let isBreak = false;

function updateDisplay() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    document.getElementById('timer-display').textContent =
        `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function startTimer() {
    if (isRunning) return;
    isRunning = true;

    timerInterval = setInterval(() => {
        timeLeft--;
        updateDisplay();

        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            isRunning = false;
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

// Initialize on page load
updateDisplay();