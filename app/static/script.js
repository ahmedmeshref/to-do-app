let nt_btn = document.getElementById("btn-new-task"),
    description = document.getElementById("description"),
    todo_list = document.getElementById("tasks-list");


let validInput = (element) => {
    if (!element.value){
        element.style.border = "thick solid #c51244";
        return false;
    }
    return true;
}

nt_btn.addEventListener("click", () => {
    if (!validInput(description)) return;
    fetch("/add_task", {
        method: "POST",
        body: JSON.stringify({
            'description': description.value
        }),
        headers: {
            'Content-type': 'application/json'
        }
    })
    .then((response) => response.json())
    .then((response_val) => {
        console.log(`Success, ${response_val.description}`);
        // create a new todo list item
        let LI = document.createElement('li');
        LI.innerHTML = response_val.description;
        todo_list.appendChild(LI);
        description.value = "";
    })
    .catch((err) => console.log(err.message))
})

// change the border of the input if onfocus
description.addEventListener("focus", () => {
    description.style.border = "1px solid black";
})