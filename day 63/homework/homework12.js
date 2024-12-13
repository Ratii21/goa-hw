function sumOfNumbers(arr){
    let total = 0;
    for(let i of arr){
        total += i;
    }
    return total
}

alert(sumOfNumbers([1,2,3,4,5]))