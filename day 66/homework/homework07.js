function isPalidrom(str){
    let palidrome = "word is palidrome"
    let len = str.length
    for (let i = 0; i < len; i += 1){
        if(str[i] != str[len - 1 - i]){
            palidrome = "word is not palidrome"
        }
    }
    return palidrome
}

console.log(isPalidrom("level"))