function highest(lst){
    let x = 0
    for (let i of lst){
        if (i>x){
            x = i
        }
    }
    return x
}