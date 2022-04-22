/*jshint esversion: 6 */
console.log('hello im working')



function isUserNameValid(username) {
  /*
    Usernames can only have:
    - Lowercase Letters (a-z)
    - Numbers (0-9)
    - Underscores (_)
  */
  const res = /^[a-z0-9_]+$/.exec(username);
  const valid = !!res;
  return valid;
}


//Password matching validation

function validateInput(id) {
    let element = document.getElementById(id);
    if (id === 'username') {
        const username = element.value
        if (isUserNameValid(username)) {
            console.log('username valid')
            document.getElementById(`${id}_error`).innerHTML='';
        }else {
             document.getElementById(`${id}_error`).innerHTML='Username can only contain a-z, 0-9 or _';
        }
    }
}