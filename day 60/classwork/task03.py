def reverse_number(n):
    s1 = str(n)
    s = ""
    if n < 0:
        s += "-"
        for i in range(len(s1)-1,0,-1):
            s += s1[i]
        return int(s)
    elif n == 0:
        return 0
    else:
        for i in range(len(s1)-1,-1,-1):
            s += s1[i]
        return int(s)