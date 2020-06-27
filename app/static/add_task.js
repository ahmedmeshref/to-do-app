'use strict';
import {validInput, invalidInput, validateInput, handleErrors} from "./utils.js";

let app = {
    form: document.getElementById("add-item-form"),
    description: document.getElementById("description"),
    todo_list: document.getElementById("tasks-wrapper")
};


// change the border of the input if onfocus in case it was errored
app.description.addEventListener("focus", () => {
    validInput(app.description);
})


app.form.addEventListener("submit", (e) => {
    e.preventDefault();
    // validate input
    if (!validateInput(app.description)) return;
    fetch("/todos/create", {
        method: "POST",
        body: JSON.stringify({
            'description': app.description.value
        }),
        headers: {
            'Content-type': 'application/json'
        }
    })
    .then(handleErrors)
    .then((response_val) => {
        console.log(response_val);
        // create a new todo list item
        let LI = document.createElement('li');
        LI.classList.add("task-item");
        LI.innerHTML = `
            <div class="check-completed">
                <input class="checkbox" data-id='${response_val.id}' type="checkbox"/>
            </div>
            <div class="task-description">
                ${response_val.description}
            </div>
            <div class="delete-wrapper">
                <button type="button" class="delete-task" data-id='${response_val.id}'>&cross;</button>
            </div>
        `;
        app.todo_list.appendChild(LI);
        app.description.value = "";
    })
    .catch((err) => {
        invalidInput(app.description);
        console.log(err.message);
    })
})
