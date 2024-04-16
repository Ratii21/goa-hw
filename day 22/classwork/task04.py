""" slice - ის ფუნქციონალი """

name = [1,2,3,4]
list = []

start = 0
end = 2
step = 1

while start < end:
    list.append(name[start])
    start += step
print(list)