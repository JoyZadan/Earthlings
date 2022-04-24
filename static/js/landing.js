// Get the modal

// get ul with items inside
const orbitUl = document.querySelector('#orbit-ul')

orbitUl.addEventListener('click', (e) => {
    let modal = document.querySelector(`#${e.target.innerText}-modal`)
    modal.style.display = "flex";
    document.body.classList.add("stop-scrolling");
        
})

// Get the <span> element that closes each modal
const span = document.querySelectorAll('.close')
span.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.target.parentElement.parentElement.style.display = 'none'
        document.body.classList.remove("stop-scrolling");
        
    });
});

// const body = document.querySelector('body')
// const nav = document.querySelector('nav')
// const orbit = document.querySelector('.orbit-wrapper');



// // body.style.backgroundImage = 'linear-gradient(180deg, rgba(255,255,255,1) 0%, rgba(68,214,44,1) 50%)'

// // intersection observers 

// const heroOptions = {
//     rootMargin: "-10px 0px 0px 0px"
// };

// const heroObserver = new IntersectionObserver((entries, heroObserver) => {
//     entries.forEach(entry => {
//         if(!entry.isIntersecting){
//                 nav.style.opacity = '1'
//                 nav.classList.add('fixed-top')

//             }
            
            
//          else {
//             // nav.classList.remove('fixed-top')
//             nav.style.opacity = '0'
            

//         }
//     })
// }, heroOptions)


// heroObserver.observe(orbit)

// const appearOptions = {
//     threshold: 0,
//     rootMargin: "0px 0px -200px 0px"
// }



