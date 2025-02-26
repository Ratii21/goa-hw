def zero_fuel(distance_to_pump, mpg, fuel_left):
    index = mpg * fuel_left 
    if index >= distance_to_pump:
        return True
    else:
        return False