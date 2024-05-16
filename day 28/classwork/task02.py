def digitize(n):
    reversed_list = []
    n = str(n)
    for i in range(len(n)-1, -1, -1):
        reversed_list.append(int(n[i]))
    return reversed_list