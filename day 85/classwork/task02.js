function replace(s) {
    let newS = ""
    for(let i of s){
      if(i != "a" && i != "e" && i != "i" && i != "o" && i != "u" && i != "A" && i != "E" && i != "I" && i != "U" && i != "O"){
        newS += i
      }
      else{
        newS += "!"
      }

  }    return newS
}