def prime(number):
    
    is_prime = "prime or not prime"
    
    if number == 2 or number == 3 or number > 3 and (number  ** 2 - 1) % 24 == 0:
        is_prime = "prime"
    else: 
        is_prime = "not prime"
    
    return is_prime

print(prime(10))

print(prime(7))

#მეორე გზა

def check_if_prime(num):
    if num == 2:
        return str(num) + " is prime"
    if num <= 1:
        return str(num) + " is invalid number"
    
    count = 2
    
    for i in range(2, num):
        if num % i == 0:
            count = count + 1
        if count > 2:
            return str(num) + ' is not prime'
    
    return str(num) + ' is prime'

print(check_if_prime(5))

