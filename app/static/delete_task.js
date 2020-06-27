import {handleErrors, logError, request} from "./utils.js";

let app = {
    delete_btns: document.querySelectorAll(".delete-task")
}

let delete_item = (btn) => {
    const btn_id = btn.getAttribute("data-id"),
        route = `/todos/${btn_id}/delete_task`,
        method = "DELETE",
        handleRequestOutput = (responseVal) => {
            console.log(responseVal);
            // delete li item from dom
            const all_tasks = document.querySelector("#tasks-wrapper"),
                task_item = all_tasks.querySelector(`li[data-id='${btn_id}']`);
            task_item.parentNode.removeChild(task_item);
        };
    request(route, method, {}, handleErrors, handleRequestOutput,  logError);
}


// delete task from db
for (let i = 0; i < app.delete_btns.length; i++) {
    const btn = app.delete_btns[i];
    btn.onclick = () => {
        delete_item(btn);
    }
}
