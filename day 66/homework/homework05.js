function check(str){
    let lastIndex = str.length - 1
    if(str[0] === str[lastIndex]){
        return "first letter is last letter"
    }
    else{
        return "first letter is not last letter"
    }
}
console.log(check("level"))