def even_div_2_odd_mul_2(numbers):
    
    result = []
    
    for i in range(0,len(numbers)):
        
        if numbers[i] % 2 == 0:
            result.append(numbers[i] / 2) 
        else:
            result.append(numbers[i] * 2) 
            
    return result

print(even_div_2_odd_mul_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))