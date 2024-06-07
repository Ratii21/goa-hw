

def max_multiple(divisor, bound):
    for i in range(1000000,-1,-1):
        if i % divisor == 0 and i <= bound and i > 0:
            return i
        
        