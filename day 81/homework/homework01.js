for(let i = 1; i <= 30; i++){
    if(i % 2 != 0){
        continue
    }
    else if(i % 8 == 0){
        break
    }
    else{
        console.log(i)
    }
}