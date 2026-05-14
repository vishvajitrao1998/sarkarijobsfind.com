// Dark mode
const toggle = document.getElementById('darkToggle');
const knob = toggle.querySelector('.knob');

// Apply dark mode
function setDark(dark) {
    document.documentElement.classList.toggle('dark-mode', dark);
    knob.textContent = dark ? '☀️' : '🌙';
    toggle.style.background = dark ? '#f59e0b' : 'var(--border-color)';

    // ✅ Save preference
    localStorage.setItem('theme', dark ? 'dark' : 'light');
}

// Load saved theme or system preference
function initTheme() {
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme) {
        setDark(savedTheme === 'dark');
    } else {
        const systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        setDark(systemDark);
    }
}

// Initialize on load
initTheme();

// Toggle click
toggle.addEventListener('click', () => {
    const isDark = document.documentElement.classList.contains('dark-mode');
    setDark(!isDark);
});