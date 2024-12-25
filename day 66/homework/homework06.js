function count(str,ltr){
    let counter = 0
    for(let i of str){
        if (i === ltr){
            counter += 1
        }
    }
    return counter

}
console.log(count("iyo da ara iyo ra, iyo erti mela", " "))

