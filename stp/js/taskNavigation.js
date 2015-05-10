var serverUrl = 'http://localhost:8080';
var apiKey = "1008bee6bf63f17efe213a5cd3e6fc69bac58c528eb6cc69ef2edb7f5cd666b3";
// The two values above are server dependant !

var numberOfDisplayableTasks = 10;

var taskStartIndex = 0;
var numberOfDisplayedTasks;

var criteria = null;
var lookedFor = null;

function initialRequest() {
	requestGroupOfTasks(taskStartIndex);
}

function searchTasks() {
	criteria = document.forms["searchForm"]["sel1"].value;
	lookedFor = document.forms["searchForm"]["search"].value;
	taskStartIndex = 0;
	requestGroupOfTasks(taskStartIndex);
}

function nextGroupOfTasks() {
	requestGroupOfTasks(taskStartIndex + numberOfDisplayableTasks);
}

function previousGroupOfTasks() {
	requestGroupOfTasks(Math.max(taskStartIndex - numberOfDisplayableTasks, 0));
}

function requestGroupOfTasks(startIndex) {
	var xhr = new XMLHttpRequest();
	xhr.addEventListener('readystatechange', function() {
		if (xhr.readyState === xhr.DONE && xhr.status == 200) {
			var parsedJSON = JSON.parse(xhr.responseText);
			console.log(parsedJSON); //TODO remove that
			if (!parsedJSON.noTask) {
				setTasks(parsedJSON.tasks, parsedJSON.start, parsedJSON.end);
			}
		}
	}, false);
	var url = serverUrl + '/api/tasks?start=' + (startIndex) + "&end=" + (startIndex + numberOfDisplayableTasks - 1) + "&key=" + apiKey;
	if (criteria != null && lookedFor != null) {
		url += "&filter=" +criteria + "&search=" + lookedFor;
	}
	xhr.open('GET', url, true);
	xhr.send(null);
}

function setTasks(tasks, start, end) {
	taskStartIndex = start;
	numberOfDisplayedTasks = end - start + 1;
	for (i = 1; i <= numberOfDisplayedTasks; i++) {
		setTaskContent(i, tasks[i - 1]);
	}
	displayAllTasks();
	hideTasksWithIndexStartingAt(numberOfDisplayedTasks + 1);
}

function setTaskContent(index, task) {
	var taskElement = getTaskElement(index);
	taskElement.children[0].children[0].children[0].text = task.title;
	taskElement.children[0].children[0].children[0].href = "/task/" + task.id;
	taskElement.children[1].children[0].innerHTML = task.content;
	var links = taskElement.children[2].children[0];
	links.children[0].innerHTML = "Publié par : " + task.author;
	links.childNodes[1].nodeValue = " Pour le " + task.date;
}

function displayAllTasks() {
	for (i = 1; i <= numberOfDisplayableTasks; i++) {
		getTaskElement(i).style.display = "";
	}
}

function hideTasksWithIndexStartingAt(startIndex) {
	for(i = startIndex; i <= numberOfDisplayableTasks; i++) {
		getTaskElement(i).style.display = "none";
	}
}

function getTaskElement(index) {
	return document.getElementById('task' + index);
}
