def even(name):
    new_word = ""
    for i in range(0,len(name)):
        if i % 2 == 0:
            new_word += name[i]
    return new_word
print(even("rati"))