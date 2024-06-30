let todoLists = [];

function addList() {

    const listName = document.getElementById('listName').value;

    if (listName) {

        todoLists.push({ name: listName, tasks: [] });

        document.getElementById('listName').value = '';

        renderLists();
    }
}

function deleteList(listIndex) {

    todoLists.splice(listIndex, 1);

    renderLists();
}

function addTask(listIndex) {

    const task = prompt('Gib die Aufgabe ein:');

    if (task) {

        todoLists[listIndex].tasks.push({ task: task, completed: false });

        renderLists();
    }
}

function deleteTask(listIndex, taskIndex) {

    todoLists[listIndex].tasks.splice(taskIndex, 1);

    renderLists();
}

function completeTask(listIndex, taskIndex) {

    todoLists[listIndex].tasks[taskIndex].completed = true;

    renderLists();
}

function renderLists() {

    const listsDiv = document.getElementById('lists');

    listsDiv.innerHTML = '';

    todoLists.forEach((list, listIndex) => {

        const listDiv = document.createElement('div');

        listDiv.className = 'list';

        const listHeader = document.createElement('h3');

        listHeader.innerText = list.name;

        listDiv.appendChild(listHeader);

        const taskButton = document.createElement('button');

        taskButton.innerText = 'Aufgabe hinzufügen';
        
        taskButton.onclick = () => addTask(listIndex);

        listDiv.appendChild(taskButton);

        const tasksDiv = document.createElement('div');

        tasksDiv.className = 'tasks';

        list.tasks.forEach((task, taskIndex) => {

            const taskDiv = document.createElement('div');

            taskDiv.className = 'task';

            const taskSpan = document.createElement('span');

            taskSpan.innerText = `${task.task} - ${task.completed ? 'Erledigt' : 'Offen'}`;

            taskDiv.appendChild(taskSpan);

            const completeButton = document.createElement('button');

            completeButton.innerText = 'Erledigt';

            completeButton.onclick = () => completeTask(listIndex, taskIndex);

            taskDiv.appendChild(completeButton);

            const deleteButton = document.createElement('button');

            deleteButton.innerText = 'Löschen';

            deleteButton.onclick = () => deleteTask(listIndex, taskIndex);

            taskDiv.appendChild(deleteButton);

            tasksDiv.appendChild(taskDiv);
        });

        listDiv.appendChild(tasksDiv);

        const deleteListButton = document.createElement('button');

        deleteListButton.innerText = 'Liste löschen';

        deleteListButton.onclick = () => deleteList(listIndex);
        
        listDiv.appendChild(deleteListButton);

        listsDiv.appendChild(listDiv);
    });
}
