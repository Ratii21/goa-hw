function moreOrLess(n1,n2){
    if (n1*n2 > 100){
        return "more than 100"
    }
    else if(n1*n2 === 100){
        return "equals to 100"
    }
    else{
        return "less than 100"
    }
}
console.log(moreOrLess(5,19))