function togglePasswordVisibility(){
    var passwordInput = document.getElementById('password');
    if(passwordInput.type === 'password'){
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
}

function togglePasswordVisibilitySignUp(){

    var id_passwordInput2 = document.getElementById('id_password');
    if(id_passwordInput2.type === 'password'){
        id_passwordInput2.type = 'text';
    } else {
        id_passwordInput2.type = 'password';
    }
}

function togglePasswordVisibilitySignUpReType(){

    var id_passwordInput2 = document.getElementById('id_password2');
    if(id_passwordInput2.type === 'password'){
        id_passwordInput2.type = 'text';
    } else {
        id_passwordInput2.type = 'password';
    }
}