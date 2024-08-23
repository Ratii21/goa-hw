def smash(words):
    sentence = ""
    for i in words:
        sentence += i + " "
    return sentence.rstrip()
