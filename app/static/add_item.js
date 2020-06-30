'use strict';
import {validInput, invalidInput, isValidateInput, handleErrors, request} from "./utils.js";

let app = {
    task_form: document.getElementById("add-task"),
    description: document.getElementById("description"),
    tasks_wrapper: document.getElementById("tasks-wrapper"),
    list_form: document.getElementById("add-list"),
    list_name: document.getElementById("list_name"),
    list_input_error: document.getElementById("list-input-error"),
    list_wrapper: document.getElementById("lists-wrapper"),
};


// change the border of the task_description input if onfocus in case it was errored
app.description.addEventListener("focus", () => {
    validInput(app.description);
})

// change the border of the list_name input if onfocus in case it was errored
app.list_name.addEventListener("focus", () => {
    validInput(app.list_name);
})

app.task_form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!isValidateInput(app.description)) return;
    const route = "/todos/create",
        method = "POST",
        msg = {'description': app.description.value},
        logRequestResult = (response_val) => {
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
                <button type="button" class="delete-task" data-id='${response_val.id}'>
                    <span class="fa  fa-trash-o"></span>
                </button>
            </div>
            `;
            app.tasks_wrapper.appendChild(LI);
            app.description.value = "";
        },
        logError = (err) => {
            invalidInput(app.description);
            console.log(err.message);
        };
     request(route, method, msg, handleErrors, logRequestResult, logError);
})


app.list_form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!isValidateInput(app.list_name)) return;
    const route = "/todos/create_list",
        method = "POST",
        msg = {"list_name": app.list_name.value},
        logRequestResult = (response_val) => {
            console.log(response_val);
            // create a new todo list item
            let LI = document.createElement('li');
            LI.classList.add("list-item");
            LI.innerHTML = `
            <div class="list-name">
                ${response_val.name}
            </div>
            <div class="delete-wrapper">
                <button type="button" class="delete-item delete-list" data-id="${response_val.id}">
                    <span class="fa  fa-trash"></span>
                </button>
            </div>
            `;
            app.list_wrapper.appendChild(LI);
            app.list_name.value = "";
        },
        logError = (err) => {
            invalidInput(app.list_name);
            console.log(err.message);
        };
     request(route, method, msg, handleErrors, logRequestResult, logError);
})