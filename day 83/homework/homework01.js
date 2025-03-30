// lst.push() - ით ვამატებთ ელემენტს სიაში
function fizzBuzz(lst){
    let newLst = []
    for(let i of lst){
        if(i % 3 == 0){
            newLst.push("Fizz")
        }
        else if(i % 5 == 0){
            newLst.push("Buzz")
        }
        else if(i % 3 == 0 && i % 5 == 0){
            newLst.push("Fi")
        }
    }
    return newLst
}