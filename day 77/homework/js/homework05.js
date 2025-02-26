const zeroFuel = (distanceToPump, mpg, fuelLeft) => {
    let index = mpg * fuelLeft;
    if (index >= distanceToPump){
      return true}
    return false
  
  };