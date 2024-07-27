def is_palidrome (word):
    is_palidrome = "The word is a palindrome."

    for i in range(len(word)):
        if word[i] != word[len(word)-1-i]:
            is_palidrome = "The word is not a palindrome."

    print(is_palidrome)

