def number(lines):
    new_lst = []
    for i in range(len(lines)):
        new_lst.append(str(i+1) + ": " + lines[i])
    return new_lst