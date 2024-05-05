def prime(number):
    
    is_prime = "prime or not prime"
    
    if number == 2 or number == 3 or number > 3 and (number  ** 2 - 1) % 24 == 0:
        is_prime = "prime"
    else: 
        is_prime = "not prime"
    
    return is_prime

print(prime(10))

print(prime(7))
