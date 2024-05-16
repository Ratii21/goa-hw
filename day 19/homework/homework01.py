names = ["Rati","Gio","Dato","Luka","Elene"]
index = int(input("enter index between 0 and 4: "))

if index <= 4:
    print(names[index])
else:
    print("enter valid index! ")
    index = int(input("please enter index between 0 and 4: "))