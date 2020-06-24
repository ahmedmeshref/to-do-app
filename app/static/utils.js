// validInput takes an input field item and removes the error class if there
export let validInput = (element) => {
    element.classList.remove("error");
}

// invalidInput takes an input field item and adds the error class
export let invalidInput = (element) => {
    element.classList.add("error");
}

// validateInput takes in an input field item and validates its value
export let validateInput = (element) => {
    if (!element.value) {
        invalidInput(element);
        return false;
    }
    return true;
}

// handleErrors is a callback function throw an error message in case response error from backend
export let handleErrors = (response) => {
    if (!response.ok) {
        throw Error(response.statusText);
    }
    return response.json();
}

