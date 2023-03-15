const rating_element = document.querySelectorAll('.ratings');
const rev_suc_element = document.querySelector('.msgbox');
const send_element = document.querySelector('.send_b');
const sent_element = document.querySelector('.sent_b');

//EventListeners
for (let i=0;i< rating_element.length;i++){
    rating_element[i].addEventListener('click', ()=>{
        for(let j=0;j< rating_element.length;j++){
            rating_element[j].classList.remove('clicked');
        }
        rating_element[i].classList.toggle('clicked');
    });
}
send_element.addEventListener('click',()=>{
    rev_suc_element.showModal();
});
sent_element.addEventListener('click',()=>{
    rev_suc_element.close();
});