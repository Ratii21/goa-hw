def vaporcode(s):
    s1 = ""
    s2 = ""
    s = s.upper()
    for i in s:
        if i != " ":
            s1 += i + "  "
    for i in range(0,len(s1)-2):
        s2 += s1[i]
    return s2