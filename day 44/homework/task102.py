list = [5, 2, 7, 10, 1]

min = list[0]
max = list[0]

for i in list:
    if i < min:
        min = i
    if i > max:
        max = i
print(min)
print(max)