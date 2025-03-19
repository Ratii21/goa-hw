let password = "GOA"
let i = 1
while(i <= 3){
    const input = prompt("enter password")
    if(password == input){
        alert("correct")
        i += 5
    }
    else{
        alert("incorrect, " + String(3 - i) + " tries left")
        i++
    }
}  