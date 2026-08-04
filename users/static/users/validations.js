const usernameInput = document.getElementById('usernameInput');
const passwordInput = document.getElementById('passwordInput');
const loginForm = document.getElementById('loginForm')
const registerUsernameInput = document.getElementById('id_username');
const registerEmailInput = document.getElementById('id_email');
const registerEmailError = document.getElementById('emailError')
const registerPassword1Input = document.getElementById('id_password1');
const registerPassword2Input = document.getElementById('id_password2');
const registerPassword2Error = document.getElementById('password2Error')
const registerForm = document.getElementById('registerForm')
const registerPasswordToggle1 = document.getElementById('togglePassword1')
const registerPasswordToggle2 = document.getElementById('togglePassword2')
const loginTogglePassword = document.getElementById('loginTogglePassword')

function validateRequired(input){
    const isValid = input.value.trim() !== "";
    input.classList.toggle('is-invalid', !isValid);
    return isValid
}

function validateEmail(input){
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const value = input.value.trim();

    if(value === ""){
        registerEmailError.textContent = "Este campo es obligatorio";
        input.classList.add('is-invalid');
        return false;
    }else if(!emailRegex.test(value)){
        registerEmailError.textContent = "Ingresa un correo valido";
        input.classList.add('is-invalid');
        return false;
    }else{
        input.classList.remove('is-invalid');
        return true;
    }
}

function validatePassword(input){
    const value = input.value.trim();
    const matches = value === registerPassword1Input.value;
    if(value === ""){
        registerPassword2Error.textContent = "Este campo es obligatorio";
        input.classList.add('is-invalid');
        return false;
    }else if(!matches){
        registerPassword2Error.textContent = "Las contraseñas no coinciden";
        input.classList.add('is-invalid');
        return false;
    }else{
        input.classList.remove('is-invalid');
        return true;
    }
}

function togglePasswordField(passwordInput, toggleButton){
    const isHidden = passwordInput.type === 'password';
    passwordInput.type = isHidden ? 'text' : 'password'
    toggleButton.textContent = isHidden ? '🙈' : '👁️';
}

if(usernameInput){
    usernameInput.addEventListener('input', () =>{
        validateRequired(usernameInput)
    })
}

if(passwordInput){
    passwordInput.addEventListener('input', () =>{
        validateRequired(passwordInput)
    })
    if(loginTogglePassword){
        loginTogglePassword.addEventListener('click', ()=>{
            togglePasswordField(passwordInput, loginTogglePassword);
        })
    }
}

if(loginForm){
    loginForm.addEventListener('submit', (event)=>{
        const usernameIsValid = validateRequired(usernameInput);
        const passwordIsValid = validateRequired(passwordInput);

        if(!usernameIsValid || !passwordIsValid)
            event.preventDefault();
    })
}

if(registerUsernameInput){
    registerUsernameInput.addEventListener('input', ()=>{
        validateRequired(registerUsernameInput)
    })
}

if(registerEmailInput){
    registerEmailInput.addEventListener('input', ()=>{
        validateEmail(registerEmailInput)
    })
}

if(registerPassword1Input){
    registerPassword1Input.addEventListener('input', ()=>{
        validateRequired(registerPassword1Input)
        validatePassword(registerPassword2Input)
    })
    if(registerPasswordToggle1){
        registerPasswordToggle1.addEventListener('click', ()=>{
            togglePasswordField(registerPassword1Input, registerPasswordToggle1)
        })
    }
}

if(registerPassword2Input){
    registerPassword2Input.addEventListener('input', ()=>{
        validatePassword(registerPassword2Input)
    })
    if(registerPasswordToggle2){
        registerPasswordToggle2.addEventListener('click', ()=>{
            togglePasswordField(registerPassword2Input, registerPasswordToggle2)
        })
    }
}

if (registerForm) {
    registerForm.addEventListener('submit', (event) => {
        const usernameIsValid = validateRequired(registerUsernameInput);
        const emailIsValid = validateEmail(registerEmailInput);
        const password1IsValid = validateRequired(registerPassword1Input);
        const password2IsValid = validatePassword(registerPassword2Input);

        if (!usernameIsValid || !emailIsValid || !password1IsValid || !password2IsValid)
            event.preventDefault();
    });
}