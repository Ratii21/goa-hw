const myForm = document.getElementById("myform")
const submit = document.getElementById("sbmt")
let dataBase = []




function validForm(){
    const name = myForm.elements.name.value
    const email = myForm.elements.email.value
    const pass = myForm.elements.password.value

    if(pass < 8){
        alert("password is too short")

    }
    else{
        const form = {
            name: name,
            email: email,
            password: pass,
        }
        dataBase.push(form)        
    }
    console.log(dataBase)

}

submit.onclick=validForm

