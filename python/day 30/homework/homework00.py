def rev_uper(word):
    reversed_word = ""

    for i in range(len(word)-1,-1,-1):
        reversed_word += (word[i])
    return reversed_word.upper()

    
print(rev_uper("rati"))