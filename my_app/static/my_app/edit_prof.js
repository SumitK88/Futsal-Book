const name_change=document.querySelector(".name_change")
const ch_name=document.querySelector(".ch_name")

const phone_change=document.querySelector(".phone_change")
const ch_phone=document.querySelector(".ch_phone")

//EventListener
name_change.addEventListener("click",()=>{
    ch_name.classList.toggle("active");
});

phone_change.addEventListener("click",()=>{
    ch_phone.classList.toggle("active");
});