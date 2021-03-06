'use strict';
import {validInput, invalidInput, validateInput, handleErrors} from "./utils.js";

let app = {
    form: document.getElementById("add-item-form"),
    description: document.getElementById("description"),
    todo_list: document.getElementById("tasks-list")
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
        console.log(`description: ${response_val.description}`);
        // create a new todo list item
        let LI = document.createElement('li');
        LI.innerHTML = response_val.description;
        app.todo_list.appendChild(LI);
        app.description.value = "";
    })
    .catch((err) => {
        invalidInput(app.description);
        console.log(err.message);
    })
})

