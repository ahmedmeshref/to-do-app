'use strict';

let app = {
    form: document.getElementById("add-item-form"),
    description: document.getElementById("description"),
    todo_list: document.getElementById("tasks-list")
};

let validInput = (element) => {
    if (element.classList.includes("error")){
        element.classList.remove("error");
    }
    element.classList.add("shadow");
}

let invalidInput = (element) => {
    element.classList.add("error");
}


let validateInput = (element) => {
    if (!element.value) {
        invalidInput(element);
        return false;
    }
    return true;
}

// change the border of the input if onfocus
app.description.addEventListener("focus", () => {
    validInput(app.description);
})


app.form.addEventListener("submit", () => {
    event.preventDefault();
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
        .then((response) => response.json())
        .then((response_val) => {
            console.log(`description: ${response_val.description}`);
            // create a new todo list item
            let LI = document.createElement('li');
            LI.innerHTML = response_val.description;
            app.todo_list.appendChild(LI);
            app.description.value = "";
        })
        .catch((err) => console.log(err.message))
})

