

app = {
    lists : document.querySelector("#lists-wrapper").querySelectorAll("li:(.list-item):not(.selected-list)")
}


for (let i = 0; i < app.lists.length; i++){
    const list = app.lists[i];
    alert("I am inside the loop");
    list.addEventListener('click', (e) => {
        alert("you clicked me");
        const list_id = list.getAttribute('data-id');
        fetch(`/${list_id}/`, {
            method: "POST",
            headers: {
                'Content-type': 'application/json'
            }
        }).catch((e) => {
            console.log(e)
        })
    })
}