for(let i = 1; i <= 20; i++){
    if(i == 15){
        break
    }
    else if(i % 3 == 0){
        continue
    }
    else{
        console.log(i)
    }
}