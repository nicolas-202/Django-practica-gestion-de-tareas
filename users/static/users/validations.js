const usernameInput = document.getElementById('usernameInput');
const passwordInput = document.getElementById('passwordInput');
const loginForm = document.querySelector('form');

function validateRequired(input){
    input.classList.toggle('is-invalid', input.value.trim() === "");
}
usernameInput.addEventListener('input', () =>{
    validateRequired(usernameInput)
})

passwordInput.addEventListener('input', () =>{
    validateRequired(passwordInput)
})

loginForm.addEventListener('submit', (event)=>{
    const usernameIsValid = validateRequired(usernameInput);
    const passwordIsValid = validateRequired(passwordInput);

    if(!usernameIsValid || !passwordIsValid)
        event.preventDefault();
})