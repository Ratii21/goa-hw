//spread operator "..." წვდომა მასივის ყველა ელემენტზე
function minMax(arr){
    let lst = []
    let max = Math.max(...arr)
    let min = Math.min(...arr)
    lst.push(min)
    lst.push(max)
    return lst
  }