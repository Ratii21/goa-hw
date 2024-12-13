function filter(numberArr){
    const evenNumbers = [];
    for (let i of numberArr){
        if (i % 2 === 0)
            evenNumbers.push(i)
    }
    return evenNumbers
}


console.log(filter([10,20,30,40,50]))
