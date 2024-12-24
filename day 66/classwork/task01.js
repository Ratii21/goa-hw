let lst = []
let evenLst = []

for (let i = 1; i < 30; i += 1){
    lst.push(i)
}

for (let i of lst){
    if (i % 2 === 0){
        evenLst.push(i)
    }
}

return evenLst

