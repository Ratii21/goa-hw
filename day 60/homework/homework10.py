def camel_case(s):
    str = ""
    s1 = s.title()
    lst = s1.split(" ")
    for i in lst:
        str += i
    return str