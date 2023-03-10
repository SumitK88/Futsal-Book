const rating_element = document.querySelector('.ratings');
const rev_element = document.querySelector('.rev');
const rev_suc_element = document.querySelector('.rev-suc');
const send_element = document.querySelector('.send_b');

//EventListeners
for (i in rating_element) {
    i.addEventListener('click', ()=>{
        i.classList.toggle('active');
        i.classList.toggle('clicked');
    });
}
send_element.addEventListener('click', addrate);

//functions
function addrate() {
    rev_suc_element.classList.add('active');
}