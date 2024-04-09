list1 = []
list2 = []

for i in range(20,31):
    list1.append(i)
print(list1)
for i in range(30,51):
    if i % 5 == 0:
        list2.append(i)
print(list2)

list3 = list1 + list2
print(list3)