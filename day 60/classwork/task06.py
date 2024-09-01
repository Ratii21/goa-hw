def tail_swap(strings):
    lst = []
    s1 = strings[0].split(":")[0]
    s2 = strings[0].split(":")[1]
    s3 = strings[1].split(":")[0]
    s4 = strings[1].split(":")[1]
    str1 = s1 + ":" + s4
    str2 = s3 + ":" + s2
    lst.append(str1)
    lst.append(str2)
    return lst