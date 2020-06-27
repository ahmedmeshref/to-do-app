import {handleErrors, logRequestResult, logError, request} from "./utils.js";

let app = {
    checkboxes: document.querySelectorAll(".checkbox"),
}


for (let i = 0; i < app.checkboxes.length; i++) {
    const checkbox = app.checkboxes[i];
    checkbox.onchange = (event) => {
        let isCompleted = event.target.checked,
            task_id = checkbox.getAttribute('data-id'),
            route = `/todos/${task_id}/update_completed`,
            method = "POST",
            msg = {
                "id": task_id,
                'state': isCompleted
            }
        request(route, method, msg, handleErrors, logRequestResult,  logError);
    }
}
