def even_or_odd(number):
    
    num = "even or odd"
    
    if number % 2 == 0:
        num = "even"
    else:
        num = "odd"
    
    return num

print(even_or_odd(2))

print(even_or_odd(3))