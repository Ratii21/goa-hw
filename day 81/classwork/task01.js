for(let i = 1; i <= 100; i++){
    if(i == 50){
        break
    }
    else if(i % 4 != 0){
        continue
    }
    else{
        console.log(i)
    }
}