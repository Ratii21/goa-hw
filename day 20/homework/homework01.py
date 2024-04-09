n1 = int(input("enter number: "))
n2 = int(input("enter number: "))
n3 = int(input("enter number: "))
n4 = int(input("enter number: "))
n5 = int(input("enter number: "))

numbers = [n1,n2,n3,n4,n5]
new_list = []

for num in numbers:
    #if ???
        new_list.append(num)

if len(new_list) == 0:
    print("new list is empty")
else:
    print(new_list)