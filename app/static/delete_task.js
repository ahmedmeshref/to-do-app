import {handleErrors} from "./utils.js";

let app = {
    delete_btns: document.querySelectorAll(".delete-task"),
    task_item: document.querySelectorAll(".task-item")
}

// delete task from db
for (let i = 0; i < app.delete_btns.length; i++) {
    const btn = app.delete_btns[i];
    btn.onclick = () => {
        let btn_id = btn.getAttribute("data-id");
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
            const task_item = app.task_item[i];
            task_item.parentNode.removeChild(task_item);
        })
        .catch((err) => {
            console.log(err);
        })
    }

}
