def repeats(arr):
    sum = 0
    for i in arr:
        if arr.count(i) == 1:
            sum += i
    return sum


