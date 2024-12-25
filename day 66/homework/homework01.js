function listCheck(lst){
    if (lst.length === 0){
        return "list is empty"
    }
    else{
        let total = 0
        for(let i of lst){
            total += i
           
        }
        return total 
    }
}

console.log(listCheck([]))