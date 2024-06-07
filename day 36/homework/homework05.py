def all_nines(x):
    for i in range(100000):
        if int(str(i * x)) == int("9" * len(str(i * x))): 
            return i
    return -1

print(all_nines(10))