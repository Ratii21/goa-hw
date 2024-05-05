def solution(string):
    reversed_word = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_word += string[i]
    return reversed_word