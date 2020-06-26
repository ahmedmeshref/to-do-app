import {request} from "./utils.js";

let app = {
    checkboxes: document.querySelectorAll(".check-completed")
}


for (let i = 0; i < app.checkboxes.length; i++) {
    const checkbox = app.checkboxes[i];
    checkbox.onchange = (event) => {
        let isCompleted = event.target.checked,
            route = "/todos/update_completed",
            method = "POST",
            msg = {
                "id": checkbox.value,
                'state': isCompleted
            }
        request(route, method, msg);
    }
}

