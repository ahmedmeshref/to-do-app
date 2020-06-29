import {handleErrors, logError, request} from "./utils.js";

let app = {
    delete_task: document.querySelectorAll(".delete-task"),
    delete_list: document.querySelectorAll(".delete-list")
}

let delete_item = (btn, address, wrapper) => {
    const btn_id = btn.getAttribute("data-id"),
        route = `/todos/${btn_id}/${address}`,
        method = "DELETE",
        handleRequestOutput = (responseVal) => {
            console.log(responseVal);
            // delete li item from dom
            const items_wrapper = document.querySelector(`#${wrapper}`),
                target_item = items_wrapper.querySelector(`li[data-id='${btn_id}']`);
            target_item.parentNode.removeChild(target_item);
        };
    request(route, method, {}, handleErrors, handleRequestOutput,  logError);
}


// loop through all task keys looking for an click event
for (let i = 0; i < app.delete_task.length; i++) {
    const btn = app.delete_task[i];
    btn.onclick = () => {
        const address = 'delete_task',
            wrapper = 'tasks-wrapper';
        delete_item(btn, address, wrapper);
    }
}

// loop through all list keys looking for an click event
for (let i= 0; i < app.delete_list.length; i++){
    const btn = app.delete_list[i],
        wrapper = 'lists-wrapper';
    btn.addEventListener('click', () => {
        const address = 'delete_list',
            wrapper = 'lists-wrapper';
        delete_item(btn, address, wrapper)
    })
}