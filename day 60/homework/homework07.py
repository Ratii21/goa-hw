def round_to_next5(n):
    counter = 0
    while n % 5 != 0:
        n += 1
        counter += 1
    return n