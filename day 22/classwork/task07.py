numbers = [1,2,3,4,5,6,7,8,9,10]
list = []

start = 9
end = -1
step = -1

while start > end:
    list.append(numbers[start])
    start += step
print(list)