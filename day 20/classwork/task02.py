a = ["b", "c", "b", "a"]
b = ["",  "a", "a", "c"]

score = 0

for index in range(len(a)):
    if a[index] == b[index]:
        score = score + 4
    elif a[index] == "" or b[index] == "":
        score = score + 0
    else:
        score = score - 1

print(score)