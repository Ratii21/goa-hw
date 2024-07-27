def vowel(s):
    counter = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in s:
        if i in vowels:
            counter += 1
    return counter
