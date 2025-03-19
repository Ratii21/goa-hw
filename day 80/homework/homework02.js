function countDown(start){
    if(start > 1){
        for(start;start >= 1;start--){
            alert(String(start) + " seconds left")
        }
        alert("💥BOOM💥")
    }
    else{
        alert("start must be more than 1")
    }


}

countDown(3,1)