numbers = [1,2,3,4,5,6,7,8,9,10]
index = int(input("enter index between 0 and 9: "))

if index <= 9:
    print(numbers[index])
else:
    print("enter valid index! ")
    index = int(input("please enter index between 0 and 9: "))