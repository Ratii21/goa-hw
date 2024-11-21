def get_sum(a,b):
    total = 0
    if a > b:
        for i in range(b, a + 1):
            total = total + i
        return total
    elif b > a:
        for i in range(a,b + 1):
            total = total + i
        return total
    elif a == b:
        return a
        