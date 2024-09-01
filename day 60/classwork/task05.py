def length_of_sequence(arr,n):
    if arr.count(n) != 2:
        return 0
    else:
        count = 0
        n1 = arr.index(n)
        arr.pop(n1)
        n2 = arr.index(n) + 1
        return n2 - n1 + 1