/*jshint esversion: 6 */
console.log('hello im working')


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
            console.log('username valid')
            document.getElementById(`${id}_error`).classList.add('hide')
            document.getElementById(`${id}_error`).innerHTML = '';
        } else {
            document.getElementById(`${id}_error`).classList.remove('hide')
            document.getElementById(`${id}_error`).innerHTML = 'Username can only contain a-z, 0-9 or _';
        }
    }
}

 //from here https://www.linkedin.com/pulse/create-strong-password-validation-regex-javascript-mitanshu-kumar/

 function checkPasswordValidation(value) {
     const isWhitespace = /^(?=.*\s)/;
     if (isWhitespace.test(value)) {
         return "Password must not contain Whitespaces.";
     }


     const isContainsUppercase = /^(?=.*[A-Z])/;
     if (!isContainsUppercase.test(value)) {
         return "Password must have at least one Uppercase Character.";
     }


     const isContainsLowercase = /^(?=.*[a-z])/;
     if (!isContainsLowercase.test(value)) {
         return "Password must have at least one Lowercase Character.";
     }


     const isContainsNumber = /^(?=.*[0-9])/;
     if (!isContainsNumber.test(value)) {
         return "Password must contain at least one Digit.";
     }


     const isContainsSymbol =
         /^(?=.*[~`!@#$%^&*()--+={}\[\]|\\:;"'<>,.?/_₹])/;
     if (!isContainsSymbol.test(value)) {
         return "Password must contain at least one Special Symbol.";
     }


     const isValidLength = /^.{5,16}$/;
     if (!isValidLength.test(value)) {
         return "Password must be 5-16 Characters Long.";
     }
     return null;
}


$("#password").on('change keydown paste input', function(e){
    if (checkPasswordValidation( e.target.value) !== 'null'){
        document.getElementById("password_error").classList.remove('hide');
        document.getElementById("password_error").innerHTML = checkPasswordValidation( e.target.value);
    } else {
        document.getElementById("password_error").classList.add('hide');
    }
});


$("#password2").on('change keydown paste input', function(e){
    console.log(e.target.value);
   let password1 = $('#password').val();
   if (password1 !== e.target.value){
        document.getElementById("password2_error").classList.remove('hide');
        document.getElementById("password2_error").innerHTML = "Passwords entered are not the same!";
   }else {
        document.getElementById("password2_error").classList.add('hide');
   }
});