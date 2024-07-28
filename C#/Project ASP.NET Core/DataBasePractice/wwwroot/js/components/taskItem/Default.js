const tasks = document.querySelectorAll('.task');
tasks.forEach(task => {
    const id = task.dataset.id;
    let editBtn = task.querySelector('.edit');

    editBtn.addEventListener('click', () => {
        task.querySelector('[for="IsCompleted-${id}"}').classList.add('d-none');
        editBtn.classList.add('disabled');
        task.querySelector('.editable-group').classList.remove('d-none');
    });

    task.querySelector('.cancel').addEventListener('click', () => {
        location.reload();
    });
});