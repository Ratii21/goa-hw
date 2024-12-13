function countOfNumbers(arr){
    let count = 0
    for(let i of arr){
        if(i % 2 === 0){
            count += 1
        }
    }
    return count
}

