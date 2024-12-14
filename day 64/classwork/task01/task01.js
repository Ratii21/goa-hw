const form = document.getElementById("f1");
const btn = document.getElementById("btn");
const c1 = document.getElementById("check")

function valid(){
    const name1 = form.elements.name.value
    const email1 = form.elements.email.value
    const password1 = form.elements.password.value
    

    if(c1.checked === false){
        alert("click to continue")
    }
    else if(name1 === "" || email1 === "" || password1 === ""){
        alert("fill out the fields")
    }
    else{
        console.log(name1)
        console.log(email1)
        console.log(password1)
    }


}


btn.onclick=valid
