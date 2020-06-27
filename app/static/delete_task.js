import {handleErrors} from "./utils.js";

let app = {
    delete_btns: document.querySelectorAll(".delete-task"),
}

// delete task from db
for (let i = 0; i < app.delete_btns.length; i++) {
    const btn = app.delete_btns[i];
    btn.onclick = () => {
        const btn_id = btn.getAttribute("data-id");
        fetch(`/todos/${btn_id}/delete_task`, {
            method: 'POST',
            body: "delete-item",
            headers: {
                'Content-type': 'application/json'
            }
        })
        .then(handleErrors)
        .then((responseVal) => {
            console.log(responseVal);
            const all_tasks = document.querySelector("#tasks-wrapper"),
                task_item = all_tasks.querySelector(`li[data-id='${btn_id}']`);
            task_item.parentNode.removeChild(task_item);
        })
        .catch((err) => {
            console.log(err);
        })
    }

}
