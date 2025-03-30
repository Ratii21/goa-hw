function fakeBin(x){
    let bin = ""
    for(let i of x){
      if(i >= 5){
        bin += 1
      }
      else{
        bin += 0
      }
      
    }
    return bin
  }