const form = document.querySelector("form");
const username = document.querySelector("input#userid");
const password = document.querySelector("input#pass")
const error_msg = document.querySelector("span.errors")

form.addEventListener("submit", (e)=>{
    e.preventDefault()
    error_msg.style.color = "red";
    
    if(username.value ==="" && password.value ===""){
        error_msg.innerText = "empty credentials not allowed";
    }
    else if(username.value ===" " && password.value ===" "){
        error_msg.innerText = "Spaces can't be credentials!";
    }
    else if(username.value ==="admin" && password.value !=="pass"){
        error_msg.innerText = "Invalid username/password."
    }
    else if(username.value ==="admin" && password.value ==="pass"){
        window.location = "admin.html";
    }
    else if(username.value !=="admin" && password.value ===""){
        error_msg.innerText = "Password can't be empty!";
    }
    else{
        window.location = "home.html";
    }
});