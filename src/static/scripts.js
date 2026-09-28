document.addEventListener('DOMContentLoaded', async () => {
    const lessonList = document.getElementById('lesson-list');

    try {
        const response = await fetch('/lessons/');
        const lessons = await response.json();

        lessons.forEach(lesson => {
            const lessonItem = document.createElement('div');
            lessonItem.className = 'lesson-item';
            lessonItem.innerHTML = `
                <h2>${lesson.title}</h2>
                <p>${lesson.content}</p>
                <a href='/lessons/${lesson.id}/exercises'>View Exercises</a>
            `;
            lessonList.appendChild(lessonItem);
        });
    } catch (error) {
        console.error('Error fetching lessons:', error);
    }
});
