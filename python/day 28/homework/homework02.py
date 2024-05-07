def to_jaden_case(string):
    jaden_case = ""
    string = string.split()
    for i in string:
        jaden_case += i.capitalize() + " "
    return jaden_case.rstrip()

