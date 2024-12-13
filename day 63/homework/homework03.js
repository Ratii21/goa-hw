function convertTemperature(temperature, scale = "C"){
    if(scale === "C"){
        return temperature * 1.8 + 32
    }
    else{
        return (temperature - 32)/1.8
    }
}