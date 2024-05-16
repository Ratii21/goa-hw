def no_space(x):
    word = ""
    for i in range(0,len(x)):
        if x[i] != " ":
            word += x[i]
    return word