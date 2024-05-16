word1 = input("enter any word: ")
word2  = input("enter any word: ")
word3  = input("enter any word: ")
word4  = input("enter any word: ")
word5  = input("enter any word: ")
list = [word1,word2,word3,word4,word5]
new_list = []

for i in list:
    new_list += i[0]

print(new_list)