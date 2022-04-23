// Get the modal

// get ul with items inside
const orbitUl = document.querySelector('#orbit-ul')

orbitUl.addEventListener('click', (e) => {
    let modal = document.querySelector(`#${e.target.innerText}-modal`)
    modal.style.display = "block";
})

// Get the <span> element that closes each modal
const span = document.querySelectorAll('.close')
span.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.target.parentElement.parentElement.style.display = 'none'
    });
});

// // When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// }