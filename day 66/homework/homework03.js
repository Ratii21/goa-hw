function highest(lst){
    let x = 0
    for (let i of lst){
        if (i>x){
            x = i
        }
    }
    return x
}
console.log(highest([1,5,6,3,4,8,3]))