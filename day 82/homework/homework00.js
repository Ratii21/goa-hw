function solution(str){
    let revWord = ""
    let len = str.length
    for(let i = len-1; i >= 0; i--){
      revWord += str[i]
    }
        return revWord
  }