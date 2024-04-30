def sum_of_numbers(list):
    
    sum = 0
    
    for i in range(0,len(list)):
        
        if i % 2 == 0:
            sum += list[i]
    
    return sum

print(sum_of_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
