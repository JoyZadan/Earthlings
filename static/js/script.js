/*jshint esversion: 6 */

function deleteHiddenInput () {

    if (typeof(document.getElementById('password_is_valid')) != 'undefined' && document.getElementById('password_is_valid') != null) {
        let password_is_valid = document.getElementById('password_is_valid');
        password_is_valid.remove();
    }
}

function isUserNameValid(username) {
    /*
      Usernames can only have:
      - Lowercase Letters (a-z)
      - Numbers (0-9)
      - Underscores (_)
    */
    const res = /^[a-z\d_-]+$/.exec(username);
    return !!res;
}

//Password matching validation

function validateInput(id) {
    let element = document.getElementById(id);
    if (id === 'username') {
        const username = element.value
        if (isUserNameValid(username)) {
            document.getElementById(`${id}_error`).classList.add('hide')
            document.getElementById(`${id}_error`).innerHTML = '';
        } else {
            document.getElementById(`${id}_error`).classList.remove('hide')
            document.getElementById(`${id}_error`).innerHTML = 'Username can only contain a-z, 0-9 or _';
            deleteHiddenInput();
        }
    }
}

 //from here https://www.linkedin.com/pulse/create-strong-password-validation-regex-javascript-mitanshu-kumar/

 function checkPasswordValidation(value) {
     const isWhitespace = /^(?=.*\s)/;
     if (isWhitespace.test(value)) {
         deleteHiddenInput();
         return "Password must not contain Whitespaces.";
     }

     const isContainsUppercase = /^(?=.*[A-Z])/;
     if (!isContainsUppercase.test(value)) {
         deleteHiddenInput();
         return "Password must have at least one Uppercase Character.";
     }

     const isContainsLowercase = /^(?=.*[a-z])/;
     if (!isContainsLowercase.test(value)) {
         deleteHiddenInput();
         return "Password must have at least one Lowercase Character.";
     }

     const isContainsNumber = /^(?=.*[0-9])/;
     if (!isContainsNumber.test(value)) {
         deleteHiddenInput();
         return "Password must contain at least one Digit.";
     }

     const isContainsSymbol =
         /^(?=.*[~`!@#$%^&*()--+={}\[\]|\\:;"'<>,.?/_₹])/;
     if (!isContainsSymbol.test(value)) {
         deleteHiddenInput();
         return "Password must contain at least one Special Symbol.";
     }


     const isValidLength = /^.{5,16}$/;
     if (!isValidLength.test(value)) {
         deleteHiddenInput();
         return "Password must be 5-16 Characters Long.";
     }
     return null;
}




$("#password").on('change keydown paste input', function(e){
    if (checkPasswordValidation( e.target.value) !== 'null'){
        deleteHiddenInput();
        document.getElementById("password_error").classList.remove('hide');
        document.getElementById("password_error").innerHTML = checkPasswordValidation( e.target.value);
    } else {
        document.getElementById("password_error").classList.add('hide');
        deleteHiddenInput();
    }
});


$("#password2").on('change keydown paste input', function(e){
   let password1 = $('#password').val();
   if (password1 !== e.target.value){
       deleteHiddenInput();
        document.getElementById("password2_error").classList.remove('hide');
        document.getElementById("password2_error").innerHTML = "Passwords entered are not the same!";
        if (document.getElementById('password_is_valid')) {

        }
   }else {
        document.getElementById("password2_error").classList.add('hide');
        let form = document.getElementById('registration_form');
        if (document.getElementById('password_is_valid')) {

        } else {
            let newInput = addNewField();
            form.appendChild(newInput);
        }

        document.getElementById('register_submit').classList.remove('disabled')
   }
});

function addNewField (){
    const newInput = document.createElement("input");
    newInput.setAttribute("type", "hidden");
    newInput.setAttribute("name", `password_is_valid`);
    newInput.setAttribute("id", `password_is_valid`);
    newInput.setAttribute("value", `yes`);
    return newInput;
}